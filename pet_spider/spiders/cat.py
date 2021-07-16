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
            # 赋值
            for idx, name in enumerate(names):
                item = PetSpiderItem()
                try:
                    item['name'] = name.replace("\t", "").replace("\r\n", "").replace("\u3000", "") \
                        .replace(" ", "")
                    item['pet_price'] = pet_prices[idx]
                    item['img'] = "http://www.maomijiaoyi.com" + imgs[idx]
                    item['iq'] = iqs[idx].replace("\t", "").replace("\r\n", "")

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
                yield item
        session.commit()
        session.close()
