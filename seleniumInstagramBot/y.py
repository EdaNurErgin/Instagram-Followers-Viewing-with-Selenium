
from instagramUserInfo import username,password
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time

class Instagram:
    def __init__(self,username,password):
        self.browser = webdriver.Chrome()
        self.username=username
        self.password=password

    def signIn(self):
        self.browser.get("https://www.instagram.com/accounts/login/")
        time.sleep(10)
        usernameInput=self.browser.find_element(By.XPATH,"//*[@id='loginForm']/div/div[1]/div/label/input")
        passwordInput=self.browser.find_element(By.XPATH,"//*[@id='loginForm']/div/div[2]/div/label/input")


        # Python'da Selenium kütüphanesi ile kullanılan
        # .send_keys() metodu,
        # bir web elementine klavye ile yazı yazma işlevini yerine getirir. Örneğin, bir form alanına ya da arama kutusuna metin girişi yapmak için kullanılır. Bu metot, tarayıcıda aktif olan web sayfasındaki bir elemente karakterler gönderir ve simüle edilmiş bir
        #  klavye girişi gerçekleştirir.


        usernameInput.send_keys(self.username)
        passwordInput.send_keys(self.password)
        passwordInput.send_keys(Keys.ENTER)
        time.sleep(10)

    def getFollowers(self):
        self.browser.get(f"https://www.instagram.com/{self.username}")
        time.sleep(2)
        
        followersLink = self.browser.find_element(By.CSS_SELECTOR, "ul > li:nth-child(2) > div > a")
        print("0")
        followersLink.click()
        time.sleep(5)
        
        
        kullanicilar=[]
        followers1 = self.browser.find_element(By.CSS_SELECTOR, " body > div.xnkg4db.xwsalez.x13ywhbb.x178cd7z.x1n2onr6.xzkaem6 > div:nth-child(2) > div > div > div.x9f619.x1n2onr6.x1ja2u2z > div > div.x1uvtmcs.x4k7w5x.x1h91t0o.x1beo9mf.xaigb6o.x12ejxvf.x3igimt.xarpa2k.xedcshv.x1lytzrv.x1t2pt76.x7ja8zs.x1n2onr6.x1qrby5j.x1jfb8zj > div > div > div > div > div.x7r02ix.xf1ldfh.x131esax.xdajt7p.xxfnqb6.xb88tzc.xw2csxc.x1odjw0f.x5fp0pe > div > div > div.xyi19xy.x1ccrb07.xtf3nb5.x1pc53ja.x1lliihq.x1iyjqo2.xs83m0k.xz65tgg.x1rife3k.x1n2onr6").find_elements(By.CSS_SELECTOR,".x1dm5mii.x16mil14.xiojian.x1yutycm.x1lliihq.x193iq5w.xh8yej3")
        print("1")
        for x in followers1:
            kullanicilar.append(x.text)
        print(kullanicilar)


        # Sayfa ilk yuklendigindeki scroll  boyu uzunlugu
        endHeight =self.browser.execute_script("return document.querySelector('.x7r02ix.xf1ldfh.x131esax.xdajt7p.xxfnqb6.xb88tzc.xw2csxc.x1odjw0f.x5fp0pe').scrollHeight;")
        print("2")
        while True:
            # scrollbari her hareket ettirdigimzdeki uzunlugu
            self.browser.execute_script("document.querySelector('.xyi19xy.x1ccrb07.xtf3nb5.x1pc53ja.x1lliihq.x1iyjqo2.xs83m0k.xz65tgg.x1rife3k.x1n2onr6').scroll(0,document.querySelector('.xyi19xy.x1ccrb07.xtf3nb5.x1pc53ja.x1lliihq.x1iyjqo2.xs83m0k.xz65tgg.x1rife3k.x1n2onr6').scrollHeight)")
            print("3")
            time.sleep(5)
            followers2 = self.browser.find_element(By.CSS_SELECTOR, " body > div.xnkg4db.xwsalez.x13ywhbb.x178cd7z.x1n2onr6.xzkaem6 > div:nth-child(2) > div > div > div.x9f619.x1n2onr6.x1ja2u2z > div > div.x1uvtmcs.x4k7w5x.x1h91t0o.x1beo9mf.xaigb6o.x12ejxvf.x3igimt.xarpa2k.xedcshv.x1lytzrv.x1t2pt76.x7ja8zs.x1n2onr6.x1qrby5j.x1jfb8zj > div > div > div > div > div.x7r02ix.xf1ldfh.x131esax.xdajt7p.xxfnqb6.xb88tzc.xw2csxc.x1odjw0f.x5fp0pe > div > div > div.xyi19xy.x1ccrb07.xtf3nb5.x1pc53ja.x1lliihq.x1iyjqo2.xs83m0k.xz65tgg.x1rife3k.x1n2onr6").find_elements(By.CSS_SELECTOR,".x1dm5mii.x16mil14.xiojian.x1yutycm.x1lliihq.x193iq5w.xh8yej3")
            print("4")
            for i in followers2:
                m=i.text
                if m not in kullanicilar:
                    kullanicilar.append(m)
            # scrolu  eniden olctuk
            newHeight= self.browser.execute_script("return document.querySelector('.xyi19xy.x1ccrb07.xtf3nb5.x1pc53ja.x1lliihq.x1iyjqo2.xs83m0k.xz65tgg.x1rife3k.x1n2onr6').scrollHeight;")
            print("5")
            if endHeight==newHeight :
                break
            endHeight=newHeight

        sayac=0
        for k in kullanicilar:
            sayac+=1
        print("f{sayac}-{k}")
        print(kullanicilar)



        


instgrm = Instagram(username, password)
instgrm.signIn()
instgrm.getFollowers()