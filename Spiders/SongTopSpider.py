from selenium import webdriver
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time, requests, os,pymongo
from pymongo import MongoClient

#连接MongoDB
client = pymongo.MongoClient(host='127.0.0.1',port=27017)
db = client.MusicApp
p = db.song_tops


# 爬虫函数
def spider_singer(url, name):
    browser = webdriver.Chrome()
    wait = WebDriverWait(browser, timeout=5)
    try:
        browser.get(url)
        iframe = browser.find_element(By.ID, 'g_iframe')
        browser.switch_to.frame(iframe)
        time.sleep(1)
        js_scroll = """
            window.scrollTo(0, 8000)
        """
        for i in range(0, 25):
            browser.execute_script(js_scroll)
            time.sleep(0.2)
        song_names = browser.find_elements(By.CSS_SELECTOR, '.ttc b')
        singer_names = browser.find_elements(By.CSS_SELECTOR, '.text span')
        song_times = browser.find_elements(By.CSS_SELECTOR, '.u-dur ')
        song_detail = browser.find_elements(By.CSS_SELECTOR, '.ttc a')
        song_list = []
        for i in range(len(song_names)):
            href = song_detail[i].get_attribute('href')
            song_id = href.split('=')[-1]
            song_name = song_names[i].get_attribute('title')
            singer_name = singer_names[i].get_attribute('title')
            song_time = song_times[i].text
            song_download_url = 'http://music.163.com/song/media/outer/url?id={download}.mp3'.format(download=song_id)
            song_dir = {'song_id': song_id, 'song_name': song_name, 'song_time': song_time, 'singer_name': singer_name, 'song_href': href, 'song_download': song_download_url}
            song_list.append(song_dir)

            print(song_id, song_name, singer_name, song_time)
        p.update_many({'top_name': name}, {'$set': {
            'top_name': name,
            'top_url': url,
            'song_list': song_list
        }}, upsert=True)
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
        time.sleep(1)
        frame1 = browser.find_element(By.ID, 'g_iframe')
        browser.switch_to.frame(frame1)
        time.sleep(2)
        js = """
            window.scrollTo(0,8000)
        """
        browser.execute_script(js)
        time.sleep(2)
        Tops_href = browser.find_elements(By.CLASS_NAME, 'avatar')
        Tops_name = browser.find_elements(By.CLASS_NAME, 's-fc0')
        time.sleep(1)
        print(Tops_name)
        for i in range(len(Tops_href)):
            dir_herf = Tops_href[i].get_attribute('href')
            dir_name = Tops_name[i].text
            print(dir_name)
            spider_singer(dir_herf, dir_name)
            time.sleep(1)
            print('----------------------------')

    except Exception as e:
        print(e)


spider_list('https://music.163.com/#/discover/toplist')