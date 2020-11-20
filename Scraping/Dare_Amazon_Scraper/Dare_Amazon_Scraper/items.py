# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import scrapy


class DareAmazonScraperItem(scrapy.Item):
    a_title = scrapy.Field()
    b_price = scrapy.Field()
    c_rating = scrapy.Field()
    d_comment = scrapy.Field()
    e_product_description = scrapy.Field()
    featured_bullets = scrapy.Field()
    category_rank = scrapy.Field()
    subcat_rank = scrapy.Field()
    asin = scrapy.Field()
    c_rate_count = scrapy.Field()
    features = scrapy.Field()

