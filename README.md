# SeleniumAutomation
Four short scripts written in Python that automate different login processes for Hudl.com. These scripts use the Selenium webdriver for Google Chrome.

# Files 
login.py: validates whether a user has entered a valid username and password

organization_login.py: validates that, from the individual login page, a user can navigate to the page that allows them to login with an organization

signup.py: validates that a user can navigate to the signup page from the the login page

needhelp.py: validates that a user can navigate to the "Need help" page from the login page

# Notes
In each file, the service variable `ser` will need to be changed to the pathname of the chromedriver on your machine. 

# Known Errors/Bugs
login.py: the "if-else" block does not print out the "Login failed" message when the wrong credentials are entered
