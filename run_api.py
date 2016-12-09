#coding: utf-8

from flask import Flask, request
from flask_restful import Resource, Api
from flask_cors import CORS
from operat_json import operate

app = Flask(__name__)
api = Api(app)
CORS(app, send_wildcard=True)

class ServiceApi(Resource):
    def get(self):
        return {'hello': 'world'}

    def post(self):
        print request.headers
        print request.form
        get_json = request.form.to_dict()
        operate(get_json)
        return 'success', 201

api.add_resource(ServiceApi, '/iptables')

if __name__ == '__main__':
    app.debug=True
    app.run(host='192.168.0.104')





