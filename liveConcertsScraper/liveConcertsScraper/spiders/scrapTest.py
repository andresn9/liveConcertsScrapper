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

    artists_ids = 1
    events_ids = 1
    # Parses the website

    #response.css('div.d-mosaic__box').css('div.d-mosaic__box').attrib['data-link']

    #response.follow(response.css('div.d-mosaic__box').css('div.d-mosaic__box').attrib['data-link'].get())

    def parse(self, response):
        for link in response.css('a.d-mosaic__c-btn::attr(href)'):

            yield response.follow(link.get(), callback=self.parse_categories)


    def get_events(self, response,n):

        events =[]


        for x in range(0,len(response)):
            name = response[x].css("h2.l-title-entity::text").get()
            location= response[x].css("div.l-subtitle-entity").css("a::text").get()
            date = response[x].css("li").css("meta[itemprop=startDate]::attr(content)").get()
            time = response[x].css("div.ent-results-list-hour-time").css("span::text").get()
            price = response[x].css("div.ent-results-list-hour-price").css("span::text").get()

            if(name is not None and location is not None and date is not None and time is not None):
                event = {
                    "id" : "c" + str(self.events_ids),
                    "name": name,
                    "location": location,
                    "date": date,
                    "time": time,
                    "price" : price

                }
                self.events_ids+=1
                events.append(event)



        return events

    def parse_categories(self, response):



        # respuesta.css("li").css("meta[itemprop=name]")
        # name =""
        # location=""
        # date=""
        # time=""
        #
        # concerts=""
        #
        # respuesta = response.css('ul.ent-results-list')
        #
        #
        # for event in respuesta:
        #     name = respuesta.css("h2.l-title-entity::text").get()
        #     location= respuesta.css("div.l-subtitle-entity").css("a::text").get()
        #     date = respuesta.css("li").css("meta[itemprop=startDate]::attr(content)").get()
        #     time = respuesta.css("div.ent-results-list-hour-time").css("span::text").get()



            # respuesta.css("li").css("meta[itemprop=startDate]::attr(content)").get()
            # respuesta.css("div.l-subtitle-entity").css("a::text").get()



        yield {
            'id': "a" + str(self.artists_ids),
            'name': response.css('div.ent-head-center').css('h1::text').get(),
            'image': response.css('div.ent-head-left').css('img::attr(src)').get(),
            'events': self.get_events(response.css('ul.ent-results-list'),1)

        }

        self.artists_ids+=1










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