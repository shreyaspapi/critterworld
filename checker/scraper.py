# Get (accepted) submissions AND leaderboard (w/ time and score)
import bs4
from helper import SUBMISSIONS_DIR
from selenium import webdriver
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.firefox.options import Options
from selenium.webdriver.support.ui import Select


# Save to SUBMISSIONS_DIR
