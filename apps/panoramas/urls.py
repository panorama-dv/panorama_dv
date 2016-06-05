from django.conf.urls import url
from panoramas import views

app_name = 'panoramas'

urlpatterns = [
    url(r'^(?P<slug>[^\.]+)', views.get_panorama_page,
        name='panorama_page')
]
