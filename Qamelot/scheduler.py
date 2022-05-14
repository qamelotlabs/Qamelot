from .rarible_tasks import *
import schedule
import time
from os import system

# schedule the job to run at intervals of 1 min
schedule.every(20).seconds.do(create_Assets)

while True:
    schedule.run_pending()
    time.sleep(5)