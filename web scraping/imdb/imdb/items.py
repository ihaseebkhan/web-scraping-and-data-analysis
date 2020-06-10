#items.py file
import scrapy

class ImdbItem(scrapy.Item):
    title = scrapy.Field()
    total_number_of_ratings = scrapy.Field()
    rating_score = scrapy.Field()
    genre = scrapy.Field()
    budget = scrapy.Field()
    gross_USA = scrapy.Field()