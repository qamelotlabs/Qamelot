from NFTCollectionApp.Seeding.CollectionsSeeding import *
from TwitterApp.scraping_and_seeding.twitter_scraping import *
from Qamelot.project_modules import *


def runCollectionSeedSchedule():
    print('Schedule running')
    # example: run_parallel(task_a(),task_b(),hello(msg="konstantinos"))
    runParallel(collectionSeeding())

def runTwitterSeedSchedule():
    print('Schedule running')
    # example: run_parallel(task_a(),task_b(),hello(msg="konstantinos"))
    runParallel(fetch_influencers())

# schedule the job daily at 05:00 am
# schedule.every(20).seconds.do(runSchedule) # for testing
schedule.every().day.at("05:00").do(runCollectionSeedSchedule)
schedule.every().day.at("06:00").do(runTwitterSeedSchedule)

while True:
    schedule.run_pending()
    time.sleep(5)