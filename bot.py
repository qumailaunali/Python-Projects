from selenium import webdriver

# br = webdriver.Chrome("D:\\Downloads(D)\\webdriver\\chromedriver.exe")
br = webdriver.Edge("D:\\Downloads(D)\\webdriver\\msedgedriver.exe")
br.get("https:/www.facebook.com/")

usr = "sonofaunali@gmail.com"
passw = "luckymob"

user = br.find_element_by_id("email")
user.clear()
user.send_keys(usr)

pasw = br.find_element_by_id("pass")
pasw.send_keys(passw)


butn = br.find_element_by_id('u_0_b')
butn.submit()



# mess = br.find_element_by_class_name("linkWrap noCount")
# mess.click()

