======
SMW Bot
======

This is a Scrapy project to scrape talk descriptions from the social media week public web directories.

Items
=====

The items scraped by this project are talks, and the item is defined in the
class::

    smwbot.items.Talk

See the source code for more details.

Spiders
=======

This project contains one spider called ``smw`` that you can see by running::

    scrapy list

Spider: smw
------------

The ``smw`` spider scrapes the talk descriptions from the social media week public web directories (http://socialmediaweek.org/newyork/schedule/), and it's
based on the dmoz spider described in the `Scrapy tutorial`_

This spider doesn't crawl the entire socialmediaweek.org site but only a few pages by default (defined in the ``start_urls`` attribute). These pages are:

* http://socialmediaweek.org/newyork/schedule/

So, if you run the spider regularly (with ``scrapy crawl smw``) it will scrape
only that page.

.. _Scrapy tutorial: http://doc.scrapy.org/en/latest/intro/tutorial.html

