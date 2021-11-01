from datetime import datetime

def run():
    #hora local
    my_time_local = datetime.now()
    print(my_time_local)
    #hora universal
    my_time_utc = datetime.utcnow()
    print(my_time_utc)
    #día de hoy
    my_day = datetime.today()
    print(my_day)
    print(f'Year: {my_day.year}')
    print(f'Month: {my_day.month}')
    print(f'Day: {my_day.day}')
    # formatos de fecha
    my_datetime = datetime.now()
    print(my_datetime)
    my_str = my_datetime.strftime("%d/%m/%Y")
    print(f'Formato LATAM: {my_str}')

    my_str = my_datetime.strftime("%m/%d/%Y")
    print(f'Formato USA: {my_str}')

    my_str = my_datetime.strftime("Estamos en el año %Y")
    print(f'Formato Random: {my_str}')

if __name__ == "__main__":
    run()