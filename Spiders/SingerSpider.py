from selenium import webdriver
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.common.by import By
import time, requests, os

import SingerListSpider

from pymongo import MongoClient
client = MongoClient('localhost', 27017)
db = client.MusicApp
collection = db.singer_info


# 爬虫函数
def spider_singer(url, kinds):
    for kind in kinds:
        singer_kind = kind.replace('/', '&')
    browser = webdriver.Chrome()
    wait = WebDriverWait(browser, timeout=0.5)
    try:
        browser.get(url)
        iframe = browser.find_element(By.ID, 'g_iframe')
        browser.switch_to.frame(iframe)
        time.sleep(0.2)
        js_scroll = """
            window.scrollTo(0, 8000)
    1    """
        for i in range(0, 25):
            browser.execute_script(js_scroll)
            time.sleep(0.2)
        results = browser.find_elements(By.CLASS_NAME, 'f-thide')
        for result in results:
            # 获取歌手歌单链接
            singer_song_list = result.get_attribute('href')
            # 调用爬取歌手歌单链接的爬虫
            # 获取歌手链接
            singer_id = singer_song_list.split('=')[-1]
            singer_name = result.get_attribute('title').split('的')[0]
            # 接收返回数据
            Infos = SingerListSpider.spider_singerlist(singer_song_list)
            print(Infos)
            # print(singer_id, singer_name, singer_song_list, singer_kind, SingerListSpider.spider_singerlist(singer_song_list))
            collection.update_many({'singer_id': singer_id}, {'$set': {
                'singer_id': singer_id,
                'singer_name': singer_name,
                'singer_kind': singer_kind,
                'singer_pic': Infos[0],
                'singer_song_list': Infos[1]
            }}, upsert=True)

    except Exception as e:
        print(e)
    finally:
        browser.quit()


# 需要爬取的列表
def spider_list(url):
    browser = webdriver.Chrome()
    wait = WebDriverWait(browser, timeout=0.5)
    try:
        browser.get(url)
        frame1 = browser.find_element(By.ID,'g_iframe')
        browser.switch_to.frame(frame1)
        time.sleep(0.2)
        js = """
            window.scrollTo(0,5000)
        """
        browser.execute_script(js)
        time.sleep(0.2)
        singers = browser.find_elements_by_class_name('cat-flag')
        time.sleep(1)
        # 一个歌手可以分属多个分类
        kinds = []
        for i in range(2,len(singers)):
            dir_herf = singers[i].get_attribute('href')
            kinds.append(singers[i].get_attribute('text'))
            spider_singer(dir_herf, kinds)
            time.sleep(0.2)
    except Exception as e:
        print(e)


spider_list('https://music.163.com/#/discover/artist/cat?id=1001')