from scrapy.item import Item, Field

class PropertiesItem(Item):
    title = Field()
    price = Field()
    available = Field()
    description = Field()
    image = Field()
    breadcrumbs = Field()
    url = Field()
    website = Field()
    address = Field()
    loc = Field()
    project = Field()
    spider = Field()
    server = Field()
    date = Field()