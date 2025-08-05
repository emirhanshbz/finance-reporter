from apscheduler.schedulers.blocking import BlockingScheduler
from app.scheduler import daily_job
from app import config

def start():
    scheduler = BlockingScheduler()

    # Günlük saat ayarı
    scheduler.add_job(
        # daily_job,
        # trigger='cron',
        # hour=config.SEND_TIME_HOUR,
        # minute=config.SEND_TIME_MINUTE,
        # id='daily_finance_report',
        # replace_existing=True
        daily_job,
        trigger='interval',
        minutes=1,
        id='test_report_job',
        replace_existing=True
    )

    scheduler.start()
    print(f"⏰ Scheduler started. Daily job set for {config.SEND_TIME_HOUR}:{config.SEND_TIME_MINUTE:02d}")
    
if __name__ == "__main__":
    start()