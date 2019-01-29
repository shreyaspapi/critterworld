from selenium import webdriver
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.firefox.options import Options
from selenium.webdriver.support.ui import Select
import time
from pymongo import MongoClient
import sys

def find_element_by_id_puttext(ID, text):
    element = driver.find_element_by_id(ID)
    element.click()
    element.send_keys(text)

def find_element_dropdown(xpath, city):
    element = driver.find_element_by_xpath(xpath)
    element.send_keys(city)
    
def click_using_element(something, ele):
    if ele == "id":
        element = driver.find_element_by_id(something)
        element.click()
    elif ele == "xpath":
        element = driver.find_element_by_xpath(something)
        element.click()

def get_text(something, by):
    if by == "id" or by == "ID":
        text = driver.find_element_by_id(something).text
        return text
    elif by == "xpath":
        text = driver.find_element_by_xpath(something).text
        return text

try:
    driver_path = r"chromedriver/chromedriver"
    driver = webdriver.Chrome(driver_path)

    driver.get("https://www.goair.in/plan-my-trip/manage-booking/")

    pnr_id = "PNR"
    pnr = str(sys.argv[1]) #"SYLG9A"

    name_or_email_id = "FirstName"
    name_or_email = str(sys.argv[2]) #"Jain"

    search_xpath = "/html/body/div[1]/div/div/div[2]/div/div/div[2]/div/div/div/div/button"

    find_element_by_id_puttext(pnr_id, pnr)
    find_element_by_id_puttext(name_or_email_id, name_or_email)

    click_using_element(search_xpath, "xpath")

    ######################################################################################################################################################
    #                                                               PAGE 2                                                                               #
    ######################################################################################################################################################


    departure_xpath = '//*[@id="sectionBody"]/div[1]/div[2]/div/div[2]/div[3]/div/div[2]/div[2]/div/div[2]/h4'
    departure_time_xpath = '//*[@id="sectionBody"]/div[1]/div[2]/div/div[2]/div[3]/div/div[2]/div[2]/div/div[1]/h4'

    arrival_xpath = '//*[@id="sectionBody"]/div[1]/div[2]/div/div[2]/div[3]/div/div[2]/div[4]/div/div[2]/h4'
    arrival_time_xpath = '//*[@id="sectionBody"]/div[1]/div[2]/div/div[2]/div[3]/div/div[2]/div[2]/div/div[1]/h4'

    departure = get_text(departure_xpath, "xpath")
    arrival = get_text(arrival_xpath, "xpath")

    departure_time = get_text(departure_time_xpath, "xpath")
    arrival_time = get_text(arrival_time_xpath, "xpath")

    date_xpath = '//*[@id="price_display_container"]/div[1]/div[1]/ul/li[3]/div[2]'
    flight_number_xpath = '//*[@id="price_display_container"]/div[1]/div[1]/ul/li[4]/div[2]' 

    date = get_text(date_xpath, "xpath")
    flight_number = get_text(flight_number_xpath, "xpath")

    driver.close()

    #print(departure_time, departure, arrival_time, arrival, date, flight_number)

    client = MongoClient('mongodb://bagshair#12:bagshair#1234@35.230.160.59:27090/')

    db = client['flight_details']

    posts = db.posts
    post_data = {
        'pnr': '{}'.format(pnr),
        'email or name': '{}'.format(name_or_email),
        'flight': 'air asia',
        'flight number': '{}'.format(flight_number),
        'departure': '{}'.format(departure),
        'arrival': '{}'.format(arrival),
        'departure time': '{}'.format(departure_time),
        'arrival time': '{}'.format(arrival_time),
        'flight date': '{}'.format(date)
        }
    result = posts.insert_one(post_data)
    print('One post: {0}'.format(result.inserted_id))

except:
    print("Something went wrong")