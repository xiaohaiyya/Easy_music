from selenium import webdriver
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.common.by import By
import time, requests, os


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
        song_names_list = []
        singer_names_list = []
        song_hrefs_list = []
        song_time_list = []
        for i in range(len(song_names)):
            href = song_detail[i].get_attribute('href')
            song_name = song_names[i].get_attribute('title')
            singer_name = singer_names[i].get_attribute('title')
            song_time = song_times[i].text
            song_names_list.append(song_name)
            singer_names_list.append(singer_name )
            song_hrefs_list.append(href)
            song_time_list.append(song_time)
            print(href, song_name, singer_name, song_time)
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
        Tops = browser.find_elements(By.CLASS_NAME, 'avatar')
        time.sleep(1)
        print(Tops)
        for Top in Tops:
            dir_herf = Top.get_attribute('href')
            dir_name = Top.get_attribute('alt')
            spider_singer(dir_herf, dir_name)
            time.sleep(1)
            print('----------------------------')
    except Exception as e:
        print(e)


spider_list('https://music.163.com/#/discover/toplist')