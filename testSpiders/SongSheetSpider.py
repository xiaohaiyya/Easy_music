from selenium import webdriver
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.common.by import By
import time, requests, os


#爬虫函数
def spider_song_sheet(url):
    browser = webdriver.Chrome()
    wait = WebDriverWait(browser, timeout=5)
    try:
        browser.get(url)
        iframe = browser.find_element(By.ID, 'g_iframe')
        browser.switch_to.frame(iframe)
        time.sleep(1)
        js_scroll = """
            window.scrollTo(0, 4000)
        """

        for i in range(0, 25):
            browser.execute_script(js_scroll)
            time.sleep(0.2)
        imgs = browser.find_elements(By.CSS_SELECTOR, '.u-cover img')
        results_a = browser.find_elements(By.CSS_SELECTOR, '.dec a')
        results_artic = browser.find_elements(By.CLASS_NAME, 'nm-icn')
        song_sheet_titles = []
        song_sheet_artics = []
        song_sheet_hrefs = []
        for i in range(len(imgs)):
            href = results_a[i].get_attribute('href')
            title = results_a[i].get_attribute('title')
            artic = results_artic[i].get_attribute('title')
            img = imgs[i]
            song_sheet_titles.append(title)
            song_sheet_artics.append(artic)
            song_sheet_hrefs.append(href)
            print(href, title, artic, img.get_attribute('src'))
    except Exception as e:
        print(e)
    finally:
        browser.quit()

spider_song_sheet()

