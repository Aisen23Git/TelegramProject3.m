import httpx
from parsel import Selector

# httpx - sync, async
# request - sync
# crawler, scraper, parsel

# crawler, scraper, parsel

MAIN_URL = "https://www.house.kg/snyat"


def get_page():
    response = httpx.get(MAIN_URL)
    # print("Status code", response.status_code)
    return response.text

def get_page_title(page):
    selector = Selector(text = page)
    title = selector.css("title::text").get()
    return title


def get_links(page):

    selector = Selector(text=page)
    links = selector.css(".list-item a::attr(href)").getall()
    return get_links


if __name__ == "__main__":
    page = get_page()
    # print(page[:300])
    # title = get_page_title(page)
    # print(title)
    links = get_links(page)
    print(links)
