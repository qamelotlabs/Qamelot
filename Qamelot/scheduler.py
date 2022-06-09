from NFTCollectionApp.Seeding.CollectionsSeeding import *
from Qamelot.project_modules import *


def runSchedule():
    print('Schedule running')
    # example: run_parallel(task_a(),task_b(),hello(msg="konstantinos"))
    runParallel(collectionSeeding())

# schedule the job daily at 05:00 am
# schedule.every(20).seconds.do(runSchedule) # for testing
schedule.every().day.at("05:00").do(runSchedule)

while True:
    schedule.run_pending()
    time.sleep(5)