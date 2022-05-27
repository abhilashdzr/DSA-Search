from cgitb import text
import math
from os import stat
from typing import Dict
from attr import field
from lxml import html
import pandas as pd
import re
# import requests
# from bs4 import BeautifulSoup
import time
from requests import request
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
import random

from helpers import *

# #setting limit of questions which a tag must contain to proceed
lim = 10


def scrape_func(URL):
    chrome_options = Options()
    chrome_options.add_argument('--no-sandbox')
    chrome_options.add_argument('--window-size=1920,1080')
    chrome_options.add_argument('--headless')
    chrome_options.add_argument('--disable-gpu')
    chrome_options.add_argument('--disable-dev-shm-usage')
    driver = webdriver.Chrome(options=chrome_options)
    driver.get(URL)

    html_tree=html.fromstring(driver.page_source)
    tagboxes = html_tree.xpath(".//div[@class='problem-tagbox-top']")

    ctr=0

    for i in range(len(tagboxes)):
        #get the tag and count of questions under the tag
        tag_name = html_tree.xpath(f"(.//div[@class='problem-tag problem-tag-overflow actual_tag'])[{i+1}]/text()")[0]
        tag_name = process(tag_name)
        if tag_name in seen_tags:
            continue

        print(f"\n--------------{tag_name}-----------------\n")

        taglink = html_tree.xpath(f"(.//div[@class='problem-tagbox-top'])[{i+1}]/a/@href")[0]
        tag_count = html_tree.xpath(f"(.//div[@class='problem-tagbox-top'])[{i+1}]/div/text()")
        tag_count = tag_count[0].__str__().split('x')[1]
        if "\xa0" in tag_count:
            tag_count = int(tag_count.replace("\xa0",'').strip())

        #if number of problems goes under 10 break | things are in sorted order
        if tag_count<lim:
            driver.close()
            break

        #get into tag
        taglink = "https://codechef.com"+taglink

        try:
            driver.get(taglink)
        except:
            continue


        time.sleep(random.uniform(1,2))
        tree = html.fromstring(driver.page_source)

        questions = tree.xpath(".//div[@class='problem-tagbox-inner']")
        for j in range(len(questions)):
            #get the question box in the tag page
            try:
                href = tree.xpath(f"(.//div[@class='problem-tagbox-headtext'])[{j+1}]/a/@href")[0]
                problem_id = href.split('/')[2]
            
            except:
                continue

            #this are already seen 
            if problem_id in seen_ids:
                    continue
            else:
                seen_ids.append(problem_id)
                
                
            #write the question to csv question column
            dict2 = {'ID':problem_id}
            #Pass the dictionary as an argument to the Writerow()
            my_write("./visited/codechef/id.csv",dict2)
                

            #add domain to get full url
            href = "https://www.codechef.com" + href
            #get into exact question page
            try:
                driver.get(href)

            #question could not be got, so continue
            except:
                continue


            time.sleep(random.randint(1,2))

            problem_tree = html.fromstring(driver.page_source)

            statement = ""

            try:
                title = problem_tree.xpath("(.//div[@class='large-12 columns'])[1]/h1/text()")
                mathjax_elements = problem_tree.xpath("(//div[contains(@class, 'mathjax-support')])//text()")
                for e in mathjax_elements:
                    statement+=e.__str__()


                # print(statement)
                for pos in range(len(statement)):
                    if pos>=len(statement)-2:
                        break  
                    ch = statement[pos]
                    result = ch+ch+ch
                    if statement[pos:pos+3]==result:
                        statement = statement.replace(statement[pos:pos+3],ch)

                #some further processing
                #remove \n \t
                statement = process(statement)
                #remove any read this question in blabla
                if statement.split(" ")[0]=="Read":
                    #split into statements 
                    list_of_sentences = statement.split(".")
                    #remove first sentence
                    statement = statement.replace(list_of_sentences[0],'')

                if statement[:2] == ". ":
                    statement = statement[2:]

                if "Time Limit: " in statement:
                    pos = statement.find("Time Limit:")
                    statement = statement[:pos]

                #check for existence of tags
                exist = 1
                tag_pos = statement.find("Tags: ")

                if tag_pos == -1:
                    exist = -1
                else:
                    end_pos = statement.find("Difficulty",tag_pos)
                    add = ""
                    if end_pos !=-1:
                        add = statement[tag_pos:end_pos]


                input_pos = statement.find("Input")
                statement = statement[:input_pos]
                if exist==1:
                    statement+=add

            except:
                continue

            try:
                title_stripped = title[0].strip()
            except:
                time.sleep(1)
                title = problem_tree.xpath("(.//div[@class='large-12 columns'])[1]/h1/text()")
                try:
                    title_stripped = title[0].strip()
                except:
                    continue

            print(title_stripped)

            #add title to statement
            statement = title_stripped + " " + statement

            my_dict = {"Title":title_stripped,"Statement":statement,"Link":href}
            my_write("./visited/codechef/codechef.csv",my_dict)



        #append this tag to seen tags
        seen_tags.append(tag_name)
        #write tags to seen tags column in csv
        dict1 = {"Tag":tag_name}
        my_write("./visited/codechef/tag.csv",dict1)

    driver.close()


def main():
    scrape_func("https://www.codechef.com/tags/problems")

if __name__ == "__main__":

    try:
        df = pd.read_csv("./visited/codechef/tag.csv")
        seen_tags = df["Tag"].tolist()
    except:
        seen_tags = []

    try:
        df = pd.read_csv("./visited/codechef/id.csv")
        seen_ids = df["ID"].tolist()
    except pd.errors.EmptyDataError:
        seen_ids = []
        

    main()


# < ------------------- END ------------------------------>




