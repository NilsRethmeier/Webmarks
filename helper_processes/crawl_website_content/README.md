# crawl_websits_content.py


## Goal of this package

This package aims to find all articles for a given domain and crawls their content.


## Input

TXT.file with domains in format (1 domain per line) into **linkchecker.py**

1. https://www.example.com/
2. http://www.example.com/
3. http://www.example.com/appendix_and_stuff/and/further/path/
4. www.example.com/appendix_and_stuff/and/further/path/
5. www.example.com/
6. example.com
6. example.com/
7. example.com/appendix_and_stuff/and/further/path/


## Output

##### END

**comes from url_to_dict_newspaper.py:**
 1. a folder for every domain with path: "/crawl_websites_content/crawled_pages/example_com/"
 2. a .TXT file for every crawled url containing a DICT with the following values:
  - "uri"
  - "title"
  - "summary"
  - "authors"
  - "publish_date"
  - "body_text"
  - "keywords"
  - "tags"

 ##### IN BETWEEN

 via


 ##### LOGS




## Files directory


### linkchecker.py
#####Goal:
Processing the list of domains to start scrapy crawl for every of them.

##### Input:
crawl_websits_content/domains_to_check.txt

##### Output:
1. broken_link_spider_example_com_spider.py (reference file for scrapy instance)
2. new scrapy crawl instance
3. json file with every url found: key: {'url': 'http://www.example.com/appendix_and_stuff/and/further/path/'}

### links_cleaner.py
##### Goal:
Filtering out non-articles with requirements:
 - have query string
 - have '/category/' path
 - have '/tags/' path
 - have '/tag/' path
 - have '/search/' path

##### Input:
'*.json' file for every crawled domain in path: '/crawl_website_content/linkfiles/raw/'
##### Output:
'*_cleaned.txt' file for every crawled domain with the urls that are eligible to be crawled with newspaper.py in the path: '/crawl_website_content/linkfiles/cleaned/'

### normaliser.py
##### Goal:
Converting urls in project wide standard identifiers in the format:
1. domain full: 'http(s)://(www.)example.com/'
2. domain_allowed: '(subdomain.)example.com'
3. domain_identifier:(subdomain_)example_com
##### Input:
a '*.json' file for every crawled domain in path: '/crawl_website_content/linkfiles/raw/'
##### Output:
a '*_cleaned.txt' file for every crawled domain with the urls that are eligible to be crawled with newspaper.py


## Package requirements

siehe requirements.txt



## Important TODOs left

1. Write error.logs for every step
