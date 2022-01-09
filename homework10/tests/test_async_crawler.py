import ast
import os

import pytest

from hw.async_crawler import get_current_usdrub_rate, get_html, get_top_10

test_dir = os.path.dirname(os.path.abspath(__file__))
os.chdir(test_dir)


with open('companies.py') as file:
    contents = file.read()
    companies = ast.literal_eval(contents)


@pytest.mark.asyncio
async def test_get_current_usdrub_rate():
    assert isinstance(await get_current_usdrub_rate(), float)


@pytest.mark.asyncio
async def test_get_html():
    url = "https://markets.businessinsider.com/index/components/s&p_500?p=1"
    assert isinstance(await get_html(url), str)


def test_get_top_10_price():
    result = get_top_10(companies, "price", True)
    with open('top_10_price.py') as file:
        contents = file.read()
        expected_result = ast.literal_eval(contents)
    assert result == expected_result


def test_get_top_10_growth():
    result = get_top_10(companies, "growth", True)
    with open('top_10_growth.py') as file:
        contents = file.read()
        expected_result = ast.literal_eval(contents)
    assert result == expected_result


def test_get_top_10_poten_profit():
    result = get_top_10(companies, "potential_profit", True)
    with open('top_10_poten_profit.py') as file:
        contents = file.read()
        expected_result = ast.literal_eval(contents)
    assert result == expected_result


def test_get_top_10_pe():
    result = get_top_10(companies, "PE", False)
    with open('top_10_pe.py') as file:
        contents = file.read()
        expected_result = ast.literal_eval(contents)
    assert result == expected_result
