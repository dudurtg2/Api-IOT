#import esp
#esp.osdebug(None)
#import webrepl
#webrepl.start()



import network
import time
from machine import Pin, ADC
import dht
import urequests
import time

# LEDs de status Wi-Fi
WIFI_LED_ON = Pin(23, Pin.OUT)  
WIFI_LED_OFF = Pin(22, Pin.OUT)

# LEDs de status POST
POST_SUCCESS = Pin(21, Pin.OUT)  


# Controle de bomba e relé
PAMP = Pin(18, Pin.OUT) 
RELAY_LIGHT = Pin(5, Pin.OUT)  # Controle do relé para luz ambiente

# Sensor de erro
ERROR_LED = Pin(19, Pin.OUT)

# Sensores de temperatura/umidade, umidade do solo e luz ambiente
SENSOR_TEMPERATURY_HUMIDITY = dht.DHT11(Pin(15))
SENSOR_SOLID_HUMIDITY = ADC(Pin(34)) 
SENSOR_SOLID_HUMIDITY.atten(ADC.ATTN_11DB)
SENSOR_LIGHT = ADC(Pin(33)) 
SENSOR_LIGHT.atten(ADC.ATTN_11DB)

url = "http://carlo4664.c44.integrator.host:10503/monitor/save"

def conectar_wifi(ssid, senha):
    wlan = network.WLAN(network.STA_IF)
    wlan.active(True)
    wlan.connect(ssid, senha)

    while not wlan.isconnected():
        print("Conectando ao Wi-Fi...")
        WIFI_LED_ON.off()
        time.sleep(0.5)
        WIFI_LED_OFF.on()
        time.sleep(1)

    print("Conectado ao Wi-Fi:", wlan.ifconfig())
    WIFI_LED_ON.on()
    WIFI_LED_OFF.off()

    while True:
        if wlan.isconnected():
            WIFI_LED_ON.on()
            WIFI_LED_OFF.off()
            try:
                SENSOR_TEMPERATURY_HUMIDITY.measure()
                temperatura = SENSOR_TEMPERATURY_HUMIDITY.temperature()
                umidade = SENSOR_TEMPERATURY_HUMIDITY.humidity()
            except Exception as e:
                print("Erro ao ler o sensor DHT11:", e)
                ERROR_LED_ALERT(1)
                continue

            try:
                solid_humidity = WHITE_SENSOR_SOLID_HUMIDITY() / 100
            except Exception as e:
                print("Erro ao ler o sensor de umidade do solo:", e)
                ERROR_LED_ALERT(2)
                continue

            try:
                light_value = SENSOR_LIGHT.read() / 100
            except Exception as e:
                print("Erro ao ler o sensor de luminosidade:", e)
                ERROR_LED_ALERT(3)
                continue

            try:
                pamp_status = PAMP_TRIGGER(solid_humidity)
                light_status = LIGHT_TRIGGER(light_value)

                POST_INFO(temperatura, umidade, solid_humidity, pamp_status, light_status)
                print("Temperatura: {}°C, Umidade: {}%, Umidade do Solo: {}, Luminosidade: {}".format(
                    temperatura, umidade, solid_humidity, light_value))
            except Exception as e:
                print("Erro ao enviar dados:", e)
                ERROR_LED_ALERT(4)
        else:
            WIFI_LED_ON.off()
            WIFI_LED_OFF.on()
        
        time.sleep(10)

def ERROR_LED_ALERT(count):
    
    # 1 para erro do sensor DHT11
    # 2 para erro do sensor de umidade do solo
    # 3 para erro do sensor de luminosidade
    # 4 para erro da post falhou

    for i in range(count):
        ERROR_LED.on()
        time.sleep(1)
        ERROR_LED.off()
        time.sleep(1)
    time.sleep(2)
    
def WHITE_SENSOR_SOLID_HUMIDITY():
    return SENSOR_SOLID_HUMIDITY.read()

def PAMP_TRIGGER(solid_humidity):
    if solid_humidity > 35: # cabo verder
        PAMP.on()
        return True
    else:
        PAMP.off()
        return False

def LIGHT_TRIGGER(light_value):
    if light_value > 22:  
        RELAY_LIGHT.on()  
        return True
    else:
        RELAY_LIGHT.off()  
        return False

def POST_INFO(temperature, humidity, solid_humidity, pamp_status, light_status):
    current_time = time.localtime()
   
    formatted_time = "{:04d}-{:02d}-{:02d}".format(
        current_time[0],  
        current_time[1], 
        current_time[2] 
    )
    payload = {
        "temperature": temperature,
        "humidity": humidity,
        "pampStatus": pamp_status,
        "solidhumidity": solid_humidity,
        "lightStatus": light_status,
        "date": formatted_time,
    }

    try:
        response = urequests.post(url, json=payload)
        print(f"Dados enviados: \n{payload}, \nStatus: {response.status_code}")
        POST_SUCCESS.on()
        time.sleep(2)
        POST_SUCCESS.off()
    except Exception as e:
        print(f"Erro ao enviar dados: {e}")   
        ERROR_LED_ALERT(4)  

conectar_wifi('SENAI_ACADEMICO', 'Senai*Academico')





