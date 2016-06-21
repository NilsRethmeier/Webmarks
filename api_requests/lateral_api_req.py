### README
'''

GOAL OF THIS MODULE:

INPUT:

OUTPUT:

IMPORTANT NOTES:

TODOs DUMP (PLEASE ADD AS ISSUE, IF YOU CAN'T DO IT YOURSELF):

'''
####





import requests

from helper_processes import newspaper_extract


def strip_non_ascii(string):
    ''' Returns the string without non ASCII characters'''
    stripped = (c for c in string if 0 < ord(c) < 127)
    return ''.join(stripped)


def post_lateral(uri):

    print ("WE DID IT WITHOUT A SELECTION!")
    url = "https://news-api.lateral.io/documents/similar-to-text"

    text_body= newspaper_extract.get_text(uri)

    text_body=text_body[0]+' '+text_body[1]+' '+text_body[4]+' '+text_body[5]

    text_body=text_body.replace("'","")
    text_body=text_body.replace("\n","")
    text_body=text_body.replace(".","")
    text_body=text_body.replace('"','')
    text_body=text_body.encode('ascii')


    payload = '{\"text\":\"%s\"}' %(text_body)
    #print payload

    headers = {
        'subscription-key': "300013d473bd6aeff226c4b9c134990a",
        'content-type': "application/json"
        }
    response = requests.post(url, data=payload, headers=headers)


    response_text=response.text
    response_code=response.status_code

    print (response_code)

    return response_text,response_code

#post_lateral("http://qz.com/704939/the-ar-15-is-the-gun-of-choice-for-mass-shootings-and-its-easier-to-buy-in-florida-than-a-pistol/")



#### search lateral with selection

def post_lateral_selection(uri,selection):

    print ("WE DID IT WITH A SELECTION!")

    url = "https://news-api.lateral.io/documents/similar-to-text"

    selection=strip_non_ascii(selection)
    selection=selection.replace("'"," ")
    selection=selection.replace("\n"," ")
    selection=selection.replace("."," ")
    selection=selection.replace('"',' ')
    selection=selection.encode('ascii')

    payload = '{\"text\":\"%s\"}' %(selection)
    #print payload

    headers = {
        'subscription-key': "300013d473bd6aeff226c4b9c134990a",
        'content-type': "application/json"
        }
    response = requests.post(url, data=payload, headers=headers)

    response_text=response.text
    response_code=response.status_code

    print (response_code)

    return response_text,response_code
