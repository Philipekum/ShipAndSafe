from Ship import Ship
import requests
from datetime import datetime


class Weather(Ship):

    def get_json(self, lat, lon):
        header = {'Content-Type': 'application/json'}
        url = 'https://api.windy.com/api/point-forecast/v2'
        # api_key = 'RTlJInX6C26qkXHiPN07X5ax0ha7KPXe'
        # api_key='NOpe1T5bbORVgVnxpuwdPBnGf9dt5mAj'
        # api_key = 'BAROVzCSvcXdtaPY7kPcpAg9YXQn6nR8'
        api_key = 'amqnyuOMRlzPvXTzzWfCfbew7kVGlfmC'
        data = {
            "lat": lat,
            "lon": lon,
            "model": "gfs",
            "parameters": ["wind"],
            "levels": ["surface"],
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
            res.append([data[j]['ts'][j], data[j]['wind_u-surface'][j]])

        return res


if __name__ == '__main__':
    wind_force = Weather('9408138')
    lat, lon = 23.361, -74.3766
    print(wind_force.data_picker())

# 'ts': [1645887600000, 1645898400000, 1645909200000, 1645920000000, 1645930800000, 1645941600000, 1645952400000, 1645963200000, 1645974000000, 1645984800000, 1645995600000, 1646006400000, 1646017200000, 1646028000000, 1646038800000, 1646049600000, 1646060400000, 1646071200000, 1646082000000, 1646092800000, 1646103600000, 1646114400000, 1646125200000, 1646136000000, 1646146800000, 1646157600000, 1646168400000, 1646179200000, 1646190000000, 1646200800000, 1646211600000, 1646222400000, 1646233200000, 1646244000000, 1646254800000, 1646265600000, 1646276400000, 1646287200000, 1646298000000, 1646308800000, 1646319600000, 1646330400000, 1646341200000, 1646352000000, 1646362800000, 1646373600000, 1646384400000, 1646395200000, 1646406000000, 1646416800000, 1646427600000, 1646438400000, 1646449200000, 1646460000000, 1646470800000, 1646481600000, 1646492400000, 1646503200000, 1646514000000, 1646524800000, 1646535600000, 1646546400000, 1646557200000, 1646568000000, 1646578800000, 1646589600000, 1646600400000, 1646611200000, 1646622000000, 1646632800000, 1646643600000, 1646654400000, 1646665200000, 1646676000000, 1646686800000, 1646697600000, 1646708400000, 1646719200000, 1646730000000, 1646740800000]
