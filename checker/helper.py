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

# Contest URL
BASE_URL = 'https://www.hackerrank.com/contests/'
CONTEST_SLUG = 'week-3-cse212-1718/' # TODO add dictionary | array
LEADERBOARD = 'leaderboard/'
JUDGE = 'judge/submissions/'
CHALLENGE = 'challenges/'
TEAM = lambda NAME: 'team/' + NAME

TEAM_URL = lambda NAME: BASE_URL + CONTEST_SLUG + JUDGE + TEAM(NAME)
PROBLEM_URL = lambda NAME: 

# Auth