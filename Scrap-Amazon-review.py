#Author- Martial Himanshu
#License- GNU 

import requests
from bs4 import BeautifulSoup

def get_reviews(p_name):
    url = "http://www.amazon.in/s/ref=nb_sb_noss?url=search-alias%3Daps&field-keywords=" + p_name
    r = requests.get(url)
    soup = BeautifulSoup(r.content,"html.parser")
    
    pid = soup.find_all("li",{"class":"s-result-item celwidget"})[0].get("data-asin")
    plink = soup.find_all("li",{"class":"s-result-item celwidget"})[0].find_all("a",{"class":"a-link-normal s-access-detail-page  a-text-normal"})[0].get("href")
    
    new_url = "http://www.amazon.in/product-reviews/" + pid + "/ref=acr_search_see_all?ie=UTF8&showViewpoints=1"
    r = requests.get(new_url)
    soup = BeautifulSoup(r.content,"html.parser")
    
    reviews_list = soup.find_all("div",{"class":"a-section a-spacing-none reviews celwidget"})[0]
    
    for review in reviews_list:
        try:
            next_review = review.find_all("span",{"class":"a-size-base review-text"})[0].text
            print(next_review,end="[END]")
            print("\n")
        except:
            pass


if '__name__' == '__main__':
    p_name = input("Enter a product name : ")
    get_reviews(p_name)
