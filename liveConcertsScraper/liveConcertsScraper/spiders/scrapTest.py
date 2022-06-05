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

    #response.css('div.d-mosaic__box').css('div.d-mosaic__box').attrib['data-link']

    #response.follow(response.css('div.d-mosaic__box').css('div.d-mosaic__box').attrib['data-link'].get())

    def parse(self, response):
        for link in response.css('a.d-mosaic__c-btn::attr(href)'):

            yield response.follow(link.get(), callback=self.parse_categories)




    def parse_categories(self, response):

        yield {
            'name': response.css('div.ent-head-center').css('h1::text').get()
,
        }


        # for x in response.css('div.d-mosaic__box'):
        #     try:
        #         final_link= x.css('div.d-mosaic__box').attrib['data-link']
        #         final_link = "https://www.taquilla.com" + final_link.replace("'", "")
        #
        #         info_page = final_link
        #
        #
        #
        #         yield {
        #                     'name' : x.css('h3.d-mosaic__title::text').get(),
        #                      'link': final_link ,
        #                  }
        #
        #
        #
        #
        #     except:
        #         yield {
        #                     'name': x.css('h3.d-mosaic__title::text').get(),
        #                     'link': "",
        #                 }
        #
        #
        #
        #






        # for x in response.css('div.d-mosaic__box'):
        #
        #     try:
        #         yield {
        #             'name' : x.css('h3.d-mosaic__title::text').get(),
        #             'link': x.css('div.d-mosaic__box').attrib['data-link'] ,
        #         }
        #     except:
        #         yield {
        #             'name': x.css('h3.d-mosaic__title::text').get(),
        #             'link': "",
        #         }
        #
        # next_page=










        #
        # # fetch('https://www.taquilla.com/conciertos/pop-rock?t10type=2&t10subtype=2&t10start=0&t10num=2000&')
        # links = response.css('div.d-mosaic__box').getall()
        #
        # for link in links:
        #     final_link = response.css('div.d-mosaic__box').attrib['data-link']
        #     final_link = "https://www.taquilla.com" + final_link.replace("'","")
        #     print(final_link)
        #





        pass