# crawl_websites_content.py


## Goal of this package

This package aims to find all articles for a given domain and crawls their content.


## Input

TXT.file with **list of domains**

allowed formats:

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

via url_to_dict_newspaper.py:
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

 ## Process description

 1. A **list of domains** is given to **linkchecker.py**
 2. .json files with the output urls from *linkchecker.py* are given to **link_cleaner.py**
 3. .txt files with the output from  *link_cleaner.py* are given to **url_to_dict_newspaper**
 4. **Output** files are generated


## Files directory

#### 1. linkchecker.py
Processing the list of domains to start scrapy linkchecker crawl for every of them.

#### 2. links_cleaner.py 
Filtering out non-articles from list of urls

#### 3. url_to_dict_newspaper.py
Takes all urls, crawls them with *newspaper* and saves them to the path: */exampledomain_com/exampleurl_com_timestamp*
 
### normaliser.py
Converting domain-urls in project wide standard identifiers

## Package requirements
siehe requirements.txt


