from flask import Flask, request
from flask_restful import Resource, Api

app = Flask(__name__)
api = Api(app)

# default message
messages = {
    1:{'message':'Merry Christmas'},
}

class Messages(Resource):
    def get(self):
        return messages

    def post(self):
        data = request.json
        messageId = len(messages.keys()) + 1
        messages[messageId] = {'message':data['message']}
        return messages

api.add_resource(Messages, '/')

if __name__ == '__main__':
    app.run(debug=True)
