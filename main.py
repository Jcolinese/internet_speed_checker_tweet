import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.service import Service
from selenium.common.exceptions import NoSuchElementException




PROMISED_DOWN = 150
PROMISED_UP = 10
TWITTER_EMAIL = "YOUR EMAIL"
TWITTER_PASSWORD = "YOUR PASSWORD"
TWITTER_WEBPAGE = "https://twitter.com/login"
SPEED_TEST_PAGE = "https://www.speedtest.net/"
TWITTER_USERNAME = "YOUR USERNAME"

# u need chrome driver installed somewhere and know the location eg /user/YOUR USER NAME/chromedriver!!!
service = Service("CHROMEDRIVER_LOCATION")

class InternetSpeedTwitterBot:
    def __init__(self, driver_path):
        self.driver = webdriver.Chrome(service=driver_path)
        self.up = 0
        self.down = 0
        self.time = time.time() + 60

    def get_internet_speed(self):
        self.driver.get(SPEED_TEST_PAGE)
        self.driver.find_element(By.ID, value="_evidon-banner-acceptbutton").click()
        self.driver.find_element(By.CSS_SELECTOR, value=".js-start-test").click()
        time.sleep(50)
        up = self.driver.find_element(By.CLASS_NAME, value="download-speed")
        down = self.driver.find_element(By.CLASS_NAME, value="upload-speed")
        self.up = up.text
        self.down = down.text
        print(f"Upload = {self.up}")
        print(f"Download = {self.down}")


    def tweet_at_provider(self):
        self.driver.get(TWITTER_WEBPAGE)
        time.sleep(3)

        click_mail = self.driver.find_element(By.XPATH, '//*[@id="layers"]/div/div/div/div/div/div/div[2]/div[2]/div/div/div[2]/div[2]/div[1]/div/div/div[5]/label/div/div[2]/div')
        click_mail.click()
        time.sleep(3)
        enter_mail = self.driver.find_element(By.XPATH, '//*[@id="layers"]/div/div/div/div/div/div/div[2]/div[2]/div/div/div[2]/div[2]/div[1]/div/div/div[5]/label/div/div[2]/div/input')
        enter_mail.send_keys(TWITTER_EMAIL)
        time.sleep(3)
        enter_mail.send_keys(Keys.ENTER)
        time.sleep(3)
        
        # if NoSuchElementException twitter brought up a box saying enter username or phone number if this dosent come up just comment it out!!
        time.sleep(3)
        # username_checker!! need to make dynamic!!!
        usr_nm = self.driver.find_element(By.XPATH, '/html/body/div/div/div/div[1]/div/div/div/div/div/div/div[2]/div[2]/div/div/div[2]/div[2]/div[1]/div/div[2]/label/div/div[2]/div/input')
        usr_nm.send_keys(TWITTER_USERNAME)
        usr_nm.send_keys(Keys.ENTER)
        time.sleep(3)
        
        # Password
        enter_pw = self.driver.find_element(By.XPATH, '/html/body/div/div/div/div[1]/div/div/div/div/div/div/div[2]/div[2]/div/div/div[2]/div[2]/div[1]/div/div/div[3]/div/label/div/div[2]/div[1]/input')
        enter_pw.send_keys(TWITTER_PASSWORD)
        enter_pw.send_keys(Keys.ENTER)

        # Accept cookies
        time.sleep(3)
        click_cookie = self.driver.find_element(By.XPATH, '//*[@id="layers"]/div/div/div/div/div/div[2]/div[1]')
        click_cookie.click()

        # Send Tweet
        time.sleep(3)
        start_tweet = self.driver.find_element(By.XPATH, '//*[@id="react-root"]/div/div/div[2]/header/div/div/div/div[1]/div[3]/a')
        start_tweet.click()
        write_tweet = self.driver.find_element(By.XPATH, '//*[@id="layers"]/div[2]/div/div/div/div/div/div[2]/div[2]/div/div/div/div[3]/div/div[1]/div/div/div/div/div[2]/div[1]/div/div/div/div/div/div/div/div/div/label/div[1]/div/div/div/div/div/div/div')
        # write_tweet.click()
        time.sleep(2)
        Message = f"Upload speed: {self.up}\n" \
                  f"Download speed: {self.down}"
        write_tweet.send_keys(Message)
        time.sleep(2)
        send_tweet = self.driver.find_element(By.XPATH, '/html/body/div[1]/div/div/div[1]/div[2]/div/div/div/div/div/div[2]/div[2]/div/div/div/div[3]/div/div[1]/div/div/div/div/div[2]/div[3]/div/div/div[2]/div[4]')
        send_tweet.click()

bot = InternetSpeedTwitterBot(service)
bot.get_internet_speed()
bot.tweet_at_provider()
