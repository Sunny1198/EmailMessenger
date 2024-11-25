import schedule
import time

def send_scheduled_email():
    print("Email sent!")

def schedule_emails():
    schedule.every(1).minutes.do(send_scheduled_email)
    while True:
        schedule.run_pending()
        time.sleep(1)
