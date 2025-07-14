# This script will print the current date in IST
import datetime
def print_current_date_ist():
    # Get the current date and time in UTC
    utc_now = datetime.datetime.now(datetime.timezone.utc)
    
    # Convert UTC to IST (UTC+5:30)
    ist_now = utc_now + datetime.timedelta(hours=5, minutes=30)
    
    # Print the current date and time in IST
    print("Current date and time in IST:", ist_now.strftime("%Y-%m-%d %H:%M:%S"))
if __name__ == "__main__":
    print_current_date_ist()
    