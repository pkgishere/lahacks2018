import paho.mqtt.publish as publish


def command(str):
	return publish.single("anith/test",str,hostname="test.mosquitto.org")



def move(direction,value):
	payload = {
		"function":"move",
		"params":
			{
			"direction":direction,
			"value":value
			}
	}
	return command(str(payload))

def rotate(direction,value):
	payload = {
		"function":"rotate",
		"params":
			{
			"direction":direction,
			"value":value
			}
	}
	return command(str(payload))

def setLED(value):
	payload = {
		"function":"setLED",
		"params":
			{
			"value":value
			}
	}
	return command(str(payload))

