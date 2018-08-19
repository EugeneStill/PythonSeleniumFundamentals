from selenium import webdriver
import os

class RunIETests():

    def test(self):
        # driverLocation = "C:\\Users\\Anil Tomar\\PycharmProjects\\libs\\IEDriverServer.exe"
        # os.environ["webdriver.ie.driver"] = driverLocation
        # driver = webdriver.Ie(driverLocation)
        driver = webdriver.Ie()
        driver.get("http://www.letskodeit.com")

ieTest = RunIETests()
ieTest.test()