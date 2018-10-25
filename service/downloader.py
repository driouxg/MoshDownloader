import urllib3
from bs4 import BeautifulSoup
import certifi
from robobrowser import RoboBrowser
import configparser


class Downloader:

    def __init__(self):
        self.http = urllib3.PoolManager(cert_reqs='CERT_REQUIRED', ca_certs=certifi.where())

    def scrape_html(self, url):
        self.login()

        response = self.http.request('GET', url)
        return BeautifulSoup(response.data, features="html.parser")

    def login(self):
        credentials = self.get_credentials()

        browser = RoboBrowser()
        login_url = 'https://sso.teachable.com/secure/146684/users/sign_in?flow_school_id=146684'
        browser.open(login_url)
        form = browser.get_form(id='new_user')
        form['user[email]'].value = credentials[0]
        form['user[password]'].value = credentials[1]
        browser.submit_form(form)

        browser.open("https://codewithmosh.com/courses/357787/lectures/5634517")

        print(browser.find())

    def get_credentials(self):
        config = configparser.ConfigParser()
        config.read('resources/auth.ini')

        return list(map(lambda x: config['CREDENTIALS'][x], config['CREDENTIALS']))
