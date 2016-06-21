from scrapy.selector import HtmlXPathSelector
from scrapy.spiders import CrawlSpider, Rule
import scrapy.linkextractors as scrapy
from scrapy.item import Item, Field

class BrokenItem(Item):
    url = Field()
    referer = Field()
    status = Field()


class BrokenLinksSpider(CrawlSpider):
    name = "jacobinmag_com"
    allowed_domains = ["jacobinmag.com"]
    start_urls = ["http://jacobinmag.com/"]
    handle_httpstatus_list = [200]

    deny=[".*\?.*", ".*.png", ".*.jpg",".*http:/www.*", ".*gs-proxy", "\&.*"]

    handle_httpstatus_list = [200]
    rules = (Rule(scrapy.LinkExtractor(deny=deny, unique=True), callback='parse_item', follow=True),)
    #print (rules)

    def parse_item(self, response):
        if response.status == 200:
            item = BrokenItem()
            item['url'] = response.url

            return item