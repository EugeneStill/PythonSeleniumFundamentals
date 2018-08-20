# {0} is a placeholder and the actual value that will be used is passed in by .format()
# EG: def selectCourseToEnroll(self, fullCourseName):
#     self.elementClick(locator=self._course.format(fullCourseName), locatorType="xpath")
_course = "//div[contains(@class,'course-listing-title') and contains(text(),'{0}')]"

_enroll_disabled = "//div[@class='spc__primary-submit is-disabled']"

//div[contains(text(),'Invalid email or password')]

//div[@id='navbar']//a[@href='/sign_out']

//*[@class='gravatar']

@ FindBy(xpath = "//button[contains(text(),'Go')]")
WebElement goButton;

@ FindBy(xpath = "//h3[contains(text(),'Oh no!')]")
WebElement outOfAreaModal;

@ FindBy(xpath = "//p[@role='alert']")
WebElement pTagError;

@ FindBy(xpath = "//iframe[@name='__privateStripeFrame4']")
WebElement iFrameCard;

@ FindBy(xpath = "//iframe[@name='__privateStripeFrame5']")
WebElement iFrameExp;

@ FindBy(xpath = "//iframe[@name='__privateStripeFrame6']")
WebElement iFrameCvc;

@ FindBy(xpath = "//iframe[@name='__privateStripeFrame7']")
WebElement iFrameZip;

@ FindBy(xpath = "//button[contains(text(),'Start Membership')]")
WebElement startButton;

# Example of using a variable value inside xpath
WebElement result = driver.findElement(By.xpath("//td[text()='" + req + "']"));