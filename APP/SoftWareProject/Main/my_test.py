__author__ = 'sepideh'


import openpyxl


def update_information_popularity_on_year(ws, name_city, year, num):
    name_city_col = 3
    year_start_col = 6
    year_row = 17

    i = 18
    while True:
        if ws.cell(row=i, column=name_city_col) == name_city:
            j = 0
            while True:
                if ws.cell(row=year_row, column=year_start_col+j) == year:
                    ws.cell(row=i, column=year_start_col+j).value = num
                    return 'update data'

                elif not ws.cell(row=i, column=year_start_col+j).value:
                    break

                j += 1

            return 'this year not exist -> year = '+year

        elif not ws.cell(row=i, column=name_city_col).value:
            break

        i += 1
        print(i)
    return 'this city not exist -> city = '+name_city




wb = openpyxl.load_workbook('..\..\..\Data\WPP2015_POP_F01_2_TOTAL_POPULATION_MALE.xlsx')
ws = wb['ESTIMATES']
print(update_information_popularity_on_year(wb['ESTIMATES'],'kkkk',10,1))


