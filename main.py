MINUTES = 60 # 設定多久執行一次

from routine import routine
from apscheduler.schedulers.blocking import BlockingScheduler

########################################
if __name__ == '__main__':
    job_defaults = {"max_instances": 100}
    scheduler = BlockingScheduler(timezone="Asia/Taipei", job_defaults=job_defaults)
    scheduler.add_job(routine, "interval", minutes=MINUTES)
    try:
        print(f'\033[92mInterval: {MINUTES} min\n\033[0m')
        routine()
        scheduler.start()
    except Exception:
        print(f'\033[91mscheduler failed\033[0m')
