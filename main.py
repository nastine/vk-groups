from modules.vk_groups import write_to_db
import schedule
import time

if __name__ == "__main__":
    schedule.every().day.at("10:30").do(write_to_db)
    while True:
        schedule.run_pending()
        time.sleep(1)
