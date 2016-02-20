from scrapy.item import Item, Field

class Event(Item):
	"""
	Loose subset of https://schema.org/Event
	"""
	name = Field()
	description = Field()
	url = Field()
	performer = Field()
	broadcastOfEvent = Field()
	startDate = Field()

	def __dict__(self):
		return {'name': self.name,
				'description': self.description,
				'url': self.url,
				'performer': performer,
				'startDate': startDate}
