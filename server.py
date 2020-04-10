from flask import Flask, request
import json
from app import resultsJson
from app import results2

# postapi = results2.get('ZWE')

test = resultsJson

app = Flask(__name__)

@app.route('/')
def hello_world():
    iso2 = request.args['iso2']
    # iso2 = request.args.get('iso2','GBR')
    postapi = results2.get(iso2)
    return((json.dumps(postapi)))

@app.route('/api')
def my_api():
    return 'my API'

if __name__ == '__main__':
    app.run(debug=True)




