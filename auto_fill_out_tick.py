# This script logs into tick, adds hours per day for a standard week
# designed to run on fridays & does not take into account holidays, etc.
# if not already, need to install chromedriver to your computer (http://chromedriver.chromium.org/downloads)
# & run 'pip install selenium' first

from selenium import webdriver
import time
from datetime import date, timedelta
import datetime
import sys

tickEmail = sys.argv[1]
tickPassword = sys.argv[2]
baseUrl = sys.argv[3]
projectString = sys.argv[4]
taskString = sys.argv[5]
hoursPerDay = sys.argv[6]
chromeDriverPath = sys.argv[7]

driver = webdriver.Chrome(executable_path=r'%s' % chromeDriverPath)
# you need to install chrome driver to your computer and point to it's location here

def Login():
    # these 5 lines log into tick for you
    driver.get(baseUrl) # for
    time.sleep(.5)
    username = driver.find_element_by_css_selector("#user_email")
    password = driver.find_element_by_css_selector("#user_password")
    username.send_keys(tickEmail)
    time.sleep(1)
    password.send_keys(tickPassword)
    time.sleep(1)
    driver.find_element_by_css_selector("#sign_in_button").click()
    time.sleep(2)

def FillInADaysHours():
    # this function fills in hours for each day selected
    hours = True
    try:
        time.sleep(1)
        driver.find_element_by_xpath("//a[contains(text(), '%s')]" % projectString)
        # this determines if there are hours entered.
        print(" - Hours were already entered for this day")
    except:
        hours = False
    if not hours:
        project = driver.find_element_by_xpath(
            "//span[contains(text(), 'Begin typing a client or project name')]").click()
        time.sleep(.5)
        project = driver.find_element_by_xpath("//div[contains(text(), '%s')]" % projectString).click()
        time.sleep(1)
        task = driver.find_element_by_id("s2id_task_id").click()
        time.sleep(.5)
        task = driver.find_element_by_xpath("//div[contains(text(), '%s')]" % taskString).click()
        time.sleep(.5)
        hours = driver.find_element_by_css_selector("#entry_hours")
        time.sleep(.5)
        hours.send_keys("%s" % hoursPerDay)
        driver.find_element_by_css_selector("#enter_time_btn").click()
        print(" - This days hours have now been entered")

def RunThrough():
    # this function clicks through the week and adds hours for each day
    Login()
    now = datetime.datetime.now()
    week = datetime.datetime.utcnow().isocalendar()[1]
    year = now.year
    d = date(year,1,1)
    if(d.weekday()>3):
        d = d+timedelta(7-d.weekday())
    else:
        d = d - timedelta(d.weekday())
    dlt = timedelta(days = (week-1)*7)
    mon = d + dlt
    tues = d + dlt + timedelta(days=1)
    wed = d + dlt + timedelta(days=2)
    thurs = d + dlt + timedelta(days=3)
    fri = d + dlt + timedelta(days=4)
    mon, tues, wed, thurs, fri = str(mon), str(tues), str(wed), str(thurs), str(fri)
    weekList = [mon, tues, wed, thurs, fri]
    for day in weekList:
        driver.find_element_by_xpath("//li[contains(@data-date, '%s')]" % day).click()
        print("The script is attempting to enter hours for %s" % day)
        FillInADaysHours()
        time.sleep(2)
    print("""
You now have hours entered for each day this week.
    """)
    driver.close()

RunThrough()
