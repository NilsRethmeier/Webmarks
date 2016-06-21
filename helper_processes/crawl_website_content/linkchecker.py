### README
'''

GOAL OF THIS MODULE:

INPUT:

OUTPUT:

IMPORTANT NOTES:

TODOs DUMP (PLEASE ADD AS ISSUE, IF YOU CAN'T DO IT YOURSELF):

'''
####


import subprocess
import normaliser
from time import sleep
import os


def linkchecker_bot():

    list_domains=[]
    with open("domains_to_check.txt") as l:
        for line in l:
            try:
                list_domains.append(line)
            except:
                pass

    ## Set current domain to crawl
    current_domain=list_domains[0]
    current_domain=current_domain.replace("\n","")
    print ("\n\n\n\n\n\n\n\n\WE NOW START WITH A NEW DOMAIN: "+ current_domain + "\n\n ")


    ## read identifier for bash command file output from buffer file
    domain_identifierS=normaliser.build_identifier(current_domain)

    # remove current domain from list & update domains_to_check_notes file
    start_urls = domain_identifierS[0].replace("\n","")
    allowed_domains = domain_identifierS[1].replace("\n","")
    domain_identifier = domain_identifierS[2].replace("\n","")


    with open("pagecrawler/pagecrawler/spiders/broken_links_spider_{}_spider.py".format(domain_identifier),"w+") as file:
        file.write('''from scrapy.selector import HtmlXPathSelector
from scrapy.spiders import CrawlSpider, Rule
import scrapy.linkextractors as scrapy
from scrapy.item import Item, Field

class BrokenItem(Item):
    url = Field()
    referer = Field()
    status = Field()


class BrokenLinksSpider(CrawlSpider):
    name = "{}"
    allowed_domains = ["{}"]
    start_urls = ["{}"]
    handle_httpstatus_list = [200]

    deny=[".*\?.*", ".*.png", ".*.jpg",".*http:/www.*", ".*gs-proxy", "\&.*"]

    handle_httpstatus_list = [200]
    rules = (Rule(scrapy.LinkExtractor(deny=deny, unique=True), callback='parse_item', follow=True),)
    #print (rules)

    def parse_item(self, response):
        if response.status == 200:
            item = BrokenItem()
            item['url'] = response.url

            return item'''.format(domain_identifier,allowed_domains,start_urls))


    try:
        # run bash command with new output file named after the domain
        os.chdir("pagecrawler/pagecrawler/")
        print (os.getcwd())
        bashCommand = "scrapy crawl {} -o ../../linkfiles/raw/{}.json".format(domain_identifier,domain_identifier)
        print (bashCommand)
        process = subprocess.Popen(bashCommand.split(), stdout=subprocess.PIPE)
        output = process.communicate()[0]



    except Exception as e:
        print (e)
        # Add current domain to domains error if unsuccessful
        print ("ERRRRROOORRRR")
        pass

linkchecker_bot()



###### STILL TO DO:
#
# 1.  Write Error logs with linkchecker_errorlog.txt as filename ("id": domain_identifier,types": excuting bash command, writing bash config file) and error message + timestamp
# 2. Multithreading supervision via python module
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#