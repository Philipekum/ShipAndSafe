from Ship import Ship
from Weather import Weather
import eel
from DataFrame import DataConverter


@eel.expose
def getWeather(imo):
    wind_force = Weather(imo)
    data = wind_force.data_picker()
    return data


@eel.expose
def getInfo(imo):
    ship = Ship(imo)
    return ship.speed, ship.course, ship.c_lat, ship.c_lon


@eel.expose
def saveFile(imo):
    file = DataConverter(imo)
    file.xlsx_maker()


def main():
    eel.init("template")
    eel.start("index.html")


if __name__ == '__main__':
    main()
