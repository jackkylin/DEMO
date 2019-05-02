#By the by, there is also a Python package for installing geckodriver
!pip install --no-cache webdriverdownloader
#This can be used as follows within a notebook
from webdriverdownloader import GeckoDriverDownloader
gdd = GeckoDriverDownloader()
geckodriver, geckobin = gdd.download_and_install("v0.23.0")

#If required, the path to the drive can be set explicitly:
from selenium import webdriver
from selenium.webdriver.firefox.options import Options
 
options = Options()
options.headless = True
 
driver = webdriver.Firefox(options=options)
#driverdriver = webdriver.Firefox(executable_path=geckobin, options=options)
