import pytest
from hw.async_crawler import get_current_usdrub_rate, get_html, get_top_10

companies = {
    "3M Co.": {
        "growth": 1.18,
        "code": "MMM",
        "name": "3M Co.",
        "price": 13137.936731999998,
        "PE": 19.91,
        "potential_profit": 27.85290338371167,
    },
    "A.O. Smith Corp.": {
        "growth": 52.36,
        "code": "AOS",
        "name": "A.O. Smith Corp.",
        "price": 6317.080577999999,
        "PE": 25.06,
        "potential_profit": 65.55299539170507,
    },
    "Abbott Laboratories": {
        "growth": 31.26,
        "code": "ABT",
        "name": "Abbott Laboratories",
        "price": 10395.158595999997,
        "PE": 29.76,
        "potential_profit": 35.26006074411541,
    },
    "AbbVie Inc": {
        "growth": 29.92,
        "code": "ABBV",
        "name": "AbbVie Inc",
        "price": 9971.663045999998,
        "PE": 9.91,
        "potential_profit": 33.44465180237698,
    },
    "ABIOMED Inc.": {
        "growth": 14.36,
        "code": "ABMD",
        "name": "ABIOMED Inc.",
        "price": 26650.022575999996,
        "PE": 63.24,
        "potential_profit": 48.275730087648796,
    },
    "Accenture plc": {
        "growth": 59.91,
        "code": "ACN",
        "name": "Accenture plc",
        "price": 30591.10899,
        "PE": 32.42,
        "potential_profit": 72.61821040003309,
    },
    "Activision Blizzard Inc.": {
        "growth": -28.42,
        "code": "ATVI",
        "name": "Activision Blizzard Inc.",
        "price": 4946.428024,
        "PE": 26.4,
        "potential_profit": 85.33687943262413,
    },
    "Adobe Inc.": {
        "growth": 15.78,
        "code": "ADBE",
        "name": "Adobe Inc.",
        "price": 41929.005505999994,
        "PE": 47.1,
        "potential_profit": 66.24839583630401,
    },
    "Advance Auto Parts Inc.": {
        "growth": 49.06,
        "code": "AAP",
        "name": "Advance Auto Parts Inc.",
        "price": 17751.460428,
        "PE": 18.27,
        "potential_profit": 69.75136192205615,
    },
    "AES Corp.": {
        "growth": 1.5,
        "code": "AES",
        "name": "AES Corp.",
        "price": 1751.430292,
        "PE": 15.98,
        "potential_profit": 28.571428571428577,
    },
    "Aflac Inc": {
        "growth": 32.47,
        "code": "AFL",
        "name": "Aflac Inc",
        "price": 4329.965805999999,
        "PE": 8.88,
        "potential_profit": 37.05772811918064,
    },
    "Agilent Technologies Inc.": {
        "growth": 34.62,
        "code": "A",
        "name": "Agilent Technologies Inc.",
        "price": 11832.833923999999,
        "PE": 30.82,
        "potential_profit": 59.66035387214368,
    },
    "Air Products and Chemicals Inc.": {
        "growth": 12.53,
        "code": "APD",
        "name": "Air Products and Chemicals Inc.",
        "price": 22496.083616,
        "PE": 24.93,
        "potential_profit": 28.744659206510676,
    },
    "Alaska Air Group Inc.": {
        "growth": -0.04,
        "code": "ALK",
        "name": "Alaska Air Group Inc.",
        "price": 3840.9205099999995,
        "PE": -5.1,
        "potential_profit": 60.43647363872082,
    },
    "Albemarle Corp.": {
        "growth": 55.69,
        "code": "ALB",
        "name": "Albemarle Corp.",
        "price": 17112.90279,
        "PE": 35.35,
        "potential_profit": 117.74772081901061,
    },
}


@pytest.mark.asyncio
async def test_get_current_usdrub_rate():
    assert isinstance(await get_current_usdrub_rate(), float)


@pytest.mark.asyncio
async def test_get_html():
    url = "https://markets.businessinsider.com/index/components/s&p_500?p=1"
    assert isinstance(await get_html(url), str)


