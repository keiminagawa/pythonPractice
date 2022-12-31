# coding:utf-8
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.ui import Select
from selenium import webdriver
from datetime import datetime

import random
import sys
import time
PURPLE = '\033[35m'
RED = '\033[31m'
CYAN = '\033[36m'
OKBLUE = '\033[94m'
OKGREEN = '\033[92m'
WARNING = '\033[93m'
FAIL = '\033[91m'
ENDC = '\033[0m'
UNDERLINE = '\033[4m'

# Selectタグが扱えるエレメントに変化させる為の関数を呼び出す

# ターゲットとなるECサイト・商品一覧１ページ目のURL
URL = 'https://www.amazon.co.jp/s?k=%E5%AE%A3%E4%BC%9D%E4%BC%9A%E8%AD%B0+-%E9%9B%91%E8%AA%8C&i=stripbooks&__mk_ja_JP=%E3%82%AB%E3%82%BF%E3%82%AB%E3%83%8A&crid=CGD49D5PPNUM&qid=1670132237&sprefix=%E5%AE%A3%E4%BC%9D%E4%BC%9A%E8%AD%B0+-%E9%9B%91%E8%AA%8C%2Cstripbooks%2C154&ref=sr_pg_1'

f = open('結果.csv', 'w')
b = webdriver.Chrome()
b.get(URL)
time.sleep(1)
flag = 0

while True:
    classes = b.find_elements_by_class_name(
        "a-link-normal")  # ('a-size-base-plus')
    # print(len(classes))
    for i in list(classes):
        # a = i.find_elements_by_class_name("a-size-base-plus")
        name = str(i.text).replace('\u2014', '')  # a[0].text.replace(',', ''))
        name = name.replace('\u3099', '')
        name = name.replace('\u3299', '')
        name = name.replace('\xae', '')
        url = str(i.get_attribute("href"))
        # print(OKBLUE+UNDERLINE+url+ENDC)
        if name == "" or name == 1 or name == 2 or name == 3:
            continue
        else:
            f.write(name+','+''+url+','+'\n')

    # q = b.find_element_by_class_name('s-pagination-item')
    a = b.find_elements_by_class_name("s-pagination-item")
    for i in a:
        name = str(i.text)
        url = str(i.get_attribute("href"))
        if '次へ' in name:
            flag = 1
            i.click()
        else:
            flag = 0
    if flag == 0:
        break
    else:
        time.sleep(1)
        continue


f.close()
