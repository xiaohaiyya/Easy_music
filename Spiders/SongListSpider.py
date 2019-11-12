from selenium import webdriver
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time,requests,pymongo



def spider_songlist(url):
    #创建一个浏览器对象
    browser = webdriver.Chrome()
    #设置等待浏览器加载的最长时间
    wait = WebDriverWait(browser,timeout=3)
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
        playlist_info = []
        songs_info=[]
        playlist_name = browser.find_element(By.CSS_SELECTOR,'.f-ff2').text
        print(playlist_name)
        playlist_author_name = browser.find_element(By.CSS_SELECTOR, '.s-fc7').text
        print(playlist_author_name)
        playlist_introduce = browser.find_element(By.CSS_SELECTOR,'.cntc p').text
        playlist_introduce=playlist_introduce.replace('\n','')
        playlist_info.append(playlist_introduce)
        print(playlist_info)
        songs_url = browser.find_elements(By.CSS_SELECTOR, '.ttc span a')
        songs_name = browser.find_elements(By.CSS_SELECTOR, '.ttc span a b')
        singers_name = browser.find_elements(By.CSS_SELECTOR,'.text span')
        songs_time = browser.find_elements(By.CLASS_NAME, 'u-dur ')
        songs_album = browser.find_elements(By.CSS_SELECTOR,'.text>a')

        print(len(songs_time))
        time.sleep(0.2)
        for i in range(0, len(songs_url)):
            song_herf = songs_url[i].get_attribute('href')#歌曲链接
            song_id = song_herf.split('=')[-1]#歌曲id
            song_download_url = 'http://music.163.com/song/media/outer/url?id={}.mp3'.format(song_id)#下载链接
            song_name = songs_name[i].get_attribute('title')#歌曲名字
            singer_name = singers_name[i].get_attribute('title')#歌手名字
            song_time = songs_time[i].text#歌曲时长
            song_album = songs_album[i].get_attribute('title')#歌曲专辑
            song_info = {'song_name':song_name,'song_id':song_id,'song_download_url':song_download_url,'song_href':song_herf,'singer_name':singer_name,'song_time':song_time,'song_album':song_album}
            songs_info.append(song_info)
            print(song_name, song_herf,song_time,singer_name,song_album,song_download_url)
        time.sleep(0.2)
        playlist_info.append(songs_info)
        return playlist_info


    finally:
        browser.quit()
if __name__ == '__main__':
    spider_songlist('https://music.163.com/#/playlist?id=2999948129')

