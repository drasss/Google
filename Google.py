from googlesearch import search
import requests
from bs4 import BeautifulSoup as bs
import urllib.request, urllib.error, urllib.parse,os
        
def google_search(query,pages):
    result=[]
    i=0
    for k in search(query, lang="en", num=pages, stop=10, pause=2):
        result+=[k]
        print("\n\n",i+1,") ",k)
        i+=1
    return(result)
        
def google_open(url):

    reponse = urllib.request.urlopen(url)
    contenu_web = reponse.read().decode('UTF-8')

    f = open('temp.html', 'w')
    f.write(contenu_web)
    f.close
    os.system("start temp.html")
        

if __name__=="__main__":
    choix=""
    while choix.upper()!="QUIT":
        choix=input("-------------\n --: ")
        if choix.upper()!="QUIT":
            print("------------- quel site voulez vous voir ?")
            result=google_search(choix, 10)
            site_nb=int(input(""))
            google_open(result[site_nb-1])
        
        
        
