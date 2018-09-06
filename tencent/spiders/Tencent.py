# -*- coding: utf-8 -*-
import scrapy
from scrapy.linkextractors import LinkExtractor
from scrapy.spiders import CrawlSpider, Rule
from tencent.items import TencentItem


class TencentSpider(CrawlSpider):
    name = 'Tencent'
    allowed_domains = ['hr.tencent.com']
    start_urls = ['https://hr.tencent.com/position.php?&start=0#a']


    rules = (
        Rule(LinkExtractor(allow=r'start=\d+'), callback='parse_item', follow=True),
    )

    def parse_item(self, response):
        print response.url
        
        for i in response.xpath("//tr[@class='even'] | //tr[@class='odd']"):
            item = TencentItem()
            item['name'] = i.xpath("./td[1]/a/text()").extract()[0]
            # 详情连接
            item['link'] = i.xpath("./td[1]/a/@href").extract()[0]
            # 职位类别
            item['lx'] = i.xpath("./td[2]/text()").extract()[0]
            # 招聘人数
            item['num'] =  i.xpath("./td[3]/text()").extract()[0]
            # 工作地点
            item['addr'] = i.xpath("./td[4]/text()").extract()[0]
            # 发布时间
            item['time'] = i.xpath("./td[5]/text()").extract()[0]
            yield item
        
