
import network
import urequests as requests
import ujson as json
from machine import Pin
from utime import sleep
p0=Pin(16,Pin.OUT)#inbuilt led GPIO 16
p2=Pin(14,Pin.OUT)#D5  GPIO 14
wlan = network.WLAN(network.STA_IF) # create station interface
wlan.active(True)       # activate the interface
wlan.connect('Omm','omm12345') # connect to an Mobile hotspot(ssid,password)


min_value=30
max_value=50

p2.value(1)

p1=machine.ADC(0) #A0 PIN
while(1):
    av=p1.read()
    ao=av/1023
    Mp=int(abs(100-(ao*100)))
   
    #print(av) #adc read
    #print(ao) #analog output
    print(str(Mp)+"%")
    setpoint=requests.post("https://api.thingspeak.com/update?api_key=BTU0V47VVN8VJPX8&field1=0"+str(Mp))
    Mp_d=setpoint.json()
    #print(Mp_d)
    
    if Mp>min_value or Mp>max_value:
   
        p0.value(0)
        p2.value(1)
        
   
    else:
   
        p0.value(1)
        p2.value(0)
        
    
   

   