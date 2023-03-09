import os, smtplib, ssl, sys
import requests
from bs4 import BeautifulSoup

data = [["https://www.cyberpuerta.mx/Computadoras/Laptops/Laptop-Dell-Inspiron-5415-14-Full-HD-AMD-Ryzen-7-5700U-1-80GHz-8GB-512GB-SSD-Windows-10-Home-64-bit-Espanol-Platino.html",
        "https://www.cyberpuerta.mx/Computadoras/Laptops/Laptop-ASUS-Vivobook-S-D413UA-14-Full-HD-AMD-Ryzen-7-5700U-1-80GHz-8GB-512GB-SSD-Windows-11-Home-64-bit-Ingles-Negro.html",
        "https://www.cyberpuerta.mx/Computadoras/Laptops/Laptop-ASUS-Vivobook-S-D413UA-14-Full-HD-AMD-Ryzen-7-5700U-1-80GHz-16GB-512GB-SSD-Windows-10-Home-64-bit-Ingles-Negro.html",
        "https://www.cyberpuerta.mx/Computadoras/Laptops/Laptop-HP-EliteBook-845-G9-14-WUXGA-AMD-Ryzen-7-PRO-6850HS-3-20GHz-16GB-512GB-SSD-Windows-10-Pro-64-bit-Espanol-Plata.html",
        "https://www.cyberpuerta.mx/Computadoras/Laptops/Laptop-ASUS-Vivobook-S-D413UA-14-Full-HD-AMD-Ryzen-7-5700U-1-80GHz-16GB-512GB-SSD-Windows-10-Home-64-bit-Espanol-Oro-Rosado.html",
        "https://www.cyberpuerta.mx/Computadoras/Laptops/Laptop-Lenovo-IdeaPad-3-15ALC6-15-6-Full-HD-AMD-Ryzen-7-5700U-1-80GHz-16GB-512GB-SSD-Windows-11-Home-64-bit-Espanol-Arena.html",
        "https://www.cyberpuerta.mx/Computadoras/Laptops/Laptop-Lenovo-V14-G2-ALC-14-HD-AMD-Ryzen-7-5700U-1-80GHz-16GB-512GB-SSD-Windows-10-Pro-64-bit-Espanol-Gris.html"],
        ["16529", "15819", "16559", "24179", "17699", "19309", "19245"]]

def send_mail(name, url1, price, password, sender_email, receiver_email):
    new_name = name.replace("ñ", "n")
    port = 587  # For starttls
    smtp_server = "smtp.office365.com"
    message ="""\
    Subject: OFERTA %s

    ***** OFERTA *****
    Nombre: %s
    URL: %s
    Precio: %s""" % (new_name, new_name, url1, price)

    print(message)
    #print(password)

    context = ssl.create_default_context()
    with smtplib.SMTP(smtp_server, port) as server:
        #server.ehlo()  # Can be omitted
        server.starttls(context=context)
        #server.ehlo()  # Can be omitted
        server.login(sender_email, password)
        server.sendmail(sender_email, receiver_email, message)
        server.quit()

if "__main__" == __name__:
    
    urls = data[0]
    prices = data[1]

    password = sys.argv[1]
    sender_email = sys.argv[2]
    receiver_email = sys.argv[3] 

    count = 0
    for url in urls:
        page = requests.get(url)
        soup = BeautifulSoup(page.content, "html.parser")
        results = soup.find("div", "nosto_product")
        name = results.find("span", "name").get_text()
        url1 = results.find("span", "url").get_text()
        price = results.find("span", "price").get_text()
        availability = results.find("span", "availability").get_text()

        current_price = prices[count]
        count += 1
        if int(price) < int(current_price) and availability == "InStock":
            send_mail(name, url1, price, password, sender_email, receiver_email)