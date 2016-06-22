### README
'''

GOAL OF THIS MODULE:

INPUT:

OUTPUT:

IMPORTANT NOTES:

TODOs DUMP (PLEASE ADD AS ISSUE, IF YOU CAN'T DO IT YOURSELF):

'''
####




from flask import Flask
from flask import request

import relevant_lateral

app = Flask(__name__)


@app.route('/')
def hello_name():
    selection=request.args.get("selection")
    url= request.args.get("url")
    trusted=request.args.get("trusted")
    #print selection
    print (trusted)
    if trusted:
        with open("trusted_domains.txt","a+") as file:
            file.writelines(trusted+"\n")

    #print ("this is the selction: "+ selection)

    return relevant_lateral.url_processor(url, selection)
