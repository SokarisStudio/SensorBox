import requests
import smbus
import time
import Adafruit_DHT

pin = 17


def readandsend():
    
    humidity, temperature = Adafruit_DHT.read_retry( Adafruit_DHT.DHT22, pin )
    if humidity is not None and temperature is not None:
        print ("Temp={0:f} *C Humidity={1:f} %".format(temperature, humidity))
    else:
        print("Fail")
        
    url = "http://sensors.vasily.onl/send_data.php?api_key=12345678"

    payload={'api_key':'12345678','sensor_id':'1','location_id':'1','client_id':'0','value_temp':str(temperature)+' *C','value_humidity':str(humidity)+' %','value_light':str(res)+' lx','value_sound':'85'}

    files=[]

    headers={}

    response=requests.request("POST",url,headers=headers,data=payload,files=files)

    print(response.text)

while True:
    readandsend()


    time.sleep(10)