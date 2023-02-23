from selenium import webdriver
from selenium.webdriver.common.by import By
import keyboard
import time

#"https://wvnet.brightspace.com/d2l/le/content/50741/viewContent/2429201/View"

iteration = int(input('How many iterations do you want to run? '))

#website = input('Copy and Paste the chapter you want to start from on BrightSpace: ')

browser = webdriver.Edge()
browser.get("https://wvnet.brightspace.com/d2l/le/content/50741/viewContent/2429201/View")

keyboard.wait("~")
browser.switch_to.window(browser.window_handles[-1])

for i in range(iteration):
    page_source = browser.page_source
    if "Play Video" in page_source:
        play_video_span = browser.find_element(By.XPATH, "//span[contains(text(), 'Play Video')]")
        play_video_span.click()
        time.sleep(20)
        arrow_span = browser.find_element(By.XPATH, "//span[@class='to-icon icon-arrow-right standard']")
        arrow_span.click()
        time.sleep(10)
    else:
        arrow_span = browser.find_element(By.XPATH, "//span[@class='to-icon icon-arrow-right standard']")
        arrow_span.click()
        time.sleep(10)
        
browser.quit()
quit()