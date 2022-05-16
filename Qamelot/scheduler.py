from .rarible_tasks import *
from WebAPI.project_modules import *

# schedule the job to run at intervals of 20 secs
schedule.every(20).seconds.do(create_Assets)

while True:
    schedule.run_pending()
    time.sleep(5)