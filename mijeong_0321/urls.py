from django.conf.urls import url
from django.contrib import admin
import wordcount.views

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^home/',wordcount.views.home, name='home'),
    url(r'^result/',wordcount.views.result, name='result'),

]
