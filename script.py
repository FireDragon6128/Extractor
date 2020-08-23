from bs4 import BeautifulSoup
import requests

def extract():   
    lis = []
    title_list=[]
    f = open("domains.txt", "r")
    for x in f:
        x = x.replace('\n', '')
        x = "http://www." + x
        lis.append(x)
        try:
            r = requests.get(x,headers = {"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/70.0.3538.77 Safari/537.36"})
            soup = BeautifulSoup(r.content, "html")
            if (soup.title is not None):
                title = soup.title.string
                if(title == None):
                    title = "Not found"
            else:
                t = soup.find("meta",  property="og:title")
                title = t["content"] if t else "No meta title given"
            title = title.strip()
            print (title)
            title_list.append(title)
        except requests.exceptions.ConnectionError:
            status = str(r.status_code)
            title = "Refused with " + status
            print(title)
            title_list.append(title)
        
    with open('titles.txt', 'w', encoding="utf-8") as f:
        for item in title_list:
            f.write("%s\n" % item)

if __name__ == '__main__':
    extract()