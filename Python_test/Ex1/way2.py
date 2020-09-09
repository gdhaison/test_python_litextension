from selenium import webdriver

# open browser and login
driver = webdriver.Chrome()
driver.get('http://45.79.43.178/source_carts/wordpress/wp-login.php')
input_name = driver.find_element_by_id("user_login").send_keys("admin")
input_pass = driver.find_element_by_id("user_pass").send_keys("123456aA")
driver.find_element_by_id("wp-submit").click()

# print name of user
print(driver.find_element_by_class_name("display-name").text)
