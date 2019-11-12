from selenium import webdriver
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.common.by import By
import time, requests, os
from pymongo import MongoClient


# 爬虫函数
def spider_singer(url, name):
    name = name.replace('/', '&')
    browser = webdriver.Chrome()
    wait = WebDriverWait(browser, timeout=5)
    try:
        browser.get(url)
        iframe = browser.find_element(By.ID, 'g_iframe')
        browser.switch_to.frame(iframe)
        time.sleep(1)
        js_scroll = """
            window.scrollTo(0, 8000)
    1    """
        for i in range(0, 25):
            browser.execute_script(js_scroll)
            time.sleep(0.2)
        results = browser.find_elements(By.CLASS_NAME, 'f-thide')
        singer_list = []
        for result in results:
            href = result.get_attribute('href')
            title = result.get_attribute('title')
            title = title.split('的')[0]
            print(title+':'+href)
            singer_list.append(title)
        imgs = browser.find_elements(By.CSS_SELECTOR, '.u-cover img')
        # 文件夹创建
        dir_name = 'img'
        if not os.path.isdir('img'):
            os.makedirs(dir_name)
        # 二级文件夹创建
        dir_name = 'img/{}'.format(name)
        if not os.path.isdir(dir_name):
            os.makedirs(dir_name)
        # 歌手列表下标
        num = 0
        for img in imgs:
            img_url = img.get_attribute('src')
            img_file = requests.get(img_url).content
            with open('./{0}/{1}.jpg'.format(str(dir_name), singer_list[num]), 'wb+') as f:
                f.write(img_file)
            num += 1
    except Exception as e:
        print(e)
    finally:
        browser.quit()


# 需要爬取的列表
def spider_list(url):
    browser = webdriver.Chrome()
    wait = WebDriverWait(browser, timeout=5)
    try:
        browser.get(url)
        frame1 = browser.find_element(By.ID,'g_iframe')
        browser.switch_to.frame(frame1)
        time.sleep(1)
        js = """
            window.scrollTo(0,5000)
        """
        browser.execute_script(js)
        time.sleep(1)
        singers = browser.find_elements_by_class_name('cat-flag')
        time.sleep(1)
        print(singers)
        for singer in singers:
            dir_herf = singer.get_attribute('href')
            dir_name = singer.get_attribute('text')
            spider_singer(dir_herf, dir_name)
            time.sleep(1)
    except Exception as e:
        print(e)


spider_list('https://music.163.com/#/discover/artist')