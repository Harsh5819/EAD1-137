import time

def countdown_timer(seconds):
    while seconds:
        mins, secs = divmod(seconds, 60)
        time_format = '{:02d}:{:02d}'.format(mins, secs)
        print(time_format, end='\r')  # Overwrite the last printed time
        time.sleep(1)
        seconds -= 1
    print("Time's up!")

# Set the countdown time in seconds
countdown_time = int(input("Enter time in seconds: "))
countdown_timer(countdown_time)
