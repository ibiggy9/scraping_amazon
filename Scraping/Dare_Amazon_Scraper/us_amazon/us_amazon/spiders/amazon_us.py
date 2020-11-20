import scrapy
from us_amazon.items import UsAmazonItem
from .get_asins import american
import os

class AmazonCaSpider(scrapy.Spider):
    name = 'us_amazon'
    allowed_domains = ['amazon.com']
    ca = american()
    start_urls = []
    for i in ca:
        start_urls.append(i)
    

    def parse(self, response):
        items = UsAmazonItem()
        titles = response.css("#productTitle").extract()
        prices = response.css('#priceblock_ourprice').extract()
        ratings = response.css('#reviewsMedley .a-size-medium').css('::text').extract()
        comments = response.css('#cm-cr-dp-review-list .a-expander-partial-collapse-content span , #customer_review-RXHBHKB1HHFJH .a-expander-partial-collapse-content , #customer_review-R36WND8H8B1CKP .a-expander-partial-collapse-content , #customer_review-R38W6KYEQ4A9D4 .a-expander-partial-collapse-content').css('::text').extract()
        product_descriptions = response.xpath('//*[(@id = "productDescription")]//p').extract()
        featured_bullets = response.css('#feature-bullets .a-list-item').css('::text').extract()
        rank_in_category = response.css('#detailBullets_feature_div+ .detail-bullet-list > li .a-list-item').css('::text').extract()
        asin = response.css('li:nth-child(4) .a-text-bold+ span').css('::text').extract()
        rate_count = response.css('.averageStarRatingNumerical .a-color-secondary').css('::text').extract()
        subcat = response.css('.zg_hrsr .a-list-item').css('::text').extract()
        
        items['a_title'] = titles
        items['b_price'] = prices
        items ['c_rate_count'] = rate_count
        items['c_rating'] = ratings
        items['d_comment'] = comments
        items['e_product_description'] = product_descriptions
        items['featured_bullets'] = featured_bullets
        items['category_rank'] = rank_in_category
        items['asin'] = asin
        items['subcat_rank'] = subcat
     

        os.system('python3.9 /Users/user9231/desktop/code/scraping/dare_amazon_scraper/cleaning.py')
        yield items
    