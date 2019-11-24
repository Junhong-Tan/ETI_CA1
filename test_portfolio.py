import os
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities

def test_consecutively():
    driver = webdriver.Chrome()
    driver.get("http://localhost:8000/admin/")

    driver2 = webdriver.Chrome()
    driver2.get("http://localhost:8000/projects/")

    driver3 = webdriver.Chrome()
    driver3.get("http://localhost:8000/blog/")

    
test_consecutively()

### Login ###

def test_login():
    driver = webdriver.Chrome()
    driver.get("http://localhost:8000/admin")
    assert "Django" in driver.title

    username = driver.find_element_by_name("username")
    username.clear()
    username.send_keys("user1")

    password = driver.find_element_by_name("password")
    password.clear()
    password.send_keys("user1pw234")

    driver.find_element_by_xpath('//*[@id="login-form"]/div[3]/input').click()
    assert "Please ensure username & password is correct" not in driver.page_source
    driver.close()

test_login()

def test_adminLogin():
    driver = webdriver.Chrome()
    driver.get("http://localhost:8000/admin")
    assert "Django" in driver.title

    username = driver.find_element_by_name("username")
    username.clear()
    username.send_keys("tanjunhong")

    password = driver.find_element_by_name("password")
    password.clear()
    password.send_keys("22Y69u96")

    driver.find_element_by_xpath('//*[@id="login-form"]/div[3]/input').click()
    driver.close()

test_adminLogin()

### Comment ###

def test_addComment():
    driver = webdriver.Chrome()
    driver.get("http://localhost:8000/blog/")
    #assert "Django" in driver.title

    driver.find_element_by_xpath('/html/body/div/div/h2/a').click()

    addComment = driver.find_element_by_name('author')
    addComment.clear()
    addComment.send_keys("Tan Junhong")

    addComment = driver.find_element_by_name('body')
    addComment.clear()
    addComment.send_keys("This comment is automated")

    driver.find_element_by_xpath('/html/body/div/div/form/button').click
    driver.close()
    
test_addComment()

def test_addCommentFail():
    driver = webdriver.Chrome()
    driver.get("http://localhost:8000/blog/")
    assert "Django" in driver.title

    driver.find_element_by_xpath('/html/body/div/div/h2/a').click()

    addComment = driver.find_element_by_xpath('//*[@id="id_author"]').click()
    addComment.clear()
    addComment.send_keys("Tan Junhong")

    driver.find_element_by_xpath('/html/body/div/div/form/button').click
    assert "Please Do not leave comment empty." not in driver.page_source
    driver.close()

### Category ###

def test_addCCA():
    driver = webdriver.Chrome()
    driver.get("http://localhost:8000/admin")
    assert "Django" in driver.title

    username = driver.find_element_by_name("username")
    username.clear()
    username.send_keys("tanjunhong")

    password = driver.find_element_by_name("password")
    password.clear()
    password.send_keys("22Y69u96")

    driver.find_element_by_xpath('//*[@id="login-form"]/div[3]/input').click()

    #driver.find_element_by_link_text("Categorys").click()

    driver.find_element_by_class_name("addlink").click()

    addCategory = driver.find_element_by_xpath('//*[@id="id_name"]').click()
    addCategory.clear()
    addCategory.send_keys("CCA Activities")

    driver.find_element_by_xpath('//*[@id="post_form"]/div/div/input[1]').click()

test_addCCA()

def test_addCategoryFail():
    driver = webdriver.Chrome()
    driver.get("http://localhost:8000/admin")
    assert "Django" in driver.title

    username = driver.find_element_by_name("username")
    username.clear()
    username.send_keys("tanjunhong")

    password = driver.find_element_by_name("password")
    password.clear()
    password.send_keys("22Y69u96")

    driver.find_element_by_xpath('//*[@id="login-form"]/div[3]/input').click()

    driver.find_element_by_link_text("Categorys").click()

    driver.find_element_by_class_name("addlink").click()

    addCategory = driver.find_element_by_name("name")
    addCategory.clear()
    addCategory.send_keys("!@#$%")

    driver.find_element_by_xpath('//*[@id="post_form"]/div/div/input[1]').click()
    assert "Please ensure characters enter are valid." not in driver.page_source
    driver.close()

test_addCategoryFail()

### Post ###

def test_addPost():
    driver = webdriver.Chrome()
    driver.get("http://localhost:8000/admin")
    assert "Django" in driver.title
    
    username = driver.find_element_by_name("username")
    username.clear()
    username.send_keys("tanjunhong")

    password = driver.find_element_by_name("password")
    password.clear()
    password.send_keys("22Y69u96")

    driver.find_element_by_xpath('//*[@id="login-form"]/div[3]/input').click()

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
    addCategory.send_keys("Test")

    driver.find_element_by_xpath('//*[@id="post_form"]/div/div/input[1]').click()
    driver.close()

test_addPost()

def test_addPostFail():
    driver = webdriver.Chrome()
    driver.get("http://localhost:8000/admin")
    assert "Django" in driver.title
    
    username = driver.find_element_by_name("username")
    username.clear()
    username.send_keys("tanjunhong")

    password = driver.find_element_by_name("password")
    password.clear()
    password.send_keys("22Y69u96")

    driver.find_element_by_xpath('//*[@id="login-form"]/div[3]/input').click()

    driver.find_element_by_link_text("Posts").click()

    driver.find_element_by_class_name("addlink").click()

    addCategory = driver.find_element_by_css_selector("#id_title")
    addCategory.clear()
    addCategory.send_keys("Test Post 3")

    addCategory = driver.find_element_by_name("body")
    addCategory.clear()
    addCategory.send_keys("This is yet another test post")

    driver.find_element_by_xpath('//*[@id="post_form"]/div/div/input[1]').click()
    assert "Please select category option." not in driver.page_source
    driver.close()

test_addPostFail()
