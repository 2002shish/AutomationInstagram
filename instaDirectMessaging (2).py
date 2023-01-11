# importing module
from random import random
from speech_recognition import Recognizer, Microphone
import os
from time import sleep
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.common.keys import Keys
from selenium import webdriver
from pyttsx3 import init
import pyautogui
driver = webdriver.Edge(r"C:\Users\kashi\Downloads\msedgedriver.exe")
# enter receiver user name
engine = init('sapi5')
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[1].id)

bot = driver
itr = 0


def speak(audio):
    engine.say(audio)
    engine.runAndWait()

speak('Dear Sir, welcome to our automation project.')

print('''////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////

Login Credentials Required   : ''')

#taking username and password from sender
speak('Please, enter username')
username = input('''///////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////
Please, enter username  :  ''')
u =0
while username == " ":
    speak('Please, enter username')
    username = input("Enter your username: ")
    u += 1
speak('enter password please!')
password = input('''///////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////
Enter your password  :  ''')
p =0
while password == " ":
    speak('enter password please!')
    password = input("Enter your password: ")
    p += 1
speak('Tell me receiver username')
receiver = input('''///////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////
Enter receiver username  :  ''')
r =0
while receiver == " ":
    speak('Tell me receiver username')
    receiver = input('Enter receiver username: ')
    r += 1

def login():
    base_url = 'https://www.instagram.com/'
    bot.get(base_url)
    enter_username = WebDriverWait(bot, 20).until(
        expected_conditions.presence_of_element_located((By.NAME, 'username')))
    enter_username.send_keys(username)
    enter_password = WebDriverWait(bot, 20).until(
        expected_conditions.presence_of_element_located((By.NAME, 'password')))
    enter_password.send_keys(password)
    enter_password.send_keys(Keys.RETURN)
    sleep(5)
    # first pop-up
    try:
        bot.find_element_by_xpath(
            '//*[@id="react-root"]/section/main/div/div/div/div/button').click()
    except:
        warn()
        return
    sleep(5)
    # 2nd pop-up
    try:
        bot.find_element_by_xpath("//button[text()='Not Now']").click()
    except:
        warn()
        return


def warn():
    speak('your internet connection is weak')


def further():
    # direct button
    bot.find_element_by_class_name('xWeGp').click()
    sleep(3)
    # clicks on send message button
    bot.find_element_by_xpath(
        "//button[text()='Send Message']").click()
    #searching the username
    inputElement = driver.find_element_by_class_name('uMkC7')
    inputElement.send_keys(receiver)
    sleep(4)

    #selcting or toogling the receiver
    toogle=driver.find_element_by_xpath('//div[@class="QBdPU "]/*[name()="svg"][@aria-label="Toggle selection"]') #for dyanamic element
    toogle.click()
    sleep(2)

    
    #moving next to chatbox of user
    from pyautogui import locateOnScreen,click;bat=None
    while bat==None:
        bat=locateOnScreen('del.png')
    click('del.png')
    from random import choice
    l = "['hello', 'Hi', 'How are You', 'Hey', 'Bro whats up']";sleep(3)
    
    pyautogui.hotkey('ctrl', 'v');pyautogui.press("enter")
def next():
    sleep(2)

def next():
    sleep(2)


if __name__ == "__main__":
    login()
    further()
    speak('instagram opened sir')
