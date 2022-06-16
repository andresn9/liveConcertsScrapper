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


    def parse(self, response):
        for link in response.css('a.d-mosaic__c-btn::attr(href)'):

            yield response.follow(link.get(), callback=self.parse_info)


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
                    "eventName": name,
                    "location": location,
                    "date": date,
                    "time": time,
                    "price" : price

                }
                self.events_ids+=1
                events.append(event)



        return events

    def parse_info(self, response):


        yield {
            'id': "a" + str(self.artists_ids),
            'name': response.css('div.ent-head-center').css('h1::text').get(),
            'image': response.css('div.ent-head-left').css('img::attr(src)').get(),
            'events': self.get_events(response.css('ul.ent-results-list'),1)

        }

        self.artists_ids+=1












        pass