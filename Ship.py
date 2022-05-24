import requests
from math import cos, sin


class Ship:
    def __init__(self, imo):
        self.imo = imo
        url = f"https://goradar.ru/vessels_map.php?imo={self.imo}"
        r = \
            requests.post(url).text.split('vesCoordinates')[1].split('Увеличение области')[0].split('</small>,')[
                1].split('</b>')[0]
        self.c_lat = float(r.split(', ')[0])
        self.c_lon = float(r.split(', ')[1])
        self.course = float(r.split(',')[2].split(': ')[1])
        self.speed = float(r.split(',')[3].split(': ')[1])

    def future_position(self, time=0):
        f_lon = self.c_lon + self.speed * 3.0 * time * 1.852 * cos(self.course) / (40075.696 / 360)
        f_lat = self.c_lat + self.speed * 3.0 * time * 1.852 * sin(self.course) / (40008.55 / 360)

        return [f_lat, f_lon]

    def expected_path(self, n=6):
        path = []
        for i in range(n):
            path.append(self.future_position(i))
        return path
