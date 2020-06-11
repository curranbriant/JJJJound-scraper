import bs4
import urllib
from urllib import urlopen as uReq
from bs4 import BeautifulSoup as soup
import shutil

my_url = "http://www.jrsrules.com/wp-content/uploads/"
uClient = uReq(my_url)
page_html = uClient.read()
uClient.close()
page_soup = soup(page_html, "html.parser")
mydivs = page_soup.find("table", {"class": None})
children = mydivs.findChildren("tr" , recursive=False)
for child in children:
    tds = child.findChildren("td" , recursive=False)
    for td in tds:
        imgs = td.findChildren("a" , recursive=False)
        x = 1
        for img in imgs:
            image = img['href']
            img_url = my_url + image
            filename,headers = urllib.urlretrieve(img_url)
            print(filename)
            shutil.copy(filename, "path/to/local")