def test_get_top_10_price():
    result = get_top_10(companies, "price", True)
    expected_result = [
        {
            "growth": 15.78,
            "code": "ADBE",
            "name": "Adobe Inc.",
            "price": 41929.005505999994,
            "PE": 47.1,
            "potential_profit": 66.24839583630401,
        },
        {
            "growth": 59.91,
            "code": "ACN",
            "name": "Accenture plc",
            "price": 30591.10899,
            "PE": 32.42,
            "potential_profit": 72.61821040003309,
        },
        {
            "growth": 14.36,
            "code": "ABMD",
            "name": "ABIOMED Inc.",
            "price": 26650.022575999996,
            "PE": 63.24,
            "potential_profit": 48.275730087648796,
        },
        {
            "growth": 12.53,
            "code": "APD",
            "name": "Air Products and Chemicals Inc.",
            "price": 22496.083616,
            "PE": 24.93,
            "potential_profit": 28.744659206510676,
        },
        {
            "growth": 49.06,
            "code": "AAP",
            "name": "Advance Auto Parts Inc.",
            "price": 17751.460428,
            "PE": 18.27,
            "potential_profit": 69.75136192205615,
        },
        {
            "growth": 55.69,
            "code": "ALB",
            "name": "Albemarle Corp.",
            "price": 17112.90279,
            "PE": 35.35,
            "potential_profit": 117.74772081901061,
        },
        {
            "growth": 1.18,
            "code": "MMM",
            "name": "3M Co.",
            "price": 13137.936731999998,
            "PE": 19.91,
            "potential_profit": 27.85290338371167,
        },
        {
            "growth": 34.62,
            "code": "A",
            "name": "Agilent Technologies Inc.",
            "price": 11832.833923999999,
            "PE": 30.82,
            "potential_profit": 59.66035387214368,
        },
        {
            "growth": 31.26,
            "code": "ABT",
            "name": "Abbott Laboratories",
            "price": 10395.158595999997,
            "PE": 29.76,
            "potential_profit": 35.26006074411541,
        },
        {
            "growth": 29.92,
            "code": "ABBV",
            "name": "AbbVie Inc",
            "price": 9971.663045999998,
            "PE": 9.91,
            "potential_profit": 33.44465180237698,
        },
    ]
    assert result == expected_result


def test_get_top_10_growth():
    result = get_top_10(companies, "growth", True)
    expected_result = [
        {
            "growth": 59.91,
            "code": "ACN",
            "name": "Accenture plc",
            "price": 30591.10899,
            "PE": 32.42,
            "potential_profit": 72.61821040003309,
        },
        {
            "growth": 55.69,
            "code": "ALB",
            "name": "Albemarle Corp.",
            "price": 17112.90279,
            "PE": 35.35,
            "potential_profit": 117.74772081901061,
        },
        {
            "growth": 52.36,
            "code": "AOS",
            "name": "A.O. Smith Corp.",
            "price": 6317.080577999999,
            "PE": 25.06,
            "potential_profit": 65.55299539170507,
        },
        {
            "growth": 49.06,
            "code": "AAP",
            "name": "Advance Auto Parts Inc.",
            "price": 17751.460428,
            "PE": 18.27,
            "potential_profit": 69.75136192205615,
        },
        {
            "growth": 34.62,
            "code": "A",
            "name": "Agilent Technologies Inc.",
            "price": 11832.833923999999,
            "PE": 30.82,
            "potential_profit": 59.66035387214368,
        },
        {
            "growth": 32.47,
            "code": "AFL",
            "name": "Aflac Inc",
            "price": 4329.965805999999,
            "PE": 8.88,
            "potential_profit": 37.05772811918064,
        },
        {
            "growth": 31.26,
            "code": "ABT",
            "name": "Abbott Laboratories",
            "price": 10395.158595999997,
            "PE": 29.76,
            "potential_profit": 35.26006074411541,
        },
        {
            "growth": 29.92,
            "code": "ABBV",
            "name": "AbbVie Inc",
            "price": 9971.663045999998,
            "PE": 9.91,
            "potential_profit": 33.44465180237698,
        },
        {
            "growth": 15.78,
            "code": "ADBE",
            "name": "Adobe Inc.",
            "price": 41929.005505999994,
            "PE": 47.1,
            "potential_profit": 66.24839583630401,
        },
        {
            "growth": 14.36,
            "code": "ABMD",
            "name": "ABIOMED Inc.",
            "price": 26650.022575999996,
            "PE": 63.24,
            "potential_profit": 48.275730087648796,
        },
    ]
    assert result == expected_result


