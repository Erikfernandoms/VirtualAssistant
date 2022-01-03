from datetime import datetime


def get_period():
    if int(datetime.today().strftime("%H")) >= 0 and int(datetime.today().strftime("%H")) <= 11:
        period = 'dia'
        return period
    elif int(datetime.today().strftime("%H")) >= 12 and int(datetime.today().strftime("%H")) <=17:
        period = 'tarde'
        return period
    else:
        period = 'noite'
        return period
        