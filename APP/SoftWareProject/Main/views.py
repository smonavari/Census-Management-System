from django.shortcuts import render_to_response
from django.template import RequestContext

import openpyxl
from openpyxl.writer.write_only import WriteOnlyCell


def update_information(request):

    if request.method=='POST':
        if request.POST.get('country', None) and request.POST.get('year', None) and \
           request.POST.get('men', None) and request.POST.get('women', None):

            country = request.POST.get('country', None)
            year = request.POST.get('year', None)
            men = request.POST.get('men', None)
            women = request.POST.get('women', None)
            
            wb = openpyxl.load_workbook('..\..\Data\WPP2015_POP_F01_2_TOTAL_POPULATION_MALE.xlsx')
            message_action = update_information_popularity_on_year(wb['ESTIMATES'], country, year, men)+'-> Men \n'
            wb.save('..\..\Data\WPP2015_POP_F01_2_TOTAL_POPULATION_MALE.xlsx')

            wb = openpyxl.load_workbook('..\..\Data\WPP2015_POP_F01_3_TOTAL_POPULATION_FEMALE.xlsx')
            message_action += update_information_popularity_on_year(wb['ESTIMATES'], country, year, women)+'-> Women'
            wb.save('..\..\Data\WPP2015_POP_F01_3_TOTAL_POPULATION_FEMALE.xlsx')
            return render_to_response('update_information.html', {'message_action':message_action}, context_instance=RequestContext(request))

    return render_to_response('update_information.html', {}, context_instance=RequestContext(request))


def update_information_popularity_on_year(ws, name_country, year, num):
    name_city_col = 3
    year_start_col = 6
    year_row = 17

    i = 18
    while True:
        if ws.cell(row=i, column=name_city_col).value == name_country:
            j = 0
            while True:
                if ws.cell(row=year_row, column=year_start_col+j).value == year:
                    ws.cell(row=i, column=year_start_col+j).value = num
                    return 'update data'

                elif not ws.cell(row=i, column=year_start_col+j).value:
                    break

                j += 1

            return 'this year not exist -> year = '+year

        elif not ws.cell(row=i, column=name_city_col).value:
            break

        i += 1
    return 'this country not exist -> country = '+name_country


def show_list_popularity(request):
    if request.method == 'POST' and request.POST.get('year', None):

        year = request.POST.get('year')

        wb = openpyxl.load_workbook('..\..\Data\WPP2015_POP_F01_2_TOTAL_POPULATION_MALE.xlsx')
        m = get_list_popularity(wb['ESTIMATES'], year)

        wb = openpyxl.load_workbook('..\..\Data\WPP2015_POP_F01_3_TOTAL_POPULATION_FEMALE.xlsx')
        w = get_list_popularity(wb['ESTIMATES'], year)

        list_pop = []
        for x in w.keys():
            list_pop.append([x, w[x], m[x], w[x]+m[x]])

        list_pop.sort(key=lambda y: y[3])

        return render_to_response('showListOfPopularity.html', {'year': year, 'list_of_popularity': list_pop}, context_instance=RequestContext(request))

    return render_to_response('showListOfPopularity.html', {}, context_instance=RequestContext(request))


def get_list_popularity(ws, year):
    name_city_col = 3
    name_city_row = 29
    year_start_col = 6
    year_row = 17
    list_pop = {}

    i = 0
    while True:
        if ws.cell(row=year_row, column=year_start_col+i).value == year:
            j = 0
            while True:
                if not ws.cell(row=name_city_row+j, column=name_city_col).value:
                    break

                else:
                    list_pop[ws.cell(row=name_city_row+j, column=name_city_col).value] = \
                        int(ws.cell(row=name_city_row+j, column=year_start_col+i).value)

                j += 1

            return list_pop

        elif not ws.cell(row=year_row, column=year_start_col+i).value:
            break

        i += 1

    return None
