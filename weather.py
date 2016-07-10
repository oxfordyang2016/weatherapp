
import requests
import psycopg2
import logging
from  datetime import datetime
from psycopg2 import extras
import json
#import conn

#do not do these
#from kenya   import api_token
#from kenya  import db_password

def fetch_data():
     api_key='f00f1dfe55930ecd1e3a4a28115cb2ab'
     api_token='youtokenhere'
     d='chengdu'
     url='http://api.openweathermap.org/data/2.5/weather?q='+str(d)+'&APPID=f00f1dfe55930ecd1e3a4a28115cb2ab'
     r = requests.get(url).json()
     print (r['wind'])
     print(str(r)+str('this is shnaghai'))
     print (type(r))
     #return(r)
     weather1=str(r['weather'])
     location1 = str(r['coord'])
     wind1 = str(r['wind'])
     city = str(r['name'])


    #conect_db
     try:
         conn =psycopg2.connect(dbname='d9apk8i46rfo8d',user='moxiqfcupkklsg',host='ec2-54-243-199-161.compute-1.amazonaws.com',password='xNL4vr8uvm_gQ7zaKaVGounfZ7')
         print('connect db success')
     except:
         print('aganin do')
         print('in fact your database donot success connect')
         logging.exception('database donnot success connect')
     else:
         cur = conn.cursor(cursor_factory = psycopg2.extras.DictCursor)

     cur.execute("""INSERT INTO station_reading(location ,weather,wind,city)  VALUES  ( %s ,%s ,%s,%s);""",[location1,weather1,wind1,city])

     conn.commit()

     cur.close()

     conn.close()

     print("data written ",datetime.now())


fetch_data()






