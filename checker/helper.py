import math
# Functions
def find_element_by_id_puttext(ID, text):
    element = driver.find_element_by_id(ID)
    element.click()
    element.send_keys(text)

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

# Preprocessing data
ACADEMIC_YEAR = '1819' # input('Enter academic year:') # 1617 | 1718 | 1819 | 1920
SEMESTER_CODE = 'SP' # input('Enter sem code:') # FA | SP | Su | Wi
BATCH_YEAR = 'SO' # input('Enter batch code:') # FR | SO | JU | SR
COURSE_CODE = 'CSE212P'


# Contest info
WEEK_NUMBER = input('Enter week number:')
CONTEST_CODE = ACADEMIC_YEAR + SEMESTER_CODE + BATCH_YEAR + COURSE_CODE + WEEK_NUMBER # 1819SPSOCSE212P##
PROBLEM = {WEEK_NUMBER:{}}
SCORE = {PROBLEM[WEEK_NUMBER]}
TOTAL = sum(SCORE.values())
CUTOFF = 0.5
CUTOFF_HALF = 0.2
SLUGS = {WEEK_NUMBER:[]}

# Dir Structure
SUBMISSIONS_DIR = os.path.join('submissions', CONTEST_CODE) # submissions/1819SPSOCSE212P##

# Auth
LOGIN_URL = 'https://www.hackerrank.com/auth/login'
USERNAME_ID = 'input-1'
PASSWORD_ID = 'input-2'
LOGIN_XPATH = '//*[@id="content"]/div/div[2]/div[2]/div/div/div[2]/div/div/div[2]/div[1]/form/div[4]/button'

BASE_URL = 'https://www.hackerrank.com/'
CONTEST_SLUG = lambda slug: 'contests/'+slug
SUBMISSIONS_URL = 'judge/submissions/'
CHALLENGE_SLUG = lambda slug: 'challenge/'+slug

TABLE_CLASS = 'table-wrap'
HEADER_CLASS = 'submissions_list-header'
SUBMISSIONS_CLASS = 'submissions_item'
NO_CLICK = 'submissions-title'

TESTCASE_ID = lambda x: 'testcase-card-'+str(x)
CODE_ID = 'submission-code'

CHALLENGE_CLASS = 'hr_tour-challenge-name'
TEAM_XPATH = '//*[@id="content"]/div/div/section/div/div[2]/section/div[1]/p/span'




CLASS_NAME = 'submissions-title'
ACCEPTED_CLASS = 'accept'
CODE_ID = lambda id: id
