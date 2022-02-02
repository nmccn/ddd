from datetime import datetime
from apscheduler.schedulers.background import BackgroundScheduler
from .automate_tasks import automate_tasks

def start():
    # This is called once on init.
    scheduler = BackgroundScheduler()
    scheduler.add_job(automate_tasks) # To get initial population of data. 
    scheduler.add_job(automate_tasks, 'interval', minutes=60)
    scheduler.start()