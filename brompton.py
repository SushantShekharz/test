import requests
from bs4 import BeautifulSoup
import json
import re
import pandas as pd


df = pd.DataFrame(columns=["Name", "Address", "Zipcode","Phone", "Email", "Latitude", "Longitude"])

url= "https://www.brompton.com/find-a-store"
r=requests.get(url)
htmlContent = r.content
soup = BeautifulSoup(htmlContent,'html.parser')
divTag = soup.find("div",class_="find-a-store-detail")
script_tag = divTag.find('script')
regex = r'"Id":(.*?),"Email":"(.*?)".*?"Phone":"(.*?)","Address1":"(.*?)","City":"(.*?)","Country":"(.*?)","Latitude":(.*?),"Longitude":(.*?),"PostCode":"(.*?)",.*?"Name":"(.*?)"'
try:
    data= re.findall(regex,str(script_tag))
except:
    pass
print(len(data))

print(data[1])
for d in data:
    email=d[1]
    phone=d[2]
    address=d[3]
    city=d[4]
    country=d[5]
    latitude =d[6]
    longitude=d[7]
    postcode = d[8]
    name = d[9]
    data={
        "Name":name,
        "Address":address,
        "Zipcode":postcode,
        "Phone":phone,
        "Latitude":latitude, 
        "Longitude":longitude,
        "email":email,
        "country":country,
        "city":city
    }
    df = df.append(data, ignore_index=True)
df.to_csv("brompton.csv", index=False, encoding='UTF-8')

