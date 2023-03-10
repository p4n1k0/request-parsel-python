import requests
import parsel


def scrape(url: str) -> str:
    URL_BASE = "http://books.toscrape.com/catalogue/"
    response = requests.get(URL_BASE + "the-grand-design_405/index.html")
    selector = parsel.Selector(response.text)

    title = selector.css("h1::text").get()

    price = selector.css(".product_main > .price_color::text").re_first(
            r"\d*\.\d{2}"
            )
    description = selector.css("#product_description ~ p::text").get()
    cover = URL_BASE + selector.css("img::attr(src)").get()
    suffix = "...more"
    if description.endswith(suffix):
        description = description.removesuffix(suffix)

    result = [title, price, description, cover]
    format_result = ",".join(result)
    return format_result
