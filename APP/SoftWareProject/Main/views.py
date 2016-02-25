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