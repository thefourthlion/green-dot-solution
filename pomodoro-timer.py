import time

def pomodoro_timer(work_time, break_time, num_intervals):
    for curr_interval in range(num_intervals):
        print(f"Work interval {curr_interval + 1}")
        for i in range(work_time):
            time.sleep(1)
        print("Take a break!")
        
        for i in range(break_time):
            time.sleep(1)

        print(f"Interval {curr_interval + 1} complete")

print('Starting Pomodoro Timer')
# work_time and break_time are in seconds, num_intervals is the number of work/break intervals
pomodoro_timer(1500, 300, 4) # typical Pomodoro intervals: 25 mins work, 5 mins break, 4 intervals