from selenium import webdriver
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time, requests, os,pymongo
import SongListSpider

#连接MongoDB
client = pymongo.MongoClient(host='127.0.0.1',port=27017)
db = client.MusicApp
p=db.songlist_info


#歌单爬虫函数
def spider_song_sheet(url):
    browser = webdriver.Chrome()
    wait = WebDriverWait(browser, timeout=3)
    try:
        browser.get(url)
        iframe = browser.find_element(By.ID, 'g_iframe')
        browser.switch_to.frame(iframe)
        time.sleep(0.2)
        js_scroll = """
            window.scrollTo(0, 4000)
        """
        for i in range(0, 10):
            browser.execute_script(js_scroll)
            time.sleep(0.2)
        imgs = browser.find_elements(By.CSS_SELECTOR, '.u-cover img')#图片列表
        results_a = browser.find_elements(By.CSS_SELECTOR, '.dec a')#歌单标题列表
        results_artic = browser.find_elements(By.CLASS_NAME, 'nm-icn')#歌单作者列表
        song_sheet_titles = []
        song_sheet_artics = []
        song_sheet_hrefs = []
        for i in range(len(imgs)):
            href = results_a[i].get_attribute('href')#所属歌单连接
            songlist_id =href.split('=')[-1]#所属歌单ID
            title = results_a[i].get_attribute('title')#所属歌单标题
            artic = results_artic[i].get_attribute('title')#所属歌单名字
            img = imgs[i].get_attribute('src')#所属歌单封面链接
            song_sheet_titles.append(title)
            song_sheet_artics.append(artic)
            song_sheet_hrefs.append(href)
            playlist_info=SongListSpider.spider_songlist(href)
            p.update_many({'songlist_id':songlist_id},
                          {'$set':{'songlist_id':songlist_id,
                                   'songlist_href':href,
                                   'songlist_title':title,
                                   'songlist_artic':artic,
                                   'songlist_img':img,
                                   'playlist_introduce':playlist_info[0],
                                   'song_list':playlist_info[1]}},upsert=True)
            print(href, title, artic, img,songlist_id)
    except Exception as e:
        print(e)
    finally:
        browser.quit()

num = 0
for i in range(1,38):
    spider_song_sheet('https://music.163.com/#/discover/playlist/?order=hot&cat=全部&limit=35&offset={}'.format(num))
    num += 35

