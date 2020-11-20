import scrapy
from Dare_Amazon_Scraper.items import DareAmazonScraperItem
from .get_asins import canadian 
import os
class AmazonCaSpider(scrapy.Spider):
    name = 'Amazon_CA'
    allowed_domains = ['amazon.ca']
    ca = canadian()
    start_urls = []
    for i in ca:
        start_urls.append(i)
    

    def parse(self, response):
        items = DareAmazonScraperItem()
        titles = response.css("#productTitle").extract()
        prices = response.css('#priceblock_ourprice').extract()
        ratings = response.css('#reviewsMedley .a-size-medium').css('::text').extract()
        comments = response.css('.a-expander-partial-collapse-content span').css('::text').extract()
        product_descriptions = response.xpath('//*[(@id = "productDescription")]//p').extract()
        featured_bullets = response.css('#feature-bullets .a-list-item').css('::text').extract()
        rank_in_category = response.css('#productDetails_detailBullets_sections1 tr~ tr+ tr span:nth-child(1)').css('::text').extract()
        asin = response.css('#productDetails_detailBullets_sections1 tr:nth-child(1) td').extract()
        rate_count = response.css('.averageStarRatingNumerical .a-color-secondary').css('::text').extract()
        subcat = response.css('#productDetails_detailBullets_sections1 br+ span').css('::text').extract()
        

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
    