from django.test import LiveServerTestCase
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time

class Htest(LiveServerTestCase):
    def testhomepage(self):
        driver=webdriver.Chrome()

        driver.get('http://127.0.0.1:8000/')
        assert "Sign in | eSports Info" in driver.title



class LoginFormTest(LiveServerTestCase):

		def testform(self):
			
				driver = webdriver.Chrome()

				driver.get('http://127.0.0.1:8000/login')

				user_name = driver.find_element("id","inputEmail")
				user_password = driver.find_element("id","inputPassword")

				submit = driver.find_element("id","submit")

				user_name.send_keys('ST')
				user_password.send_keys('ST')

				submit.send_keys(Keys.RETURN)

				assert 'ST' in driver.page_source


class RegFormTest(LiveServerTestCase):

		def testreg(self):
			
				driver = webdriver.Chrome()

				driver.get('http://127.0.0.1:8000/eleague?')

				player_name = driver.find_element("id","epname")
				team_name = driver.find_element("id","etname")
				email_addr = driver.find_element("id","efemail")

				submit = driver.find_element("id","submit")

				player_name.send_keys('Salem')
				team_name.send_keys('NAVI')
				email_addr.send_keys('salem@gmail.com')

				submit.send_keys(Keys.RETURN)

				assert 'Your registration is successful!' in driver.page_source

class teamSearch(LiveServerTestCase):

		def testtsrch(self):
			
				driver = webdriver.Chrome()

				driver.get('http://127.0.0.1:8000/teams?')
				time.sleep(5)

				assert 'Team Liquid' in driver.page_source

class findGame(LiveServerTestCase):

		def testfg(self):
			
				driver = webdriver.Chrome()

				driver.get('http://127.0.0.1:8000/login')

				user_name = driver.find_element("id","inputEmail")
				user_password = driver.find_element("id","inputPassword")

				submit = driver.find_element("id","submit")

				user_name.send_keys('ST')
				user_password.send_keys('ST')

				submit.send_keys(Keys.RETURN)

				assert 'League of Legends' in driver.page_source
