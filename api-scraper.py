#Import libraries for Python Website Monitoring project
import urllib.request
import smtplib,time, hashlib
import requests
import urllib
from decouple import config
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities



from flask import Flask, request, render_template,jsonify
import bs4, requests, smtplib, urllib.request, time
from decouple import config
import os
import psycopg2
from psycopg2 import pool



app = Flask(__name__)


def do_something():

    input_website = 'https://analisiscalidadaire.madrid.es/situacionactual'

    
    ResultText = "The website is up"
    options = Options()
    options.headless = True
    options.add_argument('--disable-blink-features=AutomationControlled')
    time.sleep(5)
   #driver = webdriver.Remote("http://selenium:4444/wd/hub",options=options)
    time.sleep(10)

   #driver = webdriver.Chrome('/Users/Rafa./Downloads/chromedriver', options=options)
    driver = webdriver.Chrome('/Users/rvilchef/OneDrive - NTT DATA EMEAL/chromedriver', options=options)
    driver.get("https://analisiscalidadaire.madrid.es/situacionactual")
    time.sleep(5)
    a = driver.find_element(by=By.XPATH, value=("//*[@id='tiempo_real_fecha']")).text
    time.sleep(5)

    print(ResultText)
    b = "Última carga de datos realizada: {}, \n {}".format(a, ResultText)
    print(b)    

    return '''
<body>
    <p> Obteniendo datos de la web...
<br><br>

          <br> Primer scrapeo: {}<br>
          
 </p>
</body>

'''.format(b)
    driver.quit();




def test_conexion():
    try:  
         postgreSQL_pool = psycopg2.pool.SimpleConnectionPool(1, 20, user = os.environ['user'],
                                                         password = os.environ['password'],
                                                         host= os.environ['host'],
                                                         port = os.environ['port'],
                                                         database = os.environ['database'])

         if (postgreSQL_pool):
             print("Connection pool created successfully")


         ps_connection = postgreSQL_pool.getconn()
         if (ps_connection):
             ps_cursor = ps_connection.cursor()
             ps_cursor.execute("SELECT to_char(dia, 'YYYY-MM-DD') AS Fechas, hora AS Hora, COUNT(*) AS registro \
FROM wbana.detalle_hora GROUP BY dia, hora ORDER BY dia DESC, hora DESC LIMIT 5")

             records = ps_cursor.fetchall()
             print("Ver si los datos horarios se están cargando correctamente hora a hora")
             #print(type(records))  
             lista = { lista : "Output" for lista in records }
             return(lista)
             ps_cursor.close()
             postgreSQL_pool.closeall 

             postgreSQL_pool.putconn(ps_connection)
             print("Put away a PostgreSQL connection")

    except (Exception, psycopg2.DatabaseError) as error:
        print("Error while connecting to PostgreSQL", error)

    finally:
    # closing database connection.
    # use closeall() method to close all the active connection if you want to turn of the application
        if postgreSQL_pool:
            postgreSQL_pool.closeall
        print("PostgreSQL connection pool is closed")




def test_pool():
    try:  
         postgreSQL_pool = psycopg2.pool.SimpleConnectionPool(1, 20, user = os.environ['user'],
                                                         password = os.environ['password'],
                                                         host= os.environ['host'],
                                                         port = os.environ['port'],
                                                         database = os.environ['database'])

         if (postgreSQL_pool):
             print("Connection pool created successfully")


         ps_connection = postgreSQL_pool.getconn()
         if (ps_connection):
             ps_cursor = ps_connection.cursor()
             ps_cursor.execute("select  * from \
(select count(*) used from pg_stat_activity) q1, \
(select setting::int res_for_super from pg_settings where name=$$superuser_reserved_connections$$) q2, \
(select setting::int max_conn from pg_settings where name=$$max_connections$$) q3;")

             records = ps_cursor.fetchall()
             print("Pool de conexiones")
             #print(type(records))  
             return(records)
             ps_cursor.close()
             postgreSQL_pool.closeall 

             postgreSQL_pool.putconn(ps_connection)
             print("Put away a PostgreSQL connection")

    except (Exception, psycopg2.DatabaseError) as error:
        print("Error while connecting to PostgreSQL", error)

    finally:
    # closing database connection.
    # use closeall() method to close all the active connection if you want to turn of the application
        if postgreSQL_pool:
            postgreSQL_pool.closeall
        print("PostgreSQL connection pool is closed")

        

@app.route('/')
def home():
    return render_template('home.html')



@app.route('/join', methods=['GET','POST'])
def my_form_post():
    combine = do_something()
    result = {
        "output": combine
    }
    result = {str(key): value for key, value in result.items()}
    return jsonify(result=result)

@app.route('/test', methods=['GET','POST'])
def prueba():
    combinar = test_conexion()
 

    #    resultado = {
    #    "output": combinar
  #  }
    resultado = {str(key): value for key, value in combinar.items()}
    print(resultado)
    #print(jsonify(result=result))
    return jsonify(resultado=resultado)

@app.route('/pool', methods=['GET','POST'])
def pool():
    prueba = test_pool()
    print(prueba) 

    resultado = {
        "output": prueba
    }
    resultado = {str(key): value for key, value in resultado.items()}
    print(resultado)
    #print(jsonify(result=result))
    return jsonify(resultado=resultado)


if __name__ == "__main__":
    port = int(os.environ.get('PORT', 5003))
    app.run(debug=True, host='0.0.0.0', port=port)


    
