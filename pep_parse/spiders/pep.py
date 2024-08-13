import re

import scrapy

from pep_parse.items import PepParseItem


class PepSpider(scrapy.Spider):
    name = 'pep'
    allowed_domains = ['peps.python.org']
    start_urls = ['https://peps.python.org/']

    def parse(self, response):
        all_peps = response.css('a[href^="pep-"]').xpath('@href').getall()
        filtered_peps_links = [
            href for href in all_peps if re.match(r'^pep-\d{4}/$', href)]
        for pep_link in filtered_peps_links:
            yield response.follow(pep_link, callback=self.parse_pep)

    def parse_pep(self, response):
        pep_number_name = ' '.join(
            response.css(
                'h1.page-title *::text').getall()).replace(
                    '  ', ' ').split(' – ')
        data = {
            'number': pep_number_name[0],
            'name': pep_number_name[1],
            'status': response.css(
                'dt:contains("Status") + dd abbr::text').get()
        }
        yield PepParseItem(data)
