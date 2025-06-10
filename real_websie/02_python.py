from bs4 import BeautifulSoup
import requests

print("put some non familiar skills according to you")
unknown_skills = input('>')
print(f"filtering out :{unknown_skills}")


html_text = requests.get("https://www.timesjobs.com/candidate/job-search.html?searchType=personalizedSearch&from=submit&searchTextSrc=&searchTextText=&txtKeywords=python&txtLocation=").text
soup = BeautifulSoup(html_text,'lxml')

jobs = soup.find_all('li',class_='clearfix job-bx wht-shd-bx')

for job in jobs:
    pub_date=job.find('span',class_='sim-posted').text
    cmpy =job.find('h3',class_='joblist-comp-name').text.replace(' ','')
    if 'few' in pub_date:

        location = job.find('li',class_='srp-zindex location-tru').text

        skills_raw = job.find('div', class_='more-skills-sections').text
        skills = ", ".join(skills_raw.strip().split())
        
        extra_info = job.header.h2.a['href']


        if unknown_skills not in skills: 
            print(f"company : {cmpy.strip()} \n date : {pub_date.strip()} \n skills: {skills.strip()} \n location : {location.strip()}  \n more info:{extra_info}")

            print(" ")
              
            
          