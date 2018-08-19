from selenium import webdriver
import time
from selenium.webdriver.support.select import Select

class DropdownSelect():

    def test(self):
        baseUrl = "https://letskodeit.teachable.com/pages/practice"
        driver = webdriver.Firefox()
        driver.maximize_window()
        driver.get(baseUrl)
        driver.implicitly_wait(10)

        element = driver.find_element_by_id("carselect")
        sel = Select(element)

        sel.select_by_value("benz")
        print("Select Benz by value")
        time.sleep(2)

        sel.select_by_index("2") # DON'T ACTUALLY NEED TO USE "" AROUND 2.  SEE BELOW.
        print("Select Honda by index")
        time.sleep(2)

        sel.select_by_visible_text("BMW")
        print("Select BMW by visible text")
        time.sleep(2)

        sel.select_by_index(2) # IN THIS EXAMPLE, WE USE 2 WITHOUT THE "" AND IT WORKS FINE.
        print("Select Honda by index")


ff = DropdownSelect()
ff.test()
