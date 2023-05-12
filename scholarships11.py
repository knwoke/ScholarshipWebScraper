import scrapy

class Scholarships11Spider(scrapy.Spider):
    name = 'scholarships11'
    allowed_domains = ['www.scholarships.com']
    start_urls = ['https://www.scholarships.com/financial-aid/college-scholarships/scholarship-directory/academic-major']

    def parse(self, response):
        for link in response.css('ul#ullist a::attr(href)'):
            baseurl = 'https://www.scholarships.com'
            yield response.follow(baseurl + link.get(), callback=self.parse_categories)
        
    def parse_categories(self, response): 
        scholarships = response.css('tr')
        for scholarship in scholarships:
            try:
                yield {
                    'scholarshipamount': scholarship.css('td.scholamt::text').get().strip(),
                    'url': scholarship.css('td.scholtitle a::attr(href)').get(),
                }
            except: 
                yield {
                    'scholarshipamount': 'missingscholarship',
                    'url': 'missingurl!'
                }
