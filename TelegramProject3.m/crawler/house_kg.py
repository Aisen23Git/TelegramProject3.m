# import httpx
# from parsel import Selector
#
# # httpx - sync, async
# # request - sync
# # crawler, scraper, parsel
#
# # crawler, scraper, parsel
#
# MAIN_URL = "https://www.house.kg/snyat"
#
#
# def get_page():
#     response = httpx.get(MAIN_URL, timeout = 10)
#     # print("Status code", response.status_code)
#     return response.text
#
# def get_page_title(page):
#     selector = Selector(text = page)
#     title = selector.css("title::text").get()
#     return title
#
#
# def get_links(page):
#
#     selector = Selector(text=page)
#     links = selector.css(".listing a::attr(href)").getall()
#     return list(map(lambda x: "https://www.house.kg/snyat"))
#
#
# if __name__ == "__main__":
#     page = get_page()
#     # print(page[:300])
#     # title = get_page_title(page)
#     # print(title)
#     links = get_links(page)
#     print(links)

import requests
from parsel import Selector

class HouseKG:
    URL = "https://www.house.kg/snyat"
    HEADERS={
        'User-Agent': 'Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:127.0) Gecko/20100101 Firefox/127.0',
        'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,*/*;q=0.8',
        'Accept-Language': 'en-US,en;q=0.5',
        'Accept-Encoding': 'gzip, deflate, br, zstd'
    }
    LINKXPATH='//p[@class="title"]/a/@href'
    base='https://www.house.kg'
    def parse_data(self):
        text= requests.get(url=self.URL,headers=self.HEADERS).text
        tree=Selector(text=text)
        links=tree.xpath(self.LINKXPATH).extract()
        linkss=[self.base+i for i in links]
        for i in linkss:
            print(i)
        return linkss

if __name__ == '__main__':
    scrapper = HouseKG()
    scrapper.parse_data()
