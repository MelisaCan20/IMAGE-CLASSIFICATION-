import requests
from bs4 import BeautifulSoup
import os



def downimage(link,categoryName,page):
    r = requests.get(link)
    categoryContent = BeautifulSoup(r.content, "lxml")
    products = categoryContent.find_all("div", attrs={"class":"products__item-img-container ratio-container"})
    n=1 
    for product in products:
       try:    
            productPhoto = product.find("img")
            url = productPhoto["data-src"]
            r = requests.get(url)
       except:
            print("**")
       with open(categoryName+'/image'+str(page)+str(n)+categoryName+'.jpg', 'wb') as f:
            f.write(r.content)
    
        # datayı alma
        # print(r.status_code)
        # print(r.headers['content-type'])
        # print(r.encoding)
        
       n = n+1
    
Category=[]
def findCategory(url):
      r=requests.get(url)
      soup = BeautifulSoup(r.content, "lxml")
      categories=soup.find_all("a",attrs={"category-slider__link"})
      for c in range(len(categories)):
        Category.append(categories[c]["href"])
        
      for i in range(len(Category)):
        createFolder(Category[i])
      
      
def createFolder(categoryName):
  if not os.path.exists(categoryName):
     f=os.mkdir(categoryName)
  
  link="https://www.ciceksepeti.com/"+categoryName
  for i in range(5):
    
    if i==0:
      continue
    if i>1:
     link="https://www.ciceksepeti.com/"+categoryName+"?page"+"="+str(i)
     downimage(link,categoryName,i)
    if i==1: 
            downimage(link,categoryName,1)





url="https://www.ciceksepeti.com/kadin-ust-giyim"
findCategory(url)
