from bot import *

driver = initialize()

try:
    go_to_login_page(driver)
except:
    go_to_login_page_alternative(driver)
time.sleep(1)
insert_email(driver, '+96555159647')
time.sleep(0.8)
insert_password(driver, '3&4hsk@#MN')
time.sleep(0.7)
find_person(driver, 'xBrendan')
try:
    follow_person(driver)
except:
    pass
# quit(driver)