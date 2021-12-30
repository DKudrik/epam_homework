import asyncio
import json
import re
from functools import lru_cache

import aiohttp
from bs4 import BeautifulSoup


async def get_current_usdrub_rate(url=None) -> float:
    """
    Returns current rate of usd/rub exchange from the site or Russian Central
    Bank.

    :return: current usr/rub rate of exchange
    """
    base_url = "http://www.cbr.ru/scripts/XML_daily.asp?date_req="
    url = base_url if url is None else url
    html = await get_html(url)
    soup = BeautifulSoup(html, "lxml")
    currencies = soup.find_all("valute")
    usdrub_rate = float(currencies[10].value.text.replace(",", "."))
    return usdrub_rate


async def get_html(url: str) -> str:
    """
    Gets html from the URL and returns it as a string.

    :param url: page url
    :return: page text
    """
    async with aiohttp.ClientSession() as session:
        async with session.get(url) as response:
            return await response.text()


async def get_code(soup) -> str:
    """
    Aceepts soup data of a company and returns its ticker.

    :param soup: company's soup data from personal page
    :return: ticker of a company
    """
    code = (
        soup.find("span", class_="price-section__category")
        .find("span")
        .text.strip(" , ,")
    )
    return code


async def get_stock_price_rub(soup):
    """
    Get the company's price from it's soup and multiplies it with the usdrub
    exchange rate to return the price in rub.

    :param soup: company's soup data from personal page
    :return: company's stock price in rub
    """
    stock_price = soup.find("span", class_="price-section__current-value").text.replace(
        ",", ""
    )
    usdrub_rate = await get_current_usdrub_rate()
    stock_price_rub = float(stock_price) * usdrub_rate
    return stock_price_rub


async def get_pe(soup):
    """
    Get the company's P/E ratio from it's soup and returns it. In case there
    it no P/E - returns infinity.

    :param soup: company's soup data from personal page
    :return: P/E ratio
    """
    try:
        pe = (
            soup.find("div", text=re.compile("P/E Ratio"))
            .parent.text.replace("P/E Ratio", "")
            .strip()
            .replace(",", "")
        )
        pe = float(pe)
    except AttributeError:
        pe = float("inf")
    return pe


async def get_poten_profit(soup):
    """
    Returns potential profit in percents, calculated as if the stock was bought
    at 52 week low and sold at 52 week high. In case any or both the values are
    absent the func returns minus infinity.

    :param soup: company's soup data from personal page
    :return: potential profit in percents
    """
    try:
        low = (
            soup.find("div", text=re.compile("52 Week Low"))
            .parent.text.replace("52 Week Low", "")
            .strip()
            .replace(",", "")
        )
        high = (
            soup.find("div", text=re.compile("52 Week High"))
            .parent.text.replace("52 Week High", "")
            .strip()
            .replace(",", "")
        )
    except AttributeError:
        poten_profit = float("-inf")
    else:
        low = float(low)
        high = float(high)
        poten_profit = (high - low) / low * 100
    return poten_profit


async def get_company_soup(comp_data):
    """
    Gets company's soup from it's personal page

    :param comp_data: company's personal page soup
    :return: soup object
    """
    comp_link = comp_data.find("a").get("href")
    base_url = "https://markets.businessinsider.com"
    html = await get_html(base_url + comp_link)
    soup = BeautifulSoup(html, "lxml")
    return soup


@lru_cache
def get_comp_name(soup):
    comp_name = soup.find("span", class_="price-section__label").text.rstrip()
    return comp_name


async def process_general_page(PAGE_COUNT: int):
    """
    Collects data from the general pages and the pages of the companies and
    return a dict with the companies data.
    """
    companies = {}
    tasks = []

    for page in range(1, PAGE_COUNT + 1):
        url = "https://markets.businessinsider.com/index/components/s&p_500?p="
        next_page_url = url + str(page)
        html = await get_html(next_page_url)
        general_soup = BeautifulSoup(html, "lxml")
        companies_data = general_soup.find("tbody", class_="table__tbody").find_all(
            "tr"
        )
        for comp_data in companies_data:
            base_url = "https://markets.businessinsider.com/"
            comp_url = comp_data.find("a").get("href")
            final_comp_url = base_url + comp_url
            html = await get_html(final_comp_url)
            soup = BeautifulSoup(html, "lxml")
            comp_name = get_comp_name(soup)
            growth = (
                general_soup.find("a", href=comp_url)
                .parent.parent.find_all("span")[-1]
                .text.strip("%")
            )
            growth = float(growth)
            companies[comp_name] = {}
            companies[comp_name]["growth"] = growth
            tasks.append(asyncio.create_task(get_company_soup(comp_data)))
    await asyncio.gather(*tasks)
    for task in tasks:
        soup = task.result()
        comp_name = get_comp_name(soup)
        companies[comp_name]["code"] = await get_code(soup)
        companies[comp_name]["name"] = comp_name
        companies[comp_name]["price"] = await get_stock_price_rub(soup)
        companies[comp_name]["PE"] = await get_pe(soup)
        companies[comp_name]["potential_profit"] = await get_poten_profit(soup)
    return companies


def get_top_10(companies, key: str, reverse: bool) -> list[dict]:
    """

    :param companies: dict values obj with company data
    :param key: parameter for sorting
    :param reverse: direction of sorting
    :return: dictionary of top 10 companies
    """
    companies_list = list(companies.values())
    top_10 = sorted(companies_list, key=lambda company: company[key], reverse=reverse)[
        :10
    ]
    return top_10


async def main():
    PAGE_COUNT = 11
    companies = await process_general_page(PAGE_COUNT)

    max_keys = ["price", "growth", "potential_profit"]
    for key in max_keys:
        with open(f"top_{key}.json", "w") as file:
            top_10 = get_top_10(companies, key, True)
            json.dump(top_10, file, indent=4)

    min_keys = ["PE"]
    for key in min_keys:
        with open(f"top_{key}.json", "w") as file:
            top_10 = get_top_10(companies, key, False)
            json.dump(top_10, file, indent=4)


if __name__ == "__main__":
    loop = asyncio.get_event_loop()
    loop.run_until_complete(main())
    loop.close()
