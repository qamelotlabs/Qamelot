<<<<<<< HEAD
from NFTCollectionApp.Seeding.CollectionsSeeding import *
from Qamelot.project_modules import *


def runSchedule():
    print('Schedule running')
    # example: run_parallel(task_a(),task_b(),hello(msg="konstantinos"))
    runParallel(collectionSeeding())

# schedule the job daily at 05:00 am
schedule.every().day.at("05:00").do(runSchedule)
=======
from WebAPI.scraping_and_seeding.rarible_scraping import *
from WebAPI.scraping_and_seeding.collection_scraping import *
from WebAPI.project_modules import *

# schedule the job to run at intervals of 20 secs
schedule.every(10).seconds.do(nft_Assets)
>>>>>>> 6c7f2e3... modified all process

while True:
    schedule.run_pending()
    time.sleep(5)