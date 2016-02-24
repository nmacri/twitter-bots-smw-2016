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
        """
        Parses structured data from talk detail pages on 
        http://socialmediaweek.org/newyork/events/.*
        and serializes it in line-denomenated json
        """
        item = response.meta['item']
        sel = Selector(response)

        # Talk Descriptions
        paragraphs = sel.css('#content')
        description = ''
        for p in paragraphs:
            p_text = p.css('p::text').extract_first().strip().encode('ascii', 'ignore')
            description = description + p_text

        item['description'] = description

        # Author Twitter Handles
        tw_buttons = sel.css('.side-speakers .button-twitter').xpath('@href').extract()
        tw_handles = [b.replace("http://twitter.com/","").replace("https://twitter.com/","")
                        for b in tw_buttons]
        tw_handles = list(set([h for h in tw_handles if h !='']))
        item['performer'] = tw_handles

        # Event Hashtag
        tw_hashtag = sel.css('a[href*="twitter.com/search?q="]::text').extract_first()
        item['broadcastOfEvent'] = tw_hashtag

        # Scheduled Time
        item['startDate'] = sel.css('time[itemprop="startDate"]').xpath('@content').extract_first()

        # Serialize Output
        json_item = json.dumps(dict(item))

        f = open('../data/smw/talks.ldjson','ab')
        f.write('\n')
        f.write(json_item)
        f.close()

        return item
