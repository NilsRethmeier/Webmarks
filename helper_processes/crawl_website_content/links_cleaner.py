### README
'''

GOAL OF THIS MODULE:

INPUT:

OUTPUT:

IMPORTANT NOTES:

TODOs DUMP (PLEASE ADD AS ISSUE, IF YOU CAN'T DO IT YOURSELF):

'''
####




import json
from pprint import pprint
import glob
import os
import normaliser


path_files = 'linkfiles/raw'


def import_json():

    for filename in glob.glob(os.path.join(path_files,'*.json')):

        try:
            json_file = open(filename, "r")
            data = json.load(json_file)
            #pprint(data)
            # TODO: log error

            # build filename for _cleaned output file
            filename_cleaned=filename.replace(".json","_cleaned.txt")
            filename_cleaned=filename_cleaned.replace(path_files,"")

            #build path for _cleaned files to store
            path_cleaned=os.path.abspath('linkfiles/')+"/cleaned"
            print (path_cleaned)


            # create list of cleaned urls
            cleaned_list=[]
            had_to_clean=0
            for item in data:
                if "?" in item['url'] or "/search/" in item['url'] or "/tag/" in item['url']:   #TODO: Improve: make a list to compare
                    had_to_clean+=1
                else:
                    cleaned_link=item['url'].replace("https://","http://")
                    cleaned_list.append(cleaned_link)


            print ("\n\nThis is the DOMAIN we are looking at: " + filename + "\n" )
            print ("this is how many query strings we removed: ", had_to_clean)
            print ("This is the original size: ", len(cleaned_list))

            # check if in output list are duplicates
            seen = set()
            uniq = []
            for x in cleaned_list:
                if x not in seen:
                    uniq.append(x)
                    seen.add(x)

            #create new duplicate free list of urls for further procesing
            cleaned_list=list(seen)
            print ("This is the duplication filtered size: ", len(cleaned_list))

            with open(path_cleaned+filename_cleaned,'w+') as file:
                for item in cleaned_list:
                    file.writelines(item+"\n")


        except Exception as e:
            print ("error!!!!!:", str(e))

            # TODO: log errors here

            pass

import_json()


#def import_csv():


#def links_filter(url):


###### STILL TO DO:
#
#  1. Log the error in links_cleaner_errorlog.txt with identifier filename (replace path and .json) and error message + timestamp
#  2. MOVE FILES THAT ARE ALREADY PROCESSED TO FOLDER /linkfiles/raw/processed
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