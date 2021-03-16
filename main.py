from flask import Flask, jsonify, request
from flask_restful import Resource, Api, reqparse
from flask_cors import CORS, cross_origin
from IconsTrainingModel import IconTrainingModel

API_URL_PREFIX = '/cv/v2/'
app = Flask(__name__)
CORS(app)

parser = reqparse.RequestParser()
model = IconTrainingModel()

def trainIconModel(payload):
    return model.help()

@app.route(API_URL_PREFIX + 'learn/icon', methods=['GET'])
def learnIcon():
    print('This API will learn to identify icons')
    try:
        parser.add_argument('imageBase64String', type=str)
        parser.add_argument('imageBase64', type=str) #boolean 1 or 0
        parser.add_argument('imagePath', type=str) # For local testing
        payload = parser.parse_args()
        response =trainIconModel(payload)
        return response
    except:
        return {
            'status': False,
            'message': 'Unexpected error occurred'
        }



@app.route(API_URL_PREFIX + 'find/icon', methods=['GET'])
def findIcon():
    print('This API will recognize a given icon image')


if __name__ == '__main__':
    
    threaded, debug, port = False, False, 9083

    print('Starting API Server with following options - ')
    print('PORT : ', port)
    print('THREADED : ', threaded)
    print('debug : ', debug)

    app.run(debug=debug, port=port, threaded=debug)

