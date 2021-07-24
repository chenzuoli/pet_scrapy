# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import scrapy


class PetSpiderItem(scrapy.Item):
    # define the fields for your item here like:
    name_zh = scrapy.Field()
    name_en = scrapy.Field()
    recommemd_price = scrapy.Field()
    real_name = scrapy.Field()
    alias = scrapy.Field()
    ancester = scrapy.Field()
    area = scrapy.Field()
    original = scrapy.Field()
    size = scrapy.Field()
    original_usage = scrapy.Field()
    today_usage = scrapy.Field()
    group = scrapy.Field()
    height = scrapy.Field()
    weight = scrapy.Field()
    age = scrapy.Field()
    avatar_url = scrapy.Field()
    pet_price = scrapy.Field()
    img = scrapy.Field()
    name = scrapy.Field()
    iq = scrapy.Field()
    url = scrapy.Field()
