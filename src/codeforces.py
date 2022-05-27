from calendar import c
from re import A
import time
from turtle import title
from numpy import alltrue, full
from requests import request
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException
from selenium.common.exceptions import WebDriverException
import random
from csv import DictWriter
from lxml import html

from helpers import *


def scrape_func(URL):
    chrome_options = Options()
    chrome_options.add_argument('--no-sandbox')
    chrome_options.add_argument('--window-size=1920,1080')
    chrome_options.add_argument('--headless')
    chrome_options.add_argument('--disable-gpu')
    chrome_options.add_argument('--disable-dev-shm-usage')
    driver = webdriver.Chrome(options=chrome_options)

    driver.get(URL)
    htmltree = html.fromstring(driver.page_source)

    #start page
    page = 1

    #count total pages now
    pagesbar = htmltree.xpath(".//div[@class='pagination']/ul/li")
    len_of_bar = len(pagesbar)
    pages = htmltree.xpath(f".//div[@class='pagination']/ul/li[{len_of_bar-1}]/span//text()")[0]

    delay = 5

    while(True):

        
        htmltree = html.fromstring(driver.page_source)
        problembox = htmltree.xpath(".//table[@class='problems']/tbody/tr")
        l = len(problembox)
        # try:
        #     myElem = WebDriverWait(driver, delay).until(EC.element_to_be_clickable(f".//table[@class='problems']/tbody/tr[{l}]/td[2]/div[1]/a"))
        # except:
        #     print('jhulche')
        #     continue

        for i in range(2,len(problembox)+1):
            
            try:
                problemlink = htmltree.xpath(f".//table[@class='problems']/tbody/tr[{i}]/td[2]/div[1]/a/@href")
                title = htmltree.xpath(f".//table[@class='problems']/tbody/tr[{i}]/td[2]/div[1]/a/text()")
                tags = htmltree.xpath(f".//table[@class='problems']/tbody/tr[{i}]/td[2]/div[2]/a/text()")

                # print(i,problemlink[0].__str__())
                # if(problemlink == ""):
                #     problemlink = htmltree.xpath(f"(.//table[@class='problems']/tbody/tr[{i}]/td[2]/div[1]/a/@href")
                # print(type(problemlink))
                z = problemlink[0].__str__()
                # print(i,problemlink[0].__str__())

                problemlink = "https://codeforces.com" + z
                print(problemlink)
                title = process(title[0])

                driver.get(problemlink)
                statementhtml = html.fromstring(driver.page_source)
                statement = statementhtml.xpath(".//div[@class='problem-statement']/div[2]//text()")

            except:
                continue
            

            result = ""

            #iterator var
            i=0
            while i<len(statement):
                ch = statement[i]
                result+=" "+ch

                if (i+2)<len(statement):
                    if ch==statement[i+1] and ch==statement[i+2]:
                        i+=2                    
                    elif ch==statement[i+1]:
                        i+=1

                #increment iterator
                i+=1


            tagplus = ""
            for tag in tags:
                tagplus+= " " + tag

            statement = result
            statement = title + " " + statement + tagplus
            #remove double spaces
            statement.replace('',"")

            result = ""
            for ch in statement.split(" "):
                if len(ch)==0:
                    continue
                else:
                    result+=ch+" "

            statement = result    

            dict = {"Title":title,"Statement":statement,"Link":problemlink,"Tag":"CF"}
            my_write("./visited/codeforces/codeforces.csv",dict)


        if page==pages:
            break

        #flip to next page
        page+=1
        #newlink
        link = f"https://codeforces.com/problemset/page/{page}"
        #get the page
        driver.get(link)

        


def main():
    scrape_func("https://codeforces.com/problemset/")


if __name__ == "__main__":
    main()