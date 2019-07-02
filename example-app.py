from flask import Flask, request
import requests
import json
webInterfaceURL = "http://localhost:3000/WickrIO/V1/Apps/CLIENT_API_KEY"
PARAMS = {'Accept': '*/*', 'Content-Type': 'application/json',
          'Authorization': 'Basic AUTH_KEY'}
PORT_NUMBER = 8090

app = Flask(__name__)  # create the Flask app


def main():

    # Configure client to send incoming messages to this apps address
    payload = {'callbackurl': 'http://127.0.0.1:8090/callback'}
    setMsgRecvCallback = requests.post(webInterfaceURL + "/MsgRecvCallback",
                                       headers=PARAMS,
                                       params=payload)
    print(setMsgRecvCallback.content)
    print("HELLO")
    # Get MsgRecvCallback
    getMsgRecvCallback = requests.get(webInterfaceURL + "/MsgRecvCallback",
                                      headers=PARAMS)
    print(getMsgRecvCallback.content)


@app.route('/callback', methods=['POST'])
def register():
    # Parse incoming message and decide what to do with it
    print('New incoming Message:', request.get_json())
    command = "/help"
    sender = "exampleuser@gmail.com"
    print(sender)
    # Other possible properties to extract from incoming messages
    # argument = request.get_json()["argument"]
    # userEmail = request.get_json()["userEmail"]
    # vGroupID = request.get_json()["vgroupid"]
    # convoType = request.get_json()["convoType"]
    #
    # Start coding below and modify the listen function to your needs
    #
    if command == "/help":
        print("command == /help")
        reply = "What can I help you with?"
        # send 1-to-1 Message
        data = {
            "message": reply,
            "users": [
                {"name": sender}
            ]
        }
        sendMessage = requests.post(webInterfaceURL + "/Messages",
                                    headers=PARAMS,
                                    data=json.dumps(data))
        print(sendMessage.content)
    return "OK 200"


if __name__ == "__main__":
    main()
    app.run(debug=True, port=PORT_NUMBER)  # run app in debug mode on port 5000
print("WORLD")
