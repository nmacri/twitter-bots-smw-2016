from scrapy.item import Item, Field

class Event(Item):
	"""
	Subset of https://schema.org/Event
	"""
	name = Field()
	description = Field()
	url = Field()