def test_get_top_10_poten_profit():
    result = get_top_10(companies, "potential_profit", True)
    expected_result = [
        {
            "growth": 55.69,
            "code": "ALB",
            "name": "Albemarle Corp.",
            "price": 17112.90279,
            "PE": 35.35,
            "potential_profit": 117.74772081901061,
        },
        {
            "growth": -28.42,
            "code": "ATVI",
            "name": "Activision Blizzard Inc.",
            "price": 4946.428024,
            "PE": 26.4,
            "potential_profit": 85.33687943262413,
        },
        {
            "growth": 59.91,
            "code": "ACN",
            "name": "Accenture plc",
            "price": 30591.10899,
            "PE": 32.42,
            "potential_profit": 72.61821040003309,
        },
        {
            "growth": 49.06,
            "code": "AAP",
            "name": "Advance Auto Parts Inc.",
            "price": 17751.460428,
            "PE": 18.27,
            "potential_profit": 69.75136192205615,
        },
        {
            "growth": 15.78,
            "code": "ADBE",
            "name": "Adobe Inc.",
            "price": 41929.005505999994,
            "PE": 47.1,
            "potential_profit": 66.24839583630401,
        },
        {
            "growth": 52.36,
            "code": "AOS",
            "name": "A.O. Smith Corp.",
            "price": 6317.080577999999,
            "PE": 25.06,
            "potential_profit": 65.55299539170507,
        },
        {
            "growth": -0.04,
            "code": "ALK",
            "name": "Alaska Air Group Inc.",
            "price": 3840.9205099999995,
            "PE": -5.1,
            "potential_profit": 60.43647363872082,
        },
        {
            "growth": 34.62,
            "code": "A",
            "name": "Agilent Technologies Inc.",
            "price": 11832.833923999999,
            "PE": 30.82,
            "potential_profit": 59.66035387214368,
        },
        {
            "growth": 14.36,
            "code": "ABMD",
            "name": "ABIOMED Inc.",
            "price": 26650.022575999996,
            "PE": 63.24,
            "potential_profit": 48.275730087648796,
        },
        {
            "growth": 32.47,
            "code": "AFL",
            "name": "Aflac Inc",
            "price": 4329.965805999999,
            "PE": 8.88,
            "potential_profit": 37.05772811918064,
        },
    ]
    assert result == expected_result


def test_get_top_10_pe():
    result = get_top_10(companies, "PE", False)
    expected_result = [
        {
            "growth": -0.04,
            "code": "ALK",
            "name": "Alaska Air Group Inc.",
            "price": 3840.9205099999995,
            "PE": -5.1,
            "potential_profit": 60.43647363872082,
        },
        {
            "growth": 32.47,
            "code": "AFL",
            "name": "Aflac Inc",
            "price": 4329.965805999999,
            "PE": 8.88,
            "potential_profit": 37.05772811918064,
        },
        {
            "growth": 29.92,
            "code": "ABBV",
            "name": "AbbVie Inc",
            "price": 9971.663045999998,
            "PE": 9.91,
            "potential_profit": 33.44465180237698,
        },
        {
            "growth": 1.5,
            "code": "AES",
            "name": "AES Corp.",
            "price": 1751.430292,
            "PE": 15.98,
            "potential_profit": 28.571428571428577,
        },
        {
            "growth": 49.06,
            "code": "AAP",
            "name": "Advance Auto Parts Inc.",
            "price": 17751.460428,
            "PE": 18.27,
            "potential_profit": 69.75136192205615,
        },
        {
            "growth": 1.18,
            "code": "MMM",
            "name": "3M Co.",
            "price": 13137.936731999998,
            "PE": 19.91,
            "potential_profit": 27.85290338371167,
        },
        {
            "growth": 12.53,
            "code": "APD",
            "name": "Air Products and Chemicals Inc.",
            "price": 22496.083616,
            "PE": 24.93,
            "potential_profit": 28.744659206510676,
        },
        {
            "growth": 52.36,
            "code": "AOS",
            "name": "A.O. Smith Corp.",
            "price": 6317.080577999999,
            "PE": 25.06,
            "potential_profit": 65.55299539170507,
        },
        {
            "growth": -28.42,
            "code": "ATVI",
            "name": "Activision Blizzard Inc.",
            "price": 4946.428024,
            "PE": 26.4,
            "potential_profit": 85.33687943262413,
        },
        {
            "growth": 31.26,
            "code": "ABT",
            "name": "Abbott Laboratories",
            "price": 10395.158595999997,
            "PE": 29.76,
            "potential_profit": 35.26006074411541,
        },
    ]
    assert result == expected_result
