import time
import ttn


app_id = "wisnodearduino1"
access_key = "ttn-account-v2.QAT09KX6NTZPal64F1iwMQvTB5kHgQj__nP0etRhSek"
dev_id = "wisnode1"
estado = True

def uplink_callback(msg,client):
    print("Uplink recibido de: ",msg.dev_id)
    
    global estado
    if msg.dev_id == "boton4200" :
        print(msg)    
        if estado:
            payload ="Qg=="
            estado = False
        else:
            payload ="Qw=="
            estado = True
            #payload = "Qw=="
        client.send(dev_id, payload, port=1, conf=False, sched="replace")

   



handler = ttn.HandlerClient(app_id,access_key)

#usando cliente mqtt


mqtt_client = handler.data()
mqtt_client.set_uplink_callback(uplink_callback)
mqtt_client.connect()
#time.sleep(60)

try:
    while True:
        time.sleep(1)   
            
except KeyboardInterrupt:
    pass