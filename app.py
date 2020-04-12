from flask import Flask, request
from flask import render_template
import json
from backend import results2

app = Flask(__name__)

@app.route('/')
def hello_world():
    iso2 = request.args.get('iso2')
    if iso2 is None:
        postapi = results2
    elif iso2 not in results2:
        postapi = ("Country code does not exist")
    else:
        postapi = results2.get(iso2)
    return (json.dumps(postapi))

@app.route('/api', methods=['GET','POST'])
def my_api():
    if request.method == 'POST':
        test = request.form.get('name')
        return render_template('tab.html', iso2=results2.get(test))
    else:
        return render_template('tab.html')
if __name__ == '__main__':
    app.run(debug=True)



