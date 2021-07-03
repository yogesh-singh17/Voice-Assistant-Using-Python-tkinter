
from bs4 import BeautifulSoup
import time
import requests

def covid_d(State):

    myhtlmdata=requests.get("https://www.mohfw.gov.in/").text
    soup =BeautifulSoup(myhtlmdata,'html.parser')    
    mydatastr=""
    for table in soup.find_all('tbody'):
        mydatastr += table.get_text()
        mydatastr=mydatastr[2:]
        list= mydatastr.split("\n\n\n")
        datalist=[]
    for item in list[0:35]:
        a = item.split("\n")
        datalist.append(a)
    for j in range(35):
        if State in datalist[j][1]:
            totalcases=datalist[j][5]
            curedcases=datalist[j][3]
            deaths=datalist[j][4]
            activecases=datalist[j][2]
            break
    return totalcases,activecases,deaths,curedcases
    '''print("Total cases : ",totalcases)    
       
    print("Active cases : ",activecases)      
    print("Deaths : ",deaths)      
    print("Cured cases : ",curedcases)  ''' 
    
    
    
#Covid_d("Delhi")