import paho.mqtt.publish as publish

def control_device(device,state):
    publish.single(f"home/{device}",state,hostname="broker.hivemq.com")
