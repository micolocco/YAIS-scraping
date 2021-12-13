# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import scrapy
from scrapy.item import Field


class ReviewItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    
    politician = Field()
    
    statement = Field()
    statement_source_url = Field()
    statement_date = Field() 
    
    review_title = Field()
    review_date = Field()
    review_truthness = Field()

