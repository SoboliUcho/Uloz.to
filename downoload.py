import os
import random
from telnetlib import EC
import time
import requests
from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.firefox.options import Options
from selenium.webdriver.firefox.firefox_profile import FirefoxProfile
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import NoSuchElementException


class scraper:
    def __init__(self) -> None:
        options = Options()
        # chrome_profile =
        firefox_profile = FirefoxProfile(
            "C:/Users/sobol/AppData/Roaming/Mozilla/Firefox/Profiles/sxf74908.default-release"
        )
        # firefox_profile.profile_dir("C:/Users/sobol/AppData/Roaming/Mozilla/Firefox/Profiles/sxf74908.default-release")
        options.profile = firefox_profile
        options.add_argument("user-agent=your_user_agent_string")
        self.driver = webdriver.Firefox(options=options)

    def quitdriver(self):
        self.driver.quit()


class page:
    def __init__(self, driver, odkaz) -> None:
        self.odkaz = odkaz
        self.page = ""
        self.driver = driver
        self.webdriver_path = "geckodriver.exe"

    def scrappage(self):
        response = requests.get(self.odkaz)
        soup = BeautifulSoup(response.content, "html.parser")
        print(soup)
        if response.status_code == 200:
            self.page = response

    def opendriver(self):
        pass

    def make_action(self):
        # random.uniform(100, 500)
        # driver.driver.set_window_size(random.uniform(100, 500), random.uniform(100, 500))
        self.driver.driver.get(self.odkaz)
        # link = driver.find_element(By.CSS_SELECTOR, '.js-fast-download-button-dialog')
        # wait = WebDriverWait(self.driver.driver, timeout=1)
        # time.sleep(2)
        while True:
            try:
                name = self.driver.driver.find_element(
                    By.CSS_SELECTOR, ".jsFileTitle"
                ).text
                break
            except NoSuchElementException:
                time.sleep(1)
                # self.driver.driver.get(self.odkaz)

        while True:
            try:
                link = WebDriverWait(driver.driver, 10).until(
                    EC.element_to_be_clickable((By.CSS_SELECTOR, ".c-button"))
                )
                # link = self.driver.driver.find_element(By.CSS_SELECTOR, ".c-button")
                driver.execute_script("arguments[0].scrollIntoView(true);", link)
                break
            except NoSuchElementException:
                time.sleep(1)
                # self.driver.driver.get(self.odkaz)

        name = name.replace('<span class="jsFileNameNoExt">', "")
        name = name.replace("</span>", "")

        linkurl = link.get_property("href")
        if linkurl != "/koupit-disk":
            link.click()
            # response = requests.get()
            # if response.status_code == 200:
            # with open("downoald/"+name, 'wb') as file:
            #     file.write(response.content)
        # delay = random.uniform(1, 3)
        # time.sleep(delay)


class searchpage:
    def __init__(self, url) -> None:
        self.url = url
        self.driver = scraper()
        self.olditems = []
        self.action = ActionChains(self.driver.driver)

        # self.vysledky = []

    def load_page(self):
        self.driver.driver.get(self.url)
        WebDriverWait(self.driver.driver, 10).until(
            EC.presence_of_element_located((By.CSS_SELECTOR, ".ctizlv"))
        )

    def vysledky(self):
        vysledky = []
        links = self.driver.driver.find_elements(By.CSS_SELECTOR, ".ctizlv")
        for link in links:
            if link not in self.olditems:
                # print(link)
                vysledky.append(link.get_property("href"))
                self.olditems.append(link)
        self.action.send_keys(Keys.PAGE_DOWN).perform()
        return vysledky


class knihovna:
    def __init__(self, url) -> None:
        self.driver = scraper()
        self.driver.driver.get(url)
        self.action = ActionChains(self.driver.driver)
        self.oldbook=[]

    def load_page(self):
        # WebDriverWait(self.driver.driver, 10).until(
        #     EC.presence_of_element_located((By.CSS_SELECTOR, 'button[data-testid="btn-action-download"]'))
        # )

        try:
            downald = self.driver.driver.find_elements(
                By.CSS_SELECTOR, 'button.ant-btn.ant-btn-text.ant-btn-sm.ant-btn-icon-only.styled__StyledButton-lkgLeC.fKlesU.c-button.styled__ActionButton-dteRlL.kkMmYD'
            )
            for dovnald in downald:
                if dovnald not in self.oldbook:
                    dovnald.click()
                    self.oldbook.append(dovnald)
            time.sleep(1)
        except NoSuchElementException:
            time.sleep(1)

    def next_page(self):
        next_button = WebDriverWait(self.driver.driver, 10).until(
            EC.presence_of_element_located(
                (By.CSS_SELECTOR, 'div[data-testid="next-file"]')
            )
        )
        next_button.click()

    def submit_but(self):
         while True:
            try:
                sub_button = self.driver.driver.find_element(
                    By.CSS_SELECTOR,
                    "button.ant-btn.ant-btn-primary.ant-btn-sm.styled__StyledButton-lkgLeC.fKlesU.c-button",
                )
                sub_button.click()
            except NoSuchElementException:
                continue
    def page_down(self):
        self.action.send_keys(Keys.PAGE_DOWN).perform()

knihov = knihovna(
    "https://uloz.to/shared/folder/LD0MaUfoJSeS?sort=name#!ZJLlLGR2ZmywBJSyMJV1BJRmLJD2MyAyH0cnGKWFo2t3EGx3MD=="
)
while True:
    knihov.load_page()
    knihov.submit_but()
    knihov.page_down()
# spage = searchpage("https://gozofinder.com/cse/ulozto/cz?query=ace-+epub+zip")
# with open("vystup.txt", "r") as souborr:
#     vystup= []
#     for radek in souborr:
#         radek.strip()
#         radek = radek.rstrip()
#         vystup.append(radek)
#     spage.olditems = vystup
# spage.load_page()
# driver = scraper()

# # for i in range(1):
# while True:
#     # spage.vysledky()
#     vysledky = spage.vysledky()
#     print(vysledky)
#     with open("vystup.txt", "w") as soubor:
#         for vasledek in vysledky:
#             npage=page(driver,vasledek)
#             npage.make_action()
#             soubor.write(str(vasledek)+ "\n")
# <div data-testid="next-file" class="styled__StyledArrowButton-fgAuXX MtDcH styled__StyledArrows-hBwmle btWvdD"><span role="img" class="anticon styled__ArrowNext-kONSEp ehnVgk" style="width: 1em; min-width: 1em; height: 1em; display: inline-flex;"><svg viewBox="31.95 72.08 208.12 367.98" xmlns="http://www.w3.org/2000/svg"><path fill="currentColor" d="M233 239c9.4 9.4 9.4 24.6 0 33.9L73 433c-9.4 9.4-24.6 9.4-33.9 0s-9.4-24.6 0-33.9l143-143L39 113c-9.4-9.4-9.4-24.6 0-33.9s24.6-9.4 33.9 0L233 239z"></path></svg></span></div>
