#! python3
import bs4, requests, smtplib, urllib.request, time
from decouple import config
while True:
    status = urllib.request.urlopen('https://www.microsoft.com/es-ES/download/details.aspx?id=53127').getcode()
    status1 = urllib.request.urlopen('https://www.microsoft.com/es-es/download/details.aspx?id=39717').getcode()
#If it returns 200, the website is up
    if status != 200 and status1 != 200:
#Call email function
        ResultText = "The website is down"
        print(ResultText)
    
    else:
        getPage = requests.get('https://www.microsoft.com/es-ES/download/details.aspx?id=53127')
        getPage1 = requests.get('https://www.microsoft.com/es-es/download/details.aspx?id=39717')
        soup = bs4.BeautifulSoup(getPage.text, 'html.parser')
        a = soup.find_all('div', {"class" : "row-fluid no-margin-row"})
        ResultText = a[6].get_text()
        cstr = "Datos del Gateway actualizados"
        b = cstr + ResultText.encode('raw_unicode_escape').decode('utf8')
        print(b)
        soup = bs4.BeautifulSoup(getPage1.text, 'html.parser')
        a = soup.find_all('div', {"class" : "row-fluid no-margin-row"})
        ResultText = a[6].get_text()
        cstr = "Datos del Integration Runtime actualizados"
        b = cstr + ResultText.encode('raw_unicode_escape').decode('utf8')
        print(b)
        time.sleep(2000)

