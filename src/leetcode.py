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


#base url which upon appendment will give page url
base_url = "https://leetcode.com/problemset/all/?page="

def scrape_func(URL):
    chrome_options = Options()
    chrome_options.add_argument('--no-sandbox')
    chrome_options.add_argument('--window-size=1920,1080')
    chrome_options.add_argument('--headless')
    chrome_options.add_argument('--disable-gpu')
    chrome_options.add_argument('--disable-dev-shm-usage')
    driver = webdriver.Chrome(options=chrome_options)

    delay = 10
    # class_of_navbar = "flex items-center justify-center w-8 h-8 rounded select-none focus:outline-none text-sm bg-fill-3 dark:bg-dark-fill-3 text-label-2 dark:text-dark-label-2 hover:bg-fill-2 dark:hover:bg-dark-fill-2 disabled:opacity-40 disabled:pointer-events-none"
    xpath_navbar = ".//nav[@role='navigation']/button[10]"
    
    try:
        driver.get(URL)
        myElem = WebDriverWait(driver, delay).until(EC.presence_of_element_located((By.XPATH, xpath_navbar)))
        print("hurrah!! got the page")
    except:
        return 

    html_tree=html.fromstring(driver.page_source)
    navbar_button = html_tree.xpath("(.//nav[@role='navigation'])[1]/button")
    #get the max number of pages. the rightmost gives the > button; l-1 will be max page
    pages = html_tree.xpath(f"(.//nav[@role='navigation'])[1]/button[{len(navbar_button)-1}]/text()")[0]
    pages = pages.__str__()
    pages = int(pages)


    #start page
    page = 38

    while page<=40:

        #page url 
        url = base_url + str(page)
        # get into the page

        xpath = "(.//div[@class='truncate overflow-hidden'])[1]/a"

        try:
            driver.get(url)
            print("in page, ",page)
            if page>1:
                myElem = WebDriverWait(driver, delay).until(EC.text_to_be_present_in_element((By.XPATH, xpath), str((page-1)*50+1)))
        except:
            continue


        tree2 = html.fromstring(driver.page_source)
        problem_box = tree2.xpath(".//div[@class='flex items-center']")


        for i in range(1,len(problem_box)+1):

            box_element = tree2.xpath(f"(.//div[@class='flex items-center'])[{i}]/*")
            #has premium tag
            if len(box_element)>=2:
                continue

            try:
                link_element = tree2.xpath(f"(.//div[@class='truncate overflow-hidden'])[{i}]/a/@href")[0]
                text_element = tree2.xpath(f"(.//div[@class='truncate overflow-hidden'])[{i}]/a/text()")
                all_text = text_element[0].__str__()
                title = all_text.split(".")[1].strip()
            except:
                continue
            # problem_name = text_element[2].__str__()

            # print(title)

            full_url = "https://leetcode.com" + link_element
            # print(full_url)

            xpath_q = ".//div[@class='description__24sA']"

            try:
                driver.get(full_url)
                myElem = WebDriverWait(driver, delay).until(EC.presence_of_element_located((By.XPATH, xpath_q)))
            except :
                continue

            try:
                question_tree = html.fromstring(driver.page_source)
                question_raw = question_tree.xpath("(.//div[@data-key='description-content']/div/div)[2]/div//text()")

                statement = ""
                for clause in question_raw:
                    statement+=clause.__str__()
                
                example_pos = statement.find("Example")

            except:
                continue

            statement = statement[0:example_pos].replace("\xa0",'')
            statement = title + " " + process(statement)

            print(title)
            mydict = {"Title":title,"Statement":statement,"Link":full_url,"Tag":"LC"}
            my_write("./visited/leetcode/leetcode.csv",mydict)


        page+=1

        # if page==10:
        #     break



def main():
    scrape_func("https://leetcode.com/problemset/all/")


if __name__ == "__main__":
    main()