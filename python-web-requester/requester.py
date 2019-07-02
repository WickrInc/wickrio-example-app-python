# This file shows examples of how to send requests to all API endpoints
import requests
import json
URL = "http://localhost:4001/WickrIO/V1/Apps/CLIENT_API_KEY"
PARAMS = {'Accept': '*/*', 'Content-Type': 'application/json',
          'Authorization': 'Basic AUTH_KEY'}

# send 1-to-1 Message
data = {
    "message": "Welcome to Wickr! This message will self destruct eventually.",
    "users": [
        {"name": "exampleuser@gmail.com"}
    ]
}
sendMessage = requests.post(URL + "/Messages",
                            headers=PARAMS,
                            data=json.dumps(data))
print(sendMessage.content)


# AddRoom
data = {
    "room": {
        "title": "Security Group room for Sports in Bot Testing Network",
        "description": "Security Group room for Sports in Bot Testing Network",
        "ttl": "25536000",
        "bor": "0",
        "members": [
            {"name": "exampleuser@gmail.com"},
            {"name": "exampleuser02@gmail.com"}
        ],
        "masters": [
            {"name": "exampleuser@gmail.com"}
        ]
    }
}
AddRoom = requests.post(URL + "/Rooms",
                        headers=PARAMS,
                        data=json.dumps(data))
print("AddRoom:")
print(AddRoom.json())
json_data = json.loads(AddRoom.text)
print(json_data['vgroupid'])
room = json_data['vgroupid']
print(room)


# Send Room message
data = {
    "message": "Welcome to Wickr! This message will self destruct eventually.",
    "vgroupid": room
}
sendMessage = requests.post(URL + "/Messages",
                            headers=PARAMS,
                            data=json.dumps(data))
print(sendMessage.content)

# Get Statistics
getStatistics = requests.get(URL + "/Statistics",
                             headers=PARAMS)
print(getStatistics.json())


# Delete Statistics
deleteStatistics = requests.delete(URL + "/Statistics",
                                   headers=PARAMS)
print(deleteStatistics.content)


# Get Room
payload = {
    'vgroupid': room}
getRoom = requests.get(URL + "/Rooms/{0}".format(room),
                             headers=PARAMS)
print("getRoom:")
print(getRoom.json())

# Get Rooms
getRooms = requests.get(URL + "/Rooms",
                        headers=PARAMS)
print("getRooms:")
print(getRooms.json())


# Modify Room
data = {
        "title": "Modified room",
        "description": "Testing ModifyRoom command",
        "ttl": "25536000",
        "bor": "0"
}
modifyRoom = requests.post(URL + "/Rooms/{0}".format(room),
                           headers=PARAMS,
                           data=json.dumps(data))
print("modifyRoom:")
print(modifyRoom.content)

# Delete Room
deleteRoom = requests.delete(URL + "/Rooms/{0}".format(room),
                             headers=PARAMS)
print("deleteRoom:")
print(deleteRoom.content)


# Add GroupConvo
data = {
    "groupconvo": {
        "members": [
            {"name": "exampleuser@gmail.com"},
            {"name": "exampleuser02@gmail.com"}
        ]
    }
}
AddGroupConvo = requests.post(URL + "/GroupConvo",
                              headers=PARAMS,
                              data=json.dumps(data))
print("AddGroupConvo:")
print(AddGroupConvo.content)
response = json.loads(AddGroupConvo.text)
print(response['vgroupid'])
groupConvo = response['vgroupid']
print(groupConvo)

# Get GroupConvos(All)
getGroupConvos = requests.get(URL + "/GroupConvo",
                              headers=PARAMS)
print("getGroupConvos:")
print(getGroupConvos.json())


# Get GroupConvo(One)
getGroupConvo = requests.get(URL + "/GroupConvo/{0}".format(groupConvo),
                             headers=PARAMS)
print("getGroupConvo:")
print(getGroupConvo.json())


# Delete GroupConvo(One)
payload = groupConvo  # double check this
deleteGroupConvo = requests.delete(URL + "/GroupConvo/{0}".format(groupConvo),
                                   headers=PARAMS)
print("deleteGroupConvo:")
print(deleteGroupConvo.content)


# Get Message
getMessage = requests.get(URL + "/Messages",
                          headers=PARAMS)
print(getMessage.json())


# Set MsgRecvCallback
payload = {'callbackurl': 'http://localhost:8090/apps/callback'}
setMsgRecvCallback = requests.post(URL + "/MsgRecvCallback",
                                   headers=PARAMS,
                                   params=payload)
print(setMsgRecvCallback.content)


# Get MsgRecvCallback
getMsgRecvCallback = requests.get(URL + "/MsgRecvCallback",
                                  headers=PARAMS)
print(getMsgRecvCallback.content)


# Delete MsgRecvCallback
deleteMsgRecvCallback = requests.delete(URL + "/MsgRecvCallback",
                                        headers=PARAMS)
print(deleteMsgRecvCallback.content)
