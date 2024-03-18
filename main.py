from twilio.rest import Client
from datetime import datetime, timedelta
def sendMessage(phNumber, name, date):
    account_sid = 'AC65785169ec1c8d279df8b7312cb47d4b'
    auth_token = '94f3d599fc22be3071a17f6663f047f7'
    client = Client(account_sid, auth_token)
    phNumber = '+91'+str(phNumber)
    message = client.messages.create(
    from_ ='+15344446739',
    body =f"Hello {name}! You have your next dialysis session on {date}",
    to = phNumber
    )
    print(message.sid)

# sendMessage(8900384866, 'Subhrajyoti', '11/11/11')
    
def generate_schedule(start_date):
    start_date = datetime.strptime(start_date, "%d/%m/%y")
    
    schedule = []
    
    days_added = 0
    
    while days_added < 8 * 7:
        for _ in range(3):
            schedule.append(start_date.strftime("%d/%m/%y"))
            start_date += timedelta(days=2)
            days_added += 2
        
        start_date += timedelta(days=4)
        days_added += 4
    
    return schedule

def print_schedule(schedule):
    print("Schedule:")
    print("----------")
    
    for i, date in enumerate(schedule, start=1):
        print(f"{i}. {date}")

def compare_dates_and_call(schedule):
    today = datetime.today().date()
    
    schedule_dates = [datetime.strptime(date, "%d/%m/%y").date() for date in schedule]
    
    success = True
    for date in schedule_dates:

        if today == date - timedelta(days=1):
            call_function(date)
            success = False
            break 
    if (success):   
        print("No upcoming sessions")

def call_function(appdate):
    print("Message has been sent because today's date is a day before a date in the schedule.")
    sendMessage(num, name, appdate)


name = '' 
num = 0
date = ''
schedule= ''
while True:
    print("Welcome to SRM Global Hospital")
    print("===============================")
    print("1. Enter New Patient ")
    print("2. Check/Create Existing Patient Schedule ")
    print("3. Send Message ")
    print("4. Exit ")
    choice = int(input("Enter your choice "))
    if choice == 1:
        name = input("Enter patient name ")
        num = input("Enter pateint phone number ")
        date = input("Enter the date of first dialysis (dd/mm/yy) ")
        
    elif choice == 2:
        schedule = generate_schedule(date)
        print_schedule(schedule)

    elif choice == 3:
        compare_dates_and_call(schedule)

    elif choice == 4:
        break