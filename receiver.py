from __future__ import print_function
from flask import Flask, request, redirect, jsonify
import xmltodict
import json
import cdrs
from models import Record

app = Flask(__name__)

@app.route('/')
def index():
    return redirect('/admin/')

@app.route('/cdr', methods=['POST'])
def post():
    try:
        cdr = xmltodict.parse(request.data)

        if isinstance(cdr['records']['record'], list):
            for record in cdr['records']['record']:
                instance = getattr(cdrs, str(record['@type']))(record)
                Record.create(data=json.dumps(instance.__dict__))
        else:
            instance = getattr(cdrs, str(cdr['records']['record']['@type']))(cdr['records']['record'])
            Record.create(data=json.dumps(instance.__dict__))
        return('', 204)
    except:
        print('Parser failure!')
        return('', 204)

@app.route('/api/v1/records/', methods=['GET'])
@app.route('/api/v1/records/<int:page>', methods=['GET'])
def records_endpoint(page=1):
    per_page = 20
    query = Record.select().paginate(page, per_page).order_by(Record.created_date.desc())
    data = [json.loads(i.serialize) for i in query]

    if data:
        response = jsonify({'records': data})
        response.status_code = 200
    else:
        output = {
            'records': 0
        }
        response = jsonify(output)
        response.status_code = 200
    return response

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8444)
