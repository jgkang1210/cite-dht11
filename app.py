from flask import Flask, render_template, request
import Adafruit_DHT

# flask setting
app = Flask(__name__)

# sensor setting
sensor = Adafruit_DHT.DHT11
pin = '4'

def get_sensor_data():
    humidity, temperature = Adafruit_DHT.read_retry(sensor,pin)
    data = ''
    
    if humidity is not None and temperature is not None:
        data = 'Temp={0:0.1f}*C Humidity={1:0.1f}%'.format(temperature, humidity)
    else:
        data = 'Failed to get reading. Try again!'

    return data

@app.route('/')
def hello_name():
   return render_template('index.html', string=get_sensor_data())

host_addr = "0.0.0.0"
port_num = "5000"

if __name__ == '__main__':
   app.run(host=host_addr, port=port_num, debug = True)
