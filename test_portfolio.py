import os
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities

def test_consecutively():
    driver_admin = webdriver.chrome()
    driver_admin.get("http://localhost:8000/admin/")

    driver_projects = webdriver.Chrome()
    driver_projects.get("http://localhost:8000/projects/")

    driver_blog = webdriver.Chrome()
    driver_blog.get("http://localhost:8000/blog/")

    
test_consecutively()

### Login ###

def test_login():
    driver.get("http://localhost:8000/admin")
    assert "Django" in driver.title

    username = driver.find_element_by_name("username")
    username.clear()
    username.send_keys("user1")

    password = driver.find_element_by_name("password")
    password.clear()
    password.send_keys("user1pw234")

    driver.find_element_by_xpath("//input[@type='submit' and @value='Log in']").click()
    assert "Please ensure username & password is correct" not in driver.page_source
    driver.close()

test_login():

def test_adminLogin():
    driver.get("http://localhost:8000/admin")
    assert "Django" in driver.title

    username = driver.find_element_by_name("username")
    username.clear()
    username.send_keys("tanjunhong")

    password = driver.find_element_by_name("password")
    password.clear()
    password.send_keys("22Y69u96")

    driver.find_element_by_xpath("//input[@type='submit' and @value='Log in']").click()

test_adminlogin()

### Comment ###

### Category ###

def test_addCCA():
    driver.get("http://localhost:8000/admin")
    assert "Django" in driver.title

    username = driver.find_element_by_name("username")
    username.clear()
    username.send_keys("userabc1")

    password = driver.find_element_by_name("password")
    password.clear()
    password.send_keys("abc1234567@")

    driver.find_element_by_xpath("//input[@type='submit' and @value='Log in']").click()

    driver.find_element_by_link_text("Categorys").click()

    driver.find_element_by_class_name("addlink").click()

    addCategory = driver.find_element_by_name("name")
    addCategory.clear()
    addCategory.send_keys("CCA Activities")

    driver.find_element_by_xpath("//input[@type='submit' and @value='Save']").click()


test_test_addCCA()


def test_addProjects():
    driver.get("http://localhost:8000/admin")
    assert "Django" in driver.title

    username = driver.find_element_by_name("username")
    username.clear()
    username.send_keys("userabc1")

    password = driver.find_element_by_name("password")
    password.clear()
    password.send_keys("abc1234567@")

    driver.find_element_by_xpath("//input[@type='submit' and @value='Log in']").click()

    driver.find_element_by_link_text("Categorys").click()

    driver.find_element_by_class_name("addlink").click()

    addCategory = driver.find_element_by_name("name")
    addCategory.clear()
    addCategory.send_keys("Projects")

    driver.find_element_by_xpath("//input[@type='submit' and @value='Save']").click()


test_test_addProjects()

def test_addHobbies():
    driver.get("http://localhost:8000/admin")
    assert "Django" in driver.title

    username = driver.find_element_by_name("username")
    username.clear()
    username.send_keys("userabc1")

    password = driver.find_element_by_name("password")
    password.clear()
    password.send_keys("abc1234567@")

    driver.find_element_by_xpath("//input[@type='submit' and @value='Log in']").click()

    driver.find_element_by_link_text("Categorys").click()

    driver.find_element_by_class_name("addlink").click()

    addCategory = driver.find_element_by_name("name")
    addCategory.clear()
    addCategory.send_keys("Hobbies")

    driver.find_element_by_xpath("//input[@type='submit' and @value='Save']").click()


test_test_addHobbies()

def test_addCategoryFail():
    driver.get("http://localhost:8000/admin")
    assert "Django" in driver.title

    username = driver.find_element_by_name("username")
    username.clear()
    username.send_keys("tanjunhong")

    password = driver.find_element_by_name("password")
    password.clear()
    password.send_keys("22Y69u96")

    driver.find_element_by_xpath("//input[@type='submit' and @value='Log in']").click()

    driver.find_element_by_link_text("Categorys").click()

    driver.find_element_by_class_name("addlink").click()

    addCategory = driver.find_element_by_name("name")
    addCategory.clear()
    addCategory.send_keys("!@#$%")

    driver.find_element_by_xpath("//input[@type='submit' and @value='Save']").click()
    assert "Please ensure characters enter are valid." not in driver.page_source
    driver.close()

test_addCategoryFail()

### Post ###

def test_addPost():
    driver.get("http://localhost:8000/admin")
    assert "Django" in driver.title
    
    username = driver.find_element_by_name("username")
    username.clear()
    username.send_keys("tanjunhong")

    password = driver.find_element_by_name("password")
    password.clear()
    password.send_keys("22Y69u96")

    driver.find_element_by_xpath("//input[@type='submit' and @value='Log in']").click()

    driver.find_element_by_link_text("Posts").click()

    driver.find_element_by_class_name("addlink").click()

    addCategory = driver.find_element_by_css_selector("#id_title")
    addCategory.clear()
    addCategory.send_keys("Test Post 2")

    addCategory = driver.find_element_by_name("body")
    addCategory.clear()
    addCategory.send_keys("This is another test post")

    driver.find_element_by_link_text("Categorys").click()

    driver.find_elemnt_by_class_name(addlink).click()

    addCategory = driver.find_element_by_name("name")
    addCategory.clear()
    addCategory.send_keys("Hobbies")

    driver.find_element_by_xpath("//input[@type='submit' and @value='Save']").click()
    driver.close()

test_addPost():

def test_addPostFail():
    driver.get("http://localhost:8000/admin")
    assert "Django" in driver.title
    
    username = driver.find_element_by_name("username")
    username.clear()
    username.send_keys("tanjunhong")

    password = driver.find_element_by_name("password")
    password.clear()
    password.send_keys("22Y69u96")

    driver.find_element_by_xpath("//input[@type='submit' and @value='Log in']").click()

    driver.find_element_by_link_text("Posts").click()

    driver.find_element_by_class_name("addlink").click()

    addCategory = driver.find_element_by_css_selector("#id_title")
    addCategory.clear()
    addCategory.send_keys("Test Post 3")

    addCategory = driver.find_element_by_name("body")
    addCategory.clear()
    addCategory.send_keys("This is yet another test post")

    driver.find_element_by_xpath("//input[@type='submit' and @value='Save']").click()
    assert "Please select category option." not in driver.page_source
    driver.close()

test_addPostFail()
