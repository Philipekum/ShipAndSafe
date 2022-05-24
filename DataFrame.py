import pandas as pd
from Weather import Weather
from pathlib import Path


class DataConverter(Weather):
    def converter_to_df(self):
        data = self.data_picker()
        # data = [{'2022-05-20 03:00:00': {'wind_u': 26, 'wind_v': 0.85, 'gust': 41, 'waves_period': 'None', 'waves_height': 'None'}}, {'2022-05-20 06:00:00': {'wind_u': 27, 'wind_v': -1.61, 'gust': 6.33, 'waves_period': 'None', 'waves_height': 'None'}}, {'2022-05-20 09:00:00': {'wind_u': 17, 'wind_v': 1.37, 'gust': 10.13, 'waves_period': 'None', 'waves_height': 'None'}}, {'2022-05-20 12:00:00': {'wind_u': -3.33, 'wind_v': 1.37, 'gust': 3.12, 'waves_period': 'None', 'waves_height': 'None'}}, {'2022-05-20 15:00:00': {'wind_u': 1.13, 'wind_v': 2.2, 'gust': 2.91, 'waves_period': 'None', 'waves_height': 'None'}}]
        date_keys = []
        wind_u = []
        wind_v = []
        gust = []
        waves_period = []
        waves_height = []
        for item in data:
            for elem in item.keys():
                date_keys.append(elem)
                wind_u.append(item[elem]['wind_u'])
                wind_v.append(item[elem]['wind_v'])
                gust.append(item[elem]['gust'])
                waves_period.append(item[elem]['waves_period'])
                waves_height.append(item[elem]['waves_height'])
        df = pd.DataFrame({
            'Date': date_keys,
            'Wind (W-E)': wind_u,
            'Wind (S-N)': wind_v,
            'Gust': gust,
            'Waves Period': waves_period,
            'Waves Height': waves_height
        })
        # df = pd.DataFrame({'date-time': [x[0] for x in data], 'wind-speed (w-e)': [x[1] for x in data]})
        return df

    def xlsx_maker(self):
        downloads_path = str(Path.home() / "Downloads")
        writer = pd.ExcelWriter(f'{downloads_path}/weather_forecast.xlsx', engine='xlsxwriter')
        self.converter_to_df().to_excel(writer, 'Sheet1', index=False)
        writer.save()
        return None
