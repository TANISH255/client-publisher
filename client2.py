import paho.mqtt.client as mqtt
import time


##########Defining all call back functions###################

def on_connect(client,userdata,flags,rc):# called when the broker responds to our connection request
    print("Connected - rc:",rc)
def on_message(client,userdata,message):#Called when a message has been received on a topic that the client has subscirbed to.
    global FLAG
    global chat
    if str(message.topic) != pubtop:
        msg = str(message.payload.decode("utf-8"))
        print(str(message.topic),msg)
        if msg == "Stop" or msg == "stop":
            FLAG = False
        else:
            chat = input("Enter Message: ")
            client.publish(pubtop,chat)
def on_subscribe(client, userdata,mid,granted_qos):##Called when the broker responds to a subscribe request.
    print("Subscribed:", str(mid),str(granted_qos))
def on_unsubscirbe(client,userdata,mid):# Called when broker responds to an unsubscribe request.
    print("Unsubscribed:",str(mid))
def on_disconnect(client,userdata,rc):#called when the client disconnects from the broker
    if rc !=0:
        print("Unexpected Disconnection")


broker_address = "mqtt.eclipseprojects.io"
port = 1883

client = mqtt.Client()
client.on_subscribe = on_subscribe
client.on_unsubscribe = on_unsubscirbe
client.on_connect = on_connect
client.on_message = on_message
client.connect(broker_address,port)

time.sleep(1)

pubtop = "/chat/client2"
subtop = "/chat/client1"
FLAG = True
chat = None

client.loop_start()
client.subscribe(subtop)
while True:
    if FLAG == False or chat == "Stop" or chat == "stop":
        break

client.disconnect()
client.loop_stop()