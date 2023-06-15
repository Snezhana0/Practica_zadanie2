from scrapy.spiders import CrawlSpider, Rule
from scrapy.linkextractors import LinkExtractor

class CrawlingSpider(CrawlSpider):
    name = "practica"
    allowed_domains = ["iisraeldefense.co.il"]
    start_urls =["https://www.israeldefense.co.il/"]

    rules = (
        Rule(LinkExtractor(allow= "en/categories/cybertech")),
        Rule(LinkExtractor(allow="en/categories", deny="cybertech"), callback="parse_item")
    )

    def parse_item(self, response):
        yield {
            "title": response.css(".page_title title h1::text").get(),
            "date": response.css(".created_date::text").get(),
            "page_text": response.css(".rtejustify::text").get(),
            "author": response.css(".author_name::text").get()
        }