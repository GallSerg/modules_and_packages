import datetime
from application.salary import calculate_salary
from application.db.people import get_employees


if __name__ == '__main__':
    print('Calc salary time is', datetime.datetime.now())
    calculate_salary()

    print('Get employee time is', datetime.datetime.now())
    get_employees()
