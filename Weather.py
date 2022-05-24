from Ship import Ship
import requests
from datetime import datetime


class Weather(Ship):

    def get_json(self, lat, lon):
        header = {'Content-Type': 'application/json'}
        url = 'https://api.windy.com/api/point-forecast/v2'
        # api_key = '83bsuhSWrEHgTcnywYmnvcAyYum8SbJu'
        # api_key = 'mJQTARUXB3UIGSI62N6nFobxnho4BGNN'
        # api_key = 'RTlJInX6C26qkXHiPN07X5ax0ha7KPXe'
        api_key = 'NOpe1T5bbORVgVnxpuwdPBnGf9dt5mAj'
        # api_key = 'BAROVzCSvcXdtaPY7kPcpAg9YXQn6nR8'
        # api_key = 'xLRbEICgGqISfZ3xiBVDQobjwc2fr26H'
        data = {
            "lat": lat,
            "lon": lon,
            "model": "gfs",
            "parameters": ["wind", "windGust", "waves"],
            "levels": ["surface", "surface", "surface"],
            "key": api_key
        }

        json = requests.post(url=url, json=data, headers=header).json()
        for i in range(len(json['ts'])):
            # Надо доработать
            json['ts'][i] = datetime.utcfromtimestamp(int(str(json['ts'][i])[0:-3])).strftime('%Y-%m-%d %H:%M:%S')

            # json['ts'][i] = pd.to_datetime(ts, unit='ms').strftime("%m/%d/%Y")

        return json

    def data_picker(self):
        path = self.expected_path()
        data = []
        res = []
        for i in range(len(path)):
            data.append(self.get_json(path[i][0], path[i][1]))

        for j in range(len(data)):
            dictionary = {data[j]['ts'][j]: {'wind_u': round(data[j]['wind_u-surface'][j], 2),
                                             'wind_v': round(data[j]['wind_v-surface'][j], 2),
                                             'gust': round(data[j]['gust-surface'][j], 2),
                                             'waves_period': str(data[j]['waves_period-surface'][j]),
                                             'waves_height': str(data[j]['waves_height-surface'][j])}}
            res.append(dictionary)

        return res
