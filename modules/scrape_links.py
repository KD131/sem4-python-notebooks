import bs4
import requests
from selenium import webdriver
from selenium.webdriver.firefox.options import Options

def scrape_links(url, *starts_with):
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
    
    # r = requests.get(url)
    # r.raise_for_status()

    soup = bs4.BeautifulSoup(source, "html.parser")
    links = [link.get("href") + "\n" for link in soup.select("a")
                if link.get("href")
                and link.get("href").startswith(starts_with)]
    return links

if __name__ == "__main__":
    links = scrape_links("https://github.com/Hartmannsolution/docker_notebooks/blob/master/notebooks/00%20Videos.ipynb", "https://youtu.be/", "https://youtube.com/")
    with open("links.txt", "w") as file:
        file.writelines(links)
