__author__ = 'sepideh'


import openpyxl
from openpyxl.styles import Protection, Style

def update_information_popularity_on_year(ws, name_country):
    name_city_col = 3
    i = 18
    while True:
        if ws.cell(row=i, column=name_city_col).value == name_country:
            for col in range(len(ws.columns)+1):
                if col > name_city_col:
                    ws.cell(row=i, column=col).style = Style(protection=Protection(locked=False))
                    print(ws.cell(row=i, column=col).style.protection)
                    print(ws.cell(row=i, column=col).value)
                    ws.cell(row=i, column=col).value = 10
                    print(ws.cell(row=i, column=col).value)
                    print("==============================")

        elif not ws.cell(row=i, column=name_city_col).value:
            break

        i += 1
    ws.protection.enable()


wb = openpyxl.load_workbook('..\..\..\Data\WPP2015_POP_F01_2_TOTAL_POPULATION_MALE.xlsx')
print(update_information_popularity_on_year(wb['ESTIMATES'], 'China'))
wb.save(filename = 'simple.xlsx')

