from selenium import webdriver
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time,requests

def spider_songlist(url):
    #创建一个浏览器对象
    browser = webdriver.Chrome()
    #设置等待浏览器加载的最长时间
    wait = WebDriverWait(browser,timeout=10)
    try:
        browser.get(url)
        time.sleep(1)
        frame1 = browser.find_element(By.ID,'g_iframe')
        browser.switch_to.frame(frame1)
        time.sleep(1)
        js = """
            window.scrollTo(0,5000)
        """
        a = browser.execute_script(js)
        time.sleep(1)
        playlist_name = browser.find_element(By.CSS_SELECTOR,'.f-ff2').text
        print(playlist_name)
        playlist_author_name = browser.find_element(By.CSS_SELECTOR, '.s-fc7').text
        print(playlist_author_name)
        playlist_introduce = browser.find_element(By.ID,'album-desc-more').text
        print(playlist_introduce)
        songs_url = browser.find_elements(By.CSS_SELECTOR, '.ttc span a')
        songs_name = browser.find_elements(By.CSS_SELECTOR, '.ttc span a b')
        singers_name = browser.find_elements(By.CSS_SELECTOR,'.text span')
        songs_time = browser.find_elements(By.CLASS_NAME, 'u-dur ')
        songs_album = browser.find_elements(By.CSS_SELECTOR,'.text>a')
        print(len(songs_time))
        time.sleep(1)
        for i in range(0, len(songs_url)):
            song_herf = songs_url[i].get_attribute('href')
            song_name = songs_name[i].get_attribute('title')
            singer_name = singers_name[i].get_attribute('title')
            song_time = songs_time[i].text
            song_album = songs_album[i].get_attribute('title')
            print(song_name, song_herf,song_time,singer_name,song_album)
        time.sleep(1)

    finally:
        browser.quit()
spider_songlist('https://music.163.com/#/playlist?id=2993162734')

