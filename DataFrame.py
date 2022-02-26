import pandas as pd
from Weather import Weather


class DataConverter(Weather):
    def converter_to_df(self):
        data = self.data_picker()
        df = pd.DataFrame({'date-time': [x[0] for x in data], 'wind-speed': [x[1] for x in data]})
        return df

    def xlsx_maker(self):
        writer = pd.ExcelWriter('Data/example.xlsx', engine='xlsxwriter')
        self.converter_to_df().to_excel(writer, 'Sheet1', index=False)
        writer.save()
        return None


if __name__ == '__main__':
    pizda = DataConverter('9408138')
    print(pizda.xlsx_maker())
