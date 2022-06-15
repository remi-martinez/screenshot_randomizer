import string
import random
import re
import cloudscraper
from django import template

register = template.Library()


def scrap_website(url):
    scraper = cloudscraper.create_scraper()
    return scraper.get(url).text


def get_random_url():
    fullListStr = list(string.ascii_lowercase) + ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']

    randomString = ''.join(random.choices(fullListStr, k=6))
    randomUrl = "https://prnt.sc/" + randomString
    notFoundUrl = "https://i.imgur.com/removed.png"

    scraped = scrap_website(randomUrl)

    imgURLBrut = re.search(r'og:image" content=".*\.(jpg|jpeg|png|gif)"', scraped)
    if imgURLBrut is None:
        return notFoundUrl
    else:
        imgURLClean = re.search(r'http.*\.(jpg|jpeg|png|gif)', imgURLBrut.group(0))

    if imgURLClean is None:
        return notFoundUrl
    else:
        return imgURLClean.group(0)
