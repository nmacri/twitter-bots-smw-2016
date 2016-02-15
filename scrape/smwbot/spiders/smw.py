from scrapy.spiders import Spider
from scrapy.selector import Selector

from scrapy.http import Request, Response

from smwbot.items import Event


class SmwSpider(Spider):
    name = "smw"
    allowed_domains = ["http://socialmediaweek.org/"]
    start_urls = [
        "http://socialmediaweek.org/newyork/schedule/",
    ]

    def parse(self, response):
        """
        """
        sel = Selector(response)
        talks = sel.css('div[itemtype="http://schema.org/Event"]')

        items = []
        for talk in talks:
            item = Event()

            item['name'] = talk.css('.title-event > a::text').extract_first()
            item['url'] = talk.css('a[itemprop="url"]::attr(href)').extract_first()
            
            item['description'] = Request(item['url'], self.parse_detail_page)

            items.append(item)

        return items

    def parse_detail_page(self, response):
        sel = Selector(response)

        paragraphs = sel.css('#details-content >')

        description = ''

        for p in paragraphs:
            description = description + p.css('::text').strip()

        return description
