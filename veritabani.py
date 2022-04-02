import sqlite3
import requests
from bs4 import BeautifulSoup
con=sqlite3.connect("proje.db")
cursor=con.cursor()

def tablo():
    cursor.execute("CREATE TABLE IF NOT EXISTS kütüphane('İsim','Yayın','Yazar','Fiyat')")
    con.commit
tablo()


def veriekle(isim,yazar,yayın,fiyat):
    cursor.execute("insert into kütüphane values (?,?,?,?)",(isim,yayın,yazar,fiyat))
    con.commit()


url = "https://www.bkmkitap.com/kitap/cok-satan-kitaplar"
response = requests.get(url)
html_icerigi = response.content
soup = BeautifulSoup(html_icerigi,"html.parser")
fiyat = soup.find_all("div",{"class":"col col-12 currentPrice"})
isim =soup.find_all("a",{"class":"fl col-12 text-description detailLink"})
yazar = soup.find_all("a",{"class":"fl col-12 text-title"})


yayın = soup.find_all("a",{"class":"col col-12 text-title mt"})

for i in range(len(isim)):
    isim[i] = (isim[i].text).strip("\n").strip()
    yazar[i] = (yazar[i].text).strip("\n").strip()
    yayın[i] = (yayın[i].text).strip("\n").strip()
    fiyat[i] = (fiyat[i].text).strip("\n").replace("\nTL"," TL").strip()
    cursor.execute("SELECT * FROM kütüphane WHERE İsim = (?) AND Yazar=(?)",(isim[i],yazar[i]))
    data=cursor.fetchone()
    if data:
         pass   
    else:
        veriekle(isim[i],yazar[i],yayın[i],fiyat[i])


def verial(yayın):
    cursor.execute("SELECT * FROM kütüphane WHERE Yayın=(?)",(yayın,))
    liste=cursor.fetchall()
    for i in liste:
        print(i)
        
        
def verideğiştir(eskiisim,eskiyayın,yeniyayın):
    cursor.execute("SELECT * FROM kütüphane WHERE İsim=?",(eskiisim,))
    data=cursor.fetchone()
    if data:
        cursor.execute("UPDATE kütüphane set Yayın = ? where Yayın = ?",(yeniyayın,eskiyayın,))
    else:
        print("Lütfen Kontrol Ediniz")
def verisil(yazar):
    cursor.execute("DELETE FROM kütüphane WHERE Yazar=?",(yazar,))
    con.commit()


