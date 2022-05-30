import board
import busio
import adafruit_bme280
import pymysql

i2c = busio.I2C(board.SCL, board.SDA)
bme280 = adafruit_bme280.Adafruit_BME280_I2C(i2c)
nowDay = time.strftime("%Y-%m-%d" , time.localtime())
nowTime = time.strftime("%H:%M:%S" , time.localtime())
temper = (round(temperature), 1)

db = pymysql.connect(host='localhost', user='root', password='1234', 
db = 'temperature', charset='utf8')
cur = db.cursor()
cur.execute("SELECT*FROM temperature")

while True:
    print("\nTemperature: %0.1f C" % bme280.temperature)
    cur.execute("insert into temperature ('nowDay', 'nowTime', 'temper') VALUES(nowDay, nowTime,temper);")
    sleep(3600)