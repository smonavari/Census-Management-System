from django.conf.urls import include, url
from django.contrib import admin

urlpatterns = [
    # Examples:
    # url(r'^$', 'SoftWareProject.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^admin/', include(admin.site.urls)),
    url(r'^updateinformation$', "Main.views.update_information"),
    url(r'^protectedcountry$', "Main.views.update_protected_cell_of_country"),
    url(r'^chart$', "Main.views"),
    url(r'^chart/(\w+)$', "Main.views.countryshowchart"),
    url(r'^getyear$', "Main.views"),
    url(r'^getyearc/(\d+)/(\w+)$', "Main.views.get_year_country"),
    url(r'^updateinformation$', "Main.views.update_information"),
    url(r'^popularitylist', "Main.views.show_list_popularity"),
]
