import pymysql
import time
import datetime


while True:
    db = pymysql.connect(host='119.194.240.110', port=33060, user='tlsl13', password='1234', db='MMM_Temperature', charset='utf8')
    cur = db.cursor()
    
    now = datetime.datetime.now()
    day = '"{}"'.format(now.strftime('%y-%m-%d'))
    Time = '"{}"'.format(now.strftime('%H:%M:%S'))
    
    f = open("/dev/shm/temp.txt","rt")
    temper=f.readline()
    f.close()
    
    sql = "INSERT INTO temperature_home(nowDay, nowTIme, temper)values ({}, {}, {})".format(day, Time, temper)
    cur.execute(sql)
    query = cur.execute("SELECT * FROM temperature_home;")
    print(query, temper)
    db.commit()
    db.close()
    time.sleep(3600)
