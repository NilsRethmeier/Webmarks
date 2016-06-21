import requests
import json

#group_id= "KG9bL1Bm"
#user= "acct:WorldBrain@hypothes.is"
#uri = "https://www.theguardian.com/environment/climate-consensus-97-per-cent/2016/jan/25/record-hot-2015-gave-us-a-glimpse-at-the-future-of-global-warming"




### list all items in a GROUP_ID for a specific URI and posted by a USER

def get_item_list_group(group_id, user, uri):
    url = "https://hypothes.is/api/search?uri={}&user={}&group={}&limit=100".format(uri,user,group_id)
    headers = {
        "Authorization" : "Bearer 6879-9dd0c5143502fc1f238e0325238151c4",
        "Content-Type" : "application/json;charset=UTF-8"
        }
    data={}

    json_data=json.dumps(data)
    response = requests.get(url, data=json_data, headers=headers)
    response_text=response.text

    json_object=json.loads(response_text)
    text_list=[]
    id_list=[]

    for element in json_object["rows"]:
        text_relevant=element["text"]
        id_relevant=element["id"]

        text_list.append(text_relevant)
        id_list.append(id_relevant)

    #print text_list

    return text_list,id_list

#get_item_list_group(group_id,user, uri)




##### delete all items in a GROUP_ID for a URI by a spcific USER:

def delete_all_items_group_uri(group_id, user, uri):

    list_to_delete=get_item_list_group(group_id,user,uri)

    for item in list_to_delete[1]:
        # print item

        url = "https://hypothes.is/api/annotations/{}".format(item)
        headers = {
            "Authorization" : "Bearer 6879-9dd0c5143502fc1f238e0325238151c4",
            "Content-Type" : "application/json;charset=UTF-8"
            }
        data={}

        json_data=json.dumps(data)
        response = requests.delete(url, data=json_data, headers=headers)
        response_text=response.text

        # print response.status_code

        print ("this item has been deleted "+ item)

#delete_all_items_group_uri(group_id,user,uri)




#### DELETE ONE SPECIFIC ITEM WITH item_id IN HYPOTHES.IS

def delete_one_item(item_id):
    url = "https://hypothes.is/api/annotations/{}".format(item_id)
    headers = {
        "Authorization" : "Bearer 6879-9dd0c5143502fc1f238e0325238151c4",
        "Content-Type" : "application/json;charset=UTF-8"
        }
    data={}

    json_data=json.dumps(data)
    response = requests.delete(url, data=json_data, headers=headers)
    response_text=response.text
    print ("The opening Text has been deleted " + item_id)
    return response_text

    # print response.status_code






###### post in hypothesis GROUP_ID as USER on URI with TEXT

def post_hypothesis(group_id, user, text, uri,selection):

    url = "https://hypothes.is/api/annotations"
    headers = {
        "Authorization" : "Bearer 6879-9dd0c5143502fc1f238e0325238151c4",
        "Content-Type" : "application/json;charset=UTF-8"
        }

    data={
        "uri": uri,
        "user": user,
        "selector": {"exact": selection , "type": "TextQuoteSelector"},
        "permissions": {
            "read": ["group:"+group_id],
            "update": [user],
            "delete": [user],
            "admin": [user]
        },
        "group":group_id,
        "document": {},
        "target": [],
        "tags": [],
        "text": text
    }

    json_data=json.dumps(data)
    response = requests.post(url, data=json_data, headers=headers)
    response_text=response.text
    return response_text

#post_hypothesis(group_id, user, text, uri)




def hypothesis_search_id(id):
    url = "https://hypothes.is/api/search?id="+id
    headers = {
        "Authorization" : "Bearer 6879-9dd0c5143502fc1f238e0325238151c4",
        "Content-Type" : "application/json;charset=UTF-8"
        }
    data={}


    response = requests.get(url, headers=headers)
    response_text=response.text

    json_object=json.loads(response_text)

    print (json_object)

    text_list=[]
    id_list=[]

    for element in json_object["rows"]:
        text_relevant=element["text"]
        id_relevant=element["id"]

        text_list.append(text_relevant)
        id_list.append(id_relevant)

    #print text_list

    return text_list,id_list

hypothesis_search_id("qhAZOjWsEeawSQ_WZLsugA")

