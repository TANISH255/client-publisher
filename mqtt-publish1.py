import paho.mqtt.client as mqtt
from random import randrange, uniform
import time

#connect with broker and create client
mqttBroker = "mqtt.eclipseprojects.io"
client =mqtt.Client("Temperature_Inside")
client.connect(mqttBroker)

while True:
    randNumber = uniform(20.1,21.0)
    client.publish("Temperature",randNumber)
    print("Just published"+str(randNumber)+"to topic Temperature")
    time.sleep(1)



