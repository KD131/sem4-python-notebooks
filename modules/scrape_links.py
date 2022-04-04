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
    source = source_from_selenium("https://github.com/Hartmannsolution/docker_notebooks/blob/master/notebooks/00%20Videos.ipynb")
    links = scrape_links(source, "https://youtu.be/", "https://youtube.com/")
    with open("links.txt", "w") as file:
        file.writelines(links)
