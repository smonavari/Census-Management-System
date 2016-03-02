from django.conf.urls import include, url
from django.contrib import admin

urlpatterns = [
    # Examples:
    # url(r'^$', 'SoftWareProject.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^admin/', include(admin.site.urls)),
    url(r'^chart/(.+)$', "Main.views.countryshowchart"),
    url(r'^getyear$', "Main.views"),
    url(r'^getyearc/(\d+)/(\w+)$', "Main.views.get_year_country"),
    url(r'^updateinformation$', "Main.views.update_information"),
    url(r'^popularitylist', "Main.views.show_list_popularity"),
    url(r'^estimatechart/(\w+)/(\w+)$', "Main.views.estimatechart"),

]
