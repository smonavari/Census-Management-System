from django.http import Http404
from django.shortcuts import render
from openpyxl import load_workbook


def get_year_country_from_work_book(wb, year, country):
    ws = wb['ESTIMATES']
    year_column = int(year) - 1950 + 5
    # i = 0
    # for row in ws.rows:
    # if row[0].value == 'Index':
    #         for cell in row:
    #             if cell.value == year:
    #                 year_column = i
    #             i += 1
    count = -1
    for row in ws.rows:
        if row[2].value == country:
            print("found!")
            print(row[year_column].value)
            count = row[year_column].value
    return count


def get_year_country(request, year, country):
    wb = load_workbook(filename='../../Data/WPP2015_POP_F01_2_TOTAL_POPULATION_MALE.xlsx', read_only=True)
    maleCount = get_year_country_from_work_book(wb, year, country)
    wb = load_workbook(filename='../../Data/WPP2015_POP_F01_3_TOTAL_POPULATION_FEMALE.xlsx', read_only=True)
    femaleCount = get_year_country_from_work_book(wb, year, country)
