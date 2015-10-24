#!/usr/bin/env python3

import requests
from bs4 import BeautifulSoup


def createHtmlParser(url):
    page = requests.get(url)
    pageParser = BeautifulSoup(page.text, "html.parser")
    return pageParser


def getChapterName(pageParser):
    currentChapterName = pageParser.find("span", class_="redhotl").string
    return currentChapterName


def getNextURLPostfix(pageParser, reverse=False):
    try:
        if reverse == True:
            nextURLPostfix = pageParser.find("a", id="prev_chapter")["href"]
        else:
            nextURLPostfix = pageParser.find("a", id="next_chapter")["href"]
    except TypeError:
        nextURLPostfix = None
    return nextURLPostfix

def getURLPrefix(url):
    return "/".join(url.split("/")[:-1])


def main():
    url = input("Enter the URL: ")
    reversal = int(input("Does direction reverse?(0 for No, 1 for Yes): "))
    urlPrefix = getURLPrefix(url)

    while url:
        parser = createHtmlParser(url)

        chapterName = getChapterName(parser)
        print((chapterName, url))

        #Get next chapter url.
        try:
            url = urlPrefix + "/" + getNextURLPostfix(parser, reversal)
        except TypeError:
            url = None

main()
