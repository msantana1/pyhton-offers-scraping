import os, smtplib, ssl, sys
import requests
from bs4 import BeautifulSoup

def sendMail(name, url, price, currentPrice, discount, password, sender_email, receiver_email):
    new_name = name.replace("ñ", "n")
    port = 587  # For starttls
    smtp_server = "smtp.office365.com"
    message ="""\
    Subject: OFERTA %s

    ***** OFERTA *****
    Nombre: %s
    URL: %s
    Precio regular: %s
    Precio actual:  %s
    Descuento:      %s""" % (new_name, new_name, url, price, currentPrice, discount)

    print(message)

    context = ssl.create_default_context()
    with smtplib.SMTP(smtp_server, port) as server:
        #server.ehlo()  # Can be omitted
        server.starttls(context=context)
        #server.ehlo()  # Can be omitted
        server.login(sender_email, password)
        server.sendmail(sender_email, receiver_email, message)
        server.quit()

def urlsCyberpuerta(urls):

    for url, price in urls.items():
        page = requests.get(url)
        soup = BeautifulSoup(page.content, "html.parser")
        results = soup.find("div", "nosto_product")
        name = results.find("span", "name").get_text()
        urlvar = results.find("span", "url").get_text()
        currentPrice = results.find("span", "price").get_text()
        availability = results.find("span", "availability").get_text()

        discount = int(price) - int(currentPrice)
        if discount > 0 and availability == "InStock":
            sendMail(name, urlvar, price, currentPrice, discount, password, sender_email, receiver_email)


if "__main__" == __name__:

    urlsRyzen7 = {  'https://www.cyberpuerta.mx/Computadoras/Laptops/Laptop-Dell-Inspiron-5415-14-Full-HD-AMD-Ryzen-7-5700U-1-80GHz-8GB-512GB-SSD-Windows-10-Home-64-bit-Espanol-Platino.html' : '16529',
                    'https://www.cyberpuerta.mx/Computadoras/Laptops/Laptop-ASUS-Vivobook-S-D413UA-14-Full-HD-AMD-Ryzen-7-5700U-1-80GHz-8GB-512GB-SSD-Windows-11-Home-64-bit-Ingles-Negro.html' : '15819',
                    'https://www.cyberpuerta.mx/Computadoras/Laptops/Laptop-ASUS-Vivobook-S-D413UA-14-Full-HD-AMD-Ryzen-7-5700U-1-80GHz-16GB-512GB-SSD-Windows-10-Home-64-bit-Ingles-Negro.html' : '16559',
                    'https://www.cyberpuerta.mx/Computadoras/Laptops/Laptop-HP-EliteBook-845-G9-14-WUXGA-AMD-Ryzen-7-PRO-6850HS-3-20GHz-16GB-512GB-SSD-Windows-10-Pro-64-bit-Espanol-Plata.html' : '24179',
                    'https://www.cyberpuerta.mx/Computadoras/Laptops/Laptop-ASUS-Vivobook-S-D413UA-14-Full-HD-AMD-Ryzen-7-5700U-1-80GHz-16GB-512GB-SSD-Windows-10-Home-64-bit-Espanol-Oro-Rosado.html' : '17699',
                    'https://www.cyberpuerta.mx/Computadoras/Laptops/Laptop-Lenovo-IdeaPad-3-15ALC6-15-6-Full-HD-AMD-Ryzen-7-5700U-1-80GHz-16GB-512GB-SSD-Windows-11-Home-64-bit-Espanol-Arena.html' : '19309',
                    'https://www.cyberpuerta.mx/Computadoras/Laptops/Laptop-Lenovo-V14-G2-ALC-14-HD-AMD-Ryzen-7-5700U-1-80GHz-16GB-512GB-SSD-Windows-10-Pro-64-bit-Espanol-Gris.html' : '19245'}
    
    urlsi7 = {  'https://www.cyberpuerta.mx/Computadoras/Laptops/Laptop-Gamer-XPG-Xenia-14-14-Full-HD-Intel-Core-i7-1165G7-2-80GHz-16GB-512GB-SSD-Windows-10-Home-64-bit-Espanol-Negro.html' : '16049',
                'https://www.cyberpuerta.mx/Computadoras/Laptops/Laptop-Gamer-Dell-Vostro-5310-13-3-Quad-HD-Intel-Core-i7-11390H-3-40GHz-16GB-512GB-SSD-NVIDIA-GeForce-MX450-Windows-11-Pro-64-bit-Espanol-Verde.html' : '22269', 
                'https://www.cyberpuerta.mx/Computadoras/Laptops/Laptop-Dell-Inspiron-3511-15-6-Full-HD-Intel-Core-i7-1165G7-2-80GHz-16GB-512GB-SSD-Windows-11-Home-64-bit-Espanol-Plata.html' : '21759', 
                'https://www.cyberpuerta.mx/Computadoras/Laptops/Laptop-Dell-Latitude-3520-15-6-Full-HD-Intel-Core-i7-1165G7-2-80GHz-16GB-512GB-SSD-Windows-11-Pro-64-bit-Espanol-Negro.html' : '25959'}

    password = sys.argv[1]
    sender_email = sys.argv[2]
    receiver_email = sys.argv[3] 

    urlsCyberpuerta(urlsRyzen7)
    urlsCyberpuerta(urlsi7)