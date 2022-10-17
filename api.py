from flask import Flask, request, render_template,jsonify
import bs4, requests, smtplib, urllib.request, time
from decouple import config
import os


app = Flask(__name__)


def do_something():
   
    status = urllib.request.urlopen('https://www.microsoft.com/es-ES/download/details.aspx?id=53127').getcode()
    status1 = urllib.request.urlopen('https://www.microsoft.com/es-es/download/details.aspx?id=39717').getcode()
#If it returns 20
    getPage = requests.get('https://www.microsoft.com/es-ES/download/details.aspx?id=53127')
    getPage1 = requests.get('https://www.microsoft.com/es-es/download/details.aspx?id=39717')
    soup = bs4.BeautifulSoup(getPage.text, 'html.parser')
    a = soup.find_all('div', {"class" : "row-fluid no-margin-row"})
    ResultText = a[6].get_text()
    cstr = "Datos del Gateway actualizados"
    b = cstr + ResultText.encode('raw_unicode_escape').decode('utf8')
    print(b)
    soup = bs4.BeautifulSoup(getPage1.text, 'html.parser')
    c = soup.find_all('div', {"class" : "row-fluid no-margin-row"})
    ResultText = c[6].get_text()
    cstr = "Datos del Integration Runtime actualizados"
    d = cstr + ResultText.encode('raw_unicode_escape').decode('utf8')
    print(d)
    
      
    return '''
<body>
    <p> Obteniendo datos de la web...
<br><br>

          <br> Primer scrapeo: {}<br>
          <br> Segundo scrapeo: {}<br>
 </p>
</body>

'''.format(b,d)


#@app.route('/')
#def home():
#    return render_template('home.html')

@app.route('/')
def my_form_post():
    combine = do_something()
   
    
    return combine

if __name__ == "__main__":
    port = int(os.environ.get('PORT', 5002))
    app.run(debug=True, host='0.0.0.0', port=port)
