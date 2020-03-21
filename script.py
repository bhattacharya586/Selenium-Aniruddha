from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from time import sleep
print("Enter 1 for Login and Enter 2 for Register")
choice = int(input())
if(choice == 1):
    #Login
    print("Enter your email id")
    username = input()
    print("Enter your password")
    password = input()
    driver = webdriver.Chrome(executable_path=r"C:\Users\cools\Desktop\chromedriver_win32\chromedriver.exe")
    driver.get('http://ec2-54-81-242-53.compute-1.amazonaws.com/')
    driver.find_element_by_id('logemail').send_keys(username)
    sleep(2)
    driver.find_element_by_id('logpsk').send_keys(password)
    driver.find_element_by_name('login').click()
elif(choice == 2):
    #Register
    print("Enter your First Name")
    fname = input()
    print("Enter your SurName")
    sname = input()
    print("Enter your email id")
    email = input()
    print("Enter your password")
    password = input()
    print("Enter your DOB in format (DD-MMM-YYYY)=>(7-Sep-2000)")
    dob = input()
    bdy = dob.split('-')
    print("Enter your gender (Male,Female,Other)")
    gen = input()
    driver = webdriver.Chrome(executable_path=r"C:\Users\cools\Desktop\chromedriver_win32\chromedriver.exe")
    driver.get('http://ec2-54-81-242-53.compute-1.amazonaws.com/')
    driver.find_element_by_id('signfirstname').send_keys(fname)
    sleep(2)
    driver.find_element_by_id('signsurname').send_keys(sname)
    sleep(2)
    driver.find_element_by_id('signemail').send_keys(email)
    sleep(2)
    driver.find_element_by_id('signpassword').send_keys(password)
    sleep(2)
    driver.find_element_by_id('signday').send_keys(bdy[0])
    sleep(2)
    driver.find_element_by_id('signmonth').send_keys(bdy[1])
    sleep(2)
    driver.find_element_by_id('signyear').send_keys(bdy[2])
    sleep(2)
    if(gen=="Male"):
        driver.find_element_by_id('signgender1').click()
    elif(gen=="Female"):
        driver.find_element_by_id('signgender2').click()
    else:
        driver.find_element_by_id('signgender3').click()
    sleep(2)
    driver.find_element_by_name('register').click()
else:
    print("Wrong Choice!!!")



