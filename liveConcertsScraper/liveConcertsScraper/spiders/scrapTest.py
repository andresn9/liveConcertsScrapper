# Import library
import scrapy
# Create Spider class
class scrapTest(scrapy.Spider):
    # Name of spider
    name = 'scrapTest'
    # Website you want to scrape
    start_urls = [
        'https://www.taquilla.com/conciertos/pop-rock?t10type=2&t10subtype=2&t10start=0&t10num=2000&'
    ]
    # Parses the website
    def parse(self, response):



        pass