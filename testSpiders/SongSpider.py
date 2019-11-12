from selenium import webdriver
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.common.by import By
import time, os, requests


def spider_song(url):
    # 获取歌曲id
    id = url.split('=')[-1]
    print(id)
    browser = webdriver.Chrome()
    wait = WebDriverWait(browser, timeout=5)
    try:
        browser.get(url)
        iframe = browser.find_element(By.ID, 'g_iframe')
        browser.switch_to.frame(iframe)
        song_name = browser.find_element(By.CSS_SELECTOR, '.f-ff2').text
        print('歌名:' + song_name)
        singer_name = browser.find_element(By.CSS_SELECTOR, '.des span').text
        print('歌手:'+singer_name)
        album_name = browser.find_elements(By.CSS_SELECTOR, '.des a')[1].text
        print('所属专辑:'+album_name)
        lyrics = browser.find_element(By.CSS_SELECTOR, '#lyric-content').text
        lyrics = lyrics.split('展开')[0].strip()
        js = """
            document.querySelector('#flag_ctrl').click(0);
        """
        browser.execute_script(js)
        lyrics2 = browser.find_element(By.CSS_SELECTOR, '#flag_more').text
        lyrics = lyrics+lyrics2
        print(lyrics)
    except Exception as e:
        print(e)
    finally:
        time.sleep(30)
        browser.quit()


spider_song('https://music.163.com/#/song?id=327419')

