## https://www.codementor.io/@gergelykovcs/scrape-the-web-with-python-and-get-updates-on-telegram-rv83fbgie
## https://www.codementor.io/@gergelykovcs/how-and-why-i-built-a-simple-web-scrapig-script-to-notify-us-about-our-favourite-food-fcrhuhn45


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

    driver = webdriver.Chrome('/Users/Rafa./Downloads/chromedriver', options=options)
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

#@app.route('/')
#def home():
#    return render_template('home.html')

@app.route('/')
def my_form_post():
    combine = do_something()
   
    
    return combine

if __name__ == "__main__":
    port = int(os.environ.get('PORT', 5003))
    app.run(debug=True, host='0.0.0.0', port=port)

