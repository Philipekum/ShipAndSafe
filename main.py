from Ship import Ship
from Weather import Weather
import eel
from DataFrame import DataConverter


@eel.expose
def imo_checker(imo):
    if type(imo) != int:
        raise ValueError('Not an integer')
    else:
        return imo


@eel.expose
def get_weather(imo):
    wind_force = Weather(imo)
    data = wind_force.data_picker()
    return data


@eel.expose
def get_info(imo):
    ship = Ship(imo)
    return ship.speed, ship.course, ship.c_lat, ship.c_lon


@eel.expose
def save_file(imo):
    file = DataConverter(imo)
    file.xlsx_maker()


def main():
    eel.init("template")
    eel.start("index.html")


if __name__ == '__main__':
    main()
