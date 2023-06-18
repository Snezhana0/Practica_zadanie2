import logging
from distutils.log import Log

from scrapy.spiders import CrawlSpider, Rule
from scrapy.linkextractors import LinkExtractor

class CrawlingSpider(CrawlSpider):
    name = "practica"
    allowed_domains = ["i-hls.com"]
    start_urls =["https://i-hls.com/"]

    rules = (
        Rule(LinkExtractor(allow= "iHLS/news")),
        Rule(LinkExtractor(allow="iHLS", deny="news"), callback="parse_item")
    )

    def parse_item(self, response):
        logging.info("работа парсера")

        yield {
            "title": response.css(".entry-title a::text").get(),
            "date": response.css(".meta-info time::text").get(),
            "page_text": response.css(".td-post-text-excerpt::text").get()
        }