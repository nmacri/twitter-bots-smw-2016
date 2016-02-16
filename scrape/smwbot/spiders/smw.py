from scrapy.spiders import Spider
from scrapy.selector import Selector

from scrapy.http import Request, Response

from smwbot.items import Event

import json


class SmwSpider(Spider):
    name = "smw"
    # allowed_domains = ["http://socialmediaweek.org/"]
    start_urls = [
        "http://socialmediaweek.org/newyork/schedule/",
    ]

    def parse(self, response):
        """
        """
        sel = Selector(response)
        talks = sel.css('div[itemtype="http://schema.org/Event"]')

        requests = []
        for talk in talks:
            item = Event()

            item['name'] = talk.css('.title-event > a::text').extract_first()
            item['url'] = talk.css('a[itemprop="url"]::attr(href)').extract_first()
            
            request = Request(item['url'], callback=self.parse_detail_page)

            request.meta['item'] = item

            requests.append(request)

        return requests


    def parse_detail_page(self, response):

        item = response.meta['item']

        sel = Selector(response)
        paragraphs = sel.css('#details-content > p')
        description = ''
        for p in paragraphs:
            description = description + p.css('p::text').extract_first().strip()

        item['description'] = description

        print description

        f = open('output.ldjson','ab')
        f.write(json.dumps(item))
        f.close()
        return item
