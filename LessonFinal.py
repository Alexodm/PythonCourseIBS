from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys


options = Options()
options.add_argument("start-maximized")
driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=options)
driver.get("http://google.com/ncr")


elm = driver.find_element(by=By.NAME, value='q')
elm.send_keys('selenide')
elm.send_keys(Keys.ENTER)
elm = driver.find_element(by=By.CSS_SELECTOR, value="body.srp:nth-child(2) div.main:nth-child(13) div.e9EfHf div.GyAeWb:nth-child(12) div.s6JM6d div.eqAnXb:nth-child(3) div.v7W49e div.g:nth-child(1) div.BYM4Nd div.eKjLze div.g div:nth-child(2) div.tF2Cxc div.yuRUbf > a:nth-child(1)")
first_elm = elm.get_property("href")
assert first_elm == "https://selenide.org/"


elm = driver.find_element(by=By.XPATH, value="//body/div[@id='main']/div[@id='cnt']/div[@id='top_nav']/div[@id='hdtb']/div[@id='pTwnEc']/div[@id='hdtb-msb']/div[1]/div[1]/div[2]/a[1]")
elm.click()
elm = driver.find_element(by=By.XPATH, value="//body/div[2]/c-wiz[1]/div[3]/div[1]/div[1]/div[1]/div[1]/div[1]/div[1]/span[1]/div[1]/div[1]/div[1]/a[1]/div[1]/img[1]")
assert "Selenide" in elm.get_property("alt")

elm = driver.find_element(by=By.XPATH, value="//body/div[2]/c-wiz[1]/div[1]/div[1]/div[1]/div[1]/div[1]/div[1]/a[1]")
elm.click()

second_elm = driver.find_element(By.CSS_SELECTOR, value="body.srp:nth-child(2) div.main:nth-child(13) div.e9EfHf div.GyAeWb:nth-child(12) div.s6JM6d div.eqAnXb:nth-child(3) div.v7W49e div.g:nth-child(1) div.BYM4Nd div.eKjLze div.g div:nth-child(2) div.tF2Cxc div.yuRUbf > a:nth-child(1)")
second_elm = second_elm.get_property("href")
assert first_elm == second_elm

driver.close()

