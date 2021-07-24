# -*- coding:utf-8 -*-

import scrapy
from pet_spider.items import PetSpiderItem


class CatSpider(scrapy.Spider):
    name = 'cat'
    allowed_domains = ['maomijiaoyi.com/']
    start_urls = ['http://www.maomijiaoyi.com/index.php?/pinzhongdaquan_5.html//']

    def parse(self, response):
        pinzhong_left = response.xpath('//div[@class="pinzhong_left"]')
        from pet_spider.model.models import session, CatInfo
        for cat_info in pinzhong_left:
            cat = cat_info.xpath('.//a[@target="_blank"]')
            price = cat.xpath('.//div[@class="pet_price"]')
            pet_prices = price.xpath('.//span/text()').extract()
            names = cat.xpath('.//div[@class="pet_name"]/text()').extract()
            imgs = cat.css("img::attr(src)").extract()
            iqs = cat.xpath('.//div[@class="IQ_ranking"]/text()').extract()
            hrefs = cat.css("a::attr(href)").extract()
            # 赋值
            for idx, name in enumerate(names):
                item = PetSpiderItem()
                try:
                    item['name'] = name.replace("\t", "").replace("\r\n", "").replace("\u3000", "") \
                        .replace(" ", "")
                    item['pet_price'] = pet_prices[idx]
                    item['img'] = "http://www.maomijiaoyi.com" + imgs[idx]
                    item['iq'] = iqs[idx].replace("\t", "").replace("\r\n", "")
                    item['url'] = hrefs[idx]

                    catInfo = CatInfo()
                    catInfo.name = item['name']
                    catInfo.pet_price = item['pet_price']
                    catInfo.img = item['img']
                    catInfo.iq = item['iq']
                    session.add(catInfo)

                except Exception as e:
                    print(e, item)
                    continue
                print(item)
                self.cat_info(item)
                yield item
        session.commit()
        session.close()

    def cat_info(self, item):
        yield scrapy.Request(item['url'], callback=self.parse_cat_detail)

    def parse_cat_detail(self, response):
        # 详情
        res_detail = []
        details = response.xpath('//div[@class="details"]')
        from pet_spider.model.models import session, CatInfo
        for detail in details:
            data = detail.xpath('.//div/div//text()')
            for element in data:
                r = element.extract().replace("\t", "").replace("\r\n", "").replace(" ", "")
                res_detail.append(r)

        # 属性
        res_attr = []
        attrs = response.xpath('//div[@class="shuxing"]')
        for attr in attrs:
            data = attr.xpath('.//div/div//text()')
            for element in data:
                r = element.extract().replace("\t", "").replace("\r\n", "").replace(" ", "")
                res_attr.append(r)

        # 生活方式
        res_liftstyle = []
        contents = response.xpath('//div[@class="property_list"]')
        for content in contents:
            data = content.xpath('.//div/p//text()').extract()
            # 移除不用的元素
            data.remove("\n")
            data.remove(" \n")
            data.remove("\n\t")


