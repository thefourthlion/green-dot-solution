import datetime
import winsound

def set_alarm(alarm_time, alarm_message):
    while True:
        time_now = datetime.datetime.now().strftime('%H:%M')
        if time_now == alarm_time:
            print(alarm_message)
            winsound.Beep(2500, 1000)
            break

def get_user_input():
    alarm_time = input("Enter the alarm time in HH:MM format: ")
    alarm_message = input("Enter the message for the alarm: ")
    set_alarm(alarm_time, alarm_message)

get_user_input()