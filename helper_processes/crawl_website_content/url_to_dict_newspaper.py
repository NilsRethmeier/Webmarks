### README
'''

GOAL OF THIS MODULE:

INPUT:

OUTPUT:

IMPORTANT NOTES:

TODOs DUMP (PLEASE ADD AS ISSUE, IF YOU CAN'T DO IT YOURSELF):

'''
####




import glob
import os
import time

import normaliser

from helper_processes import newspaper_extract

path_files="linkfiles/cleaned/"

def url_to_dict(path_files):

    for filename in glob.glob(os.path.join(path_files,'*.txt')):

        try:

            # opens every file and creates a list of urls to process via newspaper
            print ("This is the file we are processing: "+ filename)
            with open(filename,"r") as linkfile:
                list_urls=linkfile.readlines()

            #print (list_urls)

            for url in list_urls:
                url=url.replace("\n","")
                timestr = time.strftime("%Y%m%d-%H%M%S")
                print (timestr)
                #print (url)
                try:
                    filenames_normalised=normaliser.build_identifier(url)
                    # creating dictionary that will be saved in output .txt file
                    dict={}
                    # send url into newspaper: TODO: errorhandling and log
                    content= newspaper_extract.get_text(url)
                    dict['uri']=url
                    dict["title"]=content[0]
                    dict["summary"]=content[0]
                    dict["authors"]=content[2]
                    dict["publish_date"]=content[3]
                    dict["body_text"]=content[4]
                    dict["keywords"]=content[5]
                    dict["tags"]=content[6]


                    #print (dict)

                    # if less than 100 characters in body_text try next url # TODO: log all urls that are "non-Articles" as no_articles.txt
                    if len(content[4])<=100:
                        print ("Non-Article Detected: "+url)
                        print (content[4])
                        continue

                    foldername_domain=filenames_normalised[2]
                    filename_url=filenames_normalised[2]+"_"+timestr


                    if not os.path.exists("crawled_pages/"+foldername_domain):
                        os.makedirs("crawled_pages/"+foldername_domain)

                    with open('crawled_pages/{}/{}.txt'.format(foldername_domain,filename_url),"w+") as file:
                        file.write(str(dict))

                    #print ("File successfully created: " + filename_url)

                except Exception as e:  #TODO: errorlog filetype url
                    print ("There was an ERRRRORR with the URL: "+ url + "\n")
                    print (e)
                    pass

        except Exception as e: #TODO: errorlog: filetype filename
            print ("There was an ERRRRORR with the FILE: "+ filename + "\n")
            print (e)
            pass






url_to_dict(path_files)


##### TODOS:

# TODO: try first 10 links with 2 different crawlers; compare body lenghts; continue crawling with crawler, that spits out more content
# TODO: Seperate opening of files in folder from processing the individual files
# TODO: remove processed url from original file