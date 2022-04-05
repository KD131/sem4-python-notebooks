import argparse

import bs4
import requests
from selenium import webdriver
from selenium.webdriver.firefox.options import Options


def source_from_request(url):
    r = requests.get(url)
    r.raise_for_status()
    return r.text

def source_from_selenium(url):
    options = Options()
    options.headless = True
    browser = webdriver.Firefox(options=options)
    browser.get(url)
    
    browser.implicitly_wait(2)
    if url.endswith(".ipynb"):
        browser.switch_to.frame(0)

    source = browser.page_source
    
    browser.close()
    browser.quit()

    return source

def scrape_links(source, *starts_with):
    """Returns list of links with newline appended for easier writing to file.
    Could be changed to just a list and then for writing to file, you could iterate it normally and append \n manually, or you could join with \n and append one at the very end.
    """
    soup = bs4.BeautifulSoup(source, "html.parser")
    links = [link.get("href") + "\n" for link in soup.select("a")
                if link.get("href")
                and link.get("href").startswith(starts_with)]
    return links

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Scrapes links from given URL.")
    parser.add_argument("url", type=str, help="The URL to scrape for links.")
    # if refactored to use regex, call it contains or patterns or something
    parser.add_argument("--starts_with", "-s", nargs="*", default=["https://youtu.be/", "https://youtube.com/"], help="What the links should start with to be targeted. Takes more arguments. Default is YouTube links.")
    parser.add_argument("--selenium", action="store_true", help="Uses Selenium to scrape using a simulated browser. Default is using an HTTP request. Use this if the site generates content after loading the page, so a normal request doesn't give the desired result.")
    args = parser.parse_args()

    url = args.url
    # https://github.com/Hartmannsolution/docker_notebooks/blob/master/notebooks/00%20Videos.ipynb
    if args.selenium:
        source = source_from_selenium(url)
    else:
        source = source_from_request(url)

    links = scrape_links(source, *args.starts_with)
    with open("links.txt", "w") as file:
        file.writelines(links)
