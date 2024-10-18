import calendar 

def print_calendar(year, month):
    print(calendar.month(year, month))

if __name__ == "__main__":
    year = int(input('Enter year: '))
    month = int(input('Enter month: '))
    print_calendar(year, month)