from bs4.element import SoupStrainer
import requests
from bs4 import BeautifulSoup


def Links(url):
    req = requests.get(url)
    data = req.text
    soup = BeautifulSoup(data, 'html.parser')
    titulo = soup.title.string
    fo = open("{titulo}.txt", "a")
    for link in (soup.find_all('a')):
        if (link.get('href')) is not None:
            pagina = link.get('href')
            fo.write("\n {pagina}")
            print('\n ', link.get('href'))
    fo.close()

def Titulo(url):
    req = requests.get(url)
    data = req.text
    soup = BeautifulSoup(data, 'html.parser')
    title_name = soup.title.string
    title_parent = soup.title.parent.name

    print('\nBasic information:')
    print('\nTitle name: ', title_name)
    print('\nTitle parent: ', title_parent)

def Respuesta(url):
    req = requests.get(url)
    if req.status_code == 200:
        return 1
    else:
        return 0

def WebScrapping(ip):
        pStatus = url_Status(ip)
        if pStatus == 1:
            cont = False
        else:
            input("\nError, no hay respuesta.")
        Basic_Info(ip)
        print("\nLinks: ")
        Links(ip)
