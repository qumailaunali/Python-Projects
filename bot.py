from selenium import webdriver

# br = webdriver.Chrome("D:\\Downloads(D)\\webdriver\\chromedriver.exe")
br = webdriver.Edge("D:\\Downloads(D)\\webdriver\\msedgedriver.exe")
br.get("https:/www.facebook.com/")

user_email= input("Enter your email : ")
user_pass = input("Enter your password : ")
usr = user_email
passw = user_pass

user = br.find_element_by_id("email")
user.clear()
user.send_keys(usr)

pasw = br.find_element_by_id("pass")
pasw.send_keys(passw)


butn = br.find_element_by_id('u_0_b')
butn.submit()



# mess = br.find_element_by_class_name("linkWrap noCount")
# mess.click()

