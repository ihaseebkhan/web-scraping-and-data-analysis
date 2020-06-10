import scrapy
from ..items import ImdbItem
from scrapy.crawler import CrawlerProcess

class ImdbSpider(scrapy.Spider):
	name = 'imdbspider'
	allowed_domains = ['imdb.com']
	start_urls = ['https://www.imdb.com/chart/top?ref_=nv_mv_250']

	custom_settings = {'DOWNLOAD_DELAY':0.25,'FEED_FORMAT':'csv','FEED_URI':'IMDB.csv'}

	def parse(self,response):
		for href in response.css("td.titleColumn a::attr(href)").getall():
			yield response.follow(url=href,callback=self.parse_movie)

	def parse_movie(self, response):
		item = ImdbItem()
		item['title'] = [ x.replace('\xa0', '')  for x in response.css(".title_wrapper h1::text").getall()][0]
		item['total_number_of_ratings'] = [ x.replace(',', '')  for x in response.css(".imdbRating > a > span::text").getall()][0]
		item['rating_score'] = response.css(".ratingValue span::text").get()
		genre_list = response.xpath('//*[@id="title-overview-widget"]/div[1]/div[2]/div/div[2]/div[2]/div/a[contains(@href, "/search/")]/text()').getall()
		item['genre'] = '-'.join(genre_list)
		try:
			item['budget'] = [ x.replace('\n', '').replace(',', '')  for x in response.xpath('//div[contains(h4, "Budget")]/text()').getall()][1].strip()
		except:
			item['budget'] = "Not Available on IMDB"
		try:
			item['gross_USA'] = [ x.replace(',', '')  for x in response.xpath('//div[contains(h4, "Gross USA:")]/text()').getall()][1].strip("$ ")
		except:
			item['gross_USA'] = ''
		return item

# Code to make script run like normal Python script 
process = CrawlerProcess()
process.crawl(ImdbSpider)
process.start()