import scrapy

class QuotesSpider(scrapy.Spider):
    name = 'posts'
    allowed_domains = ['www.skmm.gov.my']
    start_urls = [
        'https://www.skmm.gov.my/en/legal/registers/register-of-apparatus-assignments-search?type=AARadio'
    ]

    def parse(self, response):
        #name = response.css('.legal-table.table-responsive-xl tr td ::text').extract()
        #callsign = response.css('.legal-table.table-responsive-xl tr td ::text').extract()
        #assignno = response.css('.legal-table.table-responsive-xl tr td ::text').extract()
        #expirydate = response.css('.legal-table.table-responsive-xl tr td ::text').extract()
        #post = response.css('.legal-table.table-responsive-xl tr td ::text')
        #for item in response.css('.legal-table.table-responsive-xl tr td ::text'):
        N=0
        for item in response.css('.legal-table.table-responsive-xl tr td ::text'):
            #extracted = [t.capitalize() for t in response.css(".legal-table.table-responsive-xl tr td ::text")[N].get()]
            #print(extracted)
            #N=N+1
            
            reponsetext = yield {
                'sequence' : response.css(".legal-table.table-responsive-xl tr td ::text")[N].extract(),
                'name' : response.css(".legal-table.table-responsive-xl tr td ::text")[N+1].extract(),
                'callsign' : response.css(".legal-table.table-responsive-xl tr td ::text")[N+2].extract(),
                'assignno' : response.css(".legal-table.table-responsive-xl tr td ::text")[N+3].extract(),
                'expirydate' : response.css(".legal-table.table-responsive-xl tr td ::text")[N+4].extract(),
                }   
            N+=5

            #next_page = response.xpath('//*[@id="p_lt_WebPartZone12_ZContent_pageplaceholder_p_lt_WebPartZone7_ZRegisterApparatusData_UniversalPager_pagerElem"]/nav/ul/li[3]/a/@href').get()
            ##if next_page is not None:
            #    next_page =  response.urljoin(next_page)
            #    yield scrapy.request(next_page, callback=self.parse)


            #print(reponsetext)
            #with open('posts.html', 'w') as f:
            #    f.write("'reponsetext'\n")