
#This can be used as follows within a notebook
from webdriverdownloader import ChromeDriverDownloader
cdd = ChromeDriverDownloader()
chromedriver, chromebin = cdd.download_and_install()
 
#If required, the path to the drive can be set explicitly:
from selenium import webdriver
browser = webdriver.Chrome(executable_path=chromebin/chromedriver)
