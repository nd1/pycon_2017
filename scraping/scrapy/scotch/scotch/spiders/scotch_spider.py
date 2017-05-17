'''
Use scrapy to pull the name, sale price, and regular price for scotch on the Drink Up NY site
'''

import scrapy

class ScotchSpider(scrapy.Spider):
    name = "scotch"

    start_urls = [
            'https://www.drinkupny.com/single-malt-scotch-whisky-s/77.htm'
        ]

    def parse(self, response):
        i = 0
        while i < len(response.css('.v-product__title::text')):
            yield{'brand': response.css('.v-product__title::text')[i].extract().strip(),
            'our_price' : response.css('.product_productprice::text')[0].extract().split('$', 1)[1].strip(),
            'sale_price' : response.css('.product_saleprice::text')[0].extract().split('$', 1)[1].strip()}
            i += 1
