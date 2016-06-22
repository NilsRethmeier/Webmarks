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

import hypothesis_api_req, lateral_api_req


## Takes Url, gets lateral info and posts to hypothes.is' related articles group

def url_processor(uri,selection):

    group_id= "KG9bL1Bm"
    user= "acct:WorldBrain@hypothes.is"
    print ("THIS IS THE ARTICLE WHICH IS ANALYSED: "+str(uri))

    if selection=="":
        related_articles= lateral_api_req.post_lateral(uri)

    else:
        related_articles= lateral_api_req.post_lateral_selection(uri, selection)

    try:
        #print (related_articles[0])
        json_object=json.loads(related_articles[0])
        id_item=""
        existing_items= hypothesis_api_req.get_item_list_group(group_id, user, uri)


        if related_articles[1]!=200:
                body_related= "**Unfortunately we couldnd find related content**"
                response= hypothesis_api_req.post_hypothesis(group_id, user, body_related, uri, selection)

                return ("test")


        else:
            if len(existing_items[1])==0:
                body_related= "**You are pioneering the discovery of related content for this article.** \n\n **Displaying all related items might take a few seconds.**\n\n **Thanks for your patience**"
                response= hypothesis_api_req.post_hypothesis(group_id, user, body_related, uri, selection)
                json_object2=json.loads(response)
                id_item=json_object2["id"]
                print ("this is the id of the start-disclaimer: " + str(id_item))



            for element in json_object:

                #print (element)
                title= element["title"]
                url_related=element["url"]
                summary=element["summary"]
                image_related=element["image"]
                source_name=element["source_name"]

                if url_related in str(existing_items[0]):
                    print ("this url already is linked: "+str(url_related))
                    pass

                else:
                    body_related="#####[**"+title+"**]("+url_related+")\n\n*"+summary+"*\n\nvia: **"+source_name+"**"
                    #print "this is the related url before giving to post"+url_related
                    hypothesis_api_req.post_hypothesis(group_id, user, body_related, uri, selection)
                    print ("New related article has been added!\n "+str(url_related))

            if id_item !="":
                #print (id_item)
                hypothesis_api_req.delete_one_item(id_item)
    except Exception as e:
        print (e)
        pass


    return ("There is no domain requested!")

#url_processor("http://qz.com/704939/the-ar-15-is-the-gun-of-choice-for-mass-shootings-and-its-easier-to-buy-in-florida-than-a-pistol/")
