from WebAPI.scraping_and_seeding.rarible_scraping import *
from WebAPI.scraping_and_seeding.collection_scraping import *
from WebAPI.project_modules import *

# schedule the job to run at intervals of 20 secs
schedule.every(10).seconds.do(nft_Assets)

while True:
    schedule.run_pending()
    time.sleep(5)