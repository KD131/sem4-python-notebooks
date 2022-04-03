import bs4
import requests

def scrape_links(url, *starts_with):
    r = requests.get(url)
    r.raise_for_status()
    soup = bs4.BeautifulSoup(r.text, "html.parser")
    links = [link + "\n" for link in soup.select("a")
                if link.get("href")
                and link.get("href").startswith(starts_with)]
    with open("debug", "w", encoding="utf-8") as f:
        f.write(r.text)
    return links

if __name__ == "__main__":
    links = scrape_links("https://github.com/Hartmannsolution/docker_notebooks/blob/master/notebooks/00%20Videos.ipynb", "https://youtu.be/", "https://youtube.com/")
    with open("links", "w") as file:
        file.writelines(links)
