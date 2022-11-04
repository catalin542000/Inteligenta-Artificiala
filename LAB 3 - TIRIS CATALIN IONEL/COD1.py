from hashlib import new
import requests
from bs4 import BeautifulSoup
import smtplib

def trimitere_email():
    server=smtplib.SMTP('mail.x-it.ro',26)
    server.starttls()
    server.login("data_scraping@coneasorin.ro","stiinte216_2022")
    server.sendmail("data_scraping@coneasorin.ro","catalin542000@gmail.com","Subject: Pretul a scazut\n\nPretul a scazut la 1000 lei")
    print ("Email trimis")
    server.quit()

def data_scraping():
    req = requests.get('https://www.emag.ro/telefon-mobil-samsung-galaxy-s22-ultra-dual-sim-256gb-12gb-ram-5g-phantom-black-sm-s908bzkgeue/pd/DQZ01FMBM/')
    soup=BeautifulSoup(req.text, 'html.parser')
    price=soup.find('p', attrs={'class':'product-new-price'}).text
    new_price=price[0:5]
    new_price=new_price.replace(".","")
    new_price=int(new_price)
    if(new_price<7799):
        trimitere_email()
        print("Avem o modificare de pret!!!")
    else:
        print("Pretul nu a scazut")