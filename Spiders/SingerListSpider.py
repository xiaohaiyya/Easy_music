from selenium import webdriver
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time, requests


def spider_singerlist(url):
    # 创建一个浏览器对象
    browser = webdriver.Chrome()
    # 设置等待浏览器加载的最长时间
    wait = WebDriverWait(browser, timeout=0.5)
    try:
        browser.get(url)
        time.sleep(0.2)
        frame1 = browser.find_element(By.ID,'g_iframe')
        browser.switch_to.frame(frame1)
        time.sleep(0.2)
        js = """
            window.scrollTo(0,5000)
        """
        a = browser.execute_script(js)
        time.sleep(0.2)
        # 定义Infos存储需要返回的数据（图片链接和歌曲信息）
        Infos = []
        # 获取上一级所需歌手图片
        singer_pic = browser.find_element(By.CSS_SELECTOR, '.n-artist img')
        singer_pic = singer_pic.get_attribute('src')
        Infos.append(singer_pic)
        songs_url = browser.find_elements(By.CSS_SELECTOR, '.ttc span a')
        songs_name = browser.find_elements(By.CSS_SELECTOR, '.ttc span a b')
        songs_time = browser.find_elements(By.CLASS_NAME, 'u-dur ')
        songs_album = browser.find_elements(By.CSS_SELECTOR, '.w4 div a')
        time.sleep(0.2)

        # 定义songInfo存储从歌手歌单链接爬取的数据
        songInfo = []
        for i in range(0, len(songs_url)):
            song_herf = songs_url[i].get_attribute('href')
            song_id = song_herf.split('=')[-1]
            song_name = songs_name[i].get_attribute('title')
            song_time = songs_time[i].text
            song_album = songs_album[i].get_attribute('title')
            song_download_url = 'http://music.163.com/song/media/outer/url?id={}.mp3'.format(song_id)
            one_song = {'song_id': song_id, 'song_name': song_name, 'song_href': song_herf, 'song_time': song_time, 'song_album': song_album, 'song_download_url': song_download_url}
            songInfo.append(one_song)
        Infos.append(songInfo)
        # print(Infos)
        return Infos

        # return Infos
    finally:
        browser.quit()


if __name__ == '__main__':
    spider_singerlist('https://music.163.com/#/artist?id=10559')

