import paho.mqtt.publish as publish

for i in range(1, 10):
    publish.single("anith/test", "Hello", hostname = "test.mosquitto.org")
    publish.single("anith/topic", "World!", hostname = "test.mosquitto.org")
    print("Done")               
