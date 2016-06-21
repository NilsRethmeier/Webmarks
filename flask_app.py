from flask import Flask
from flask import request

from meta_browsing_types import relevant_lateral

app = Flask(__name__)


@app.route('/',methods=['GET'])
def hello_name():
    selection=request.args.get("selection")
    url= request.args.get("url")
    print selection

    print ("this is the selction: "+ selection)

    return relevant_lateral.url_processor(url, selection)
