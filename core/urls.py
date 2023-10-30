from django.urls import path

from .views import IndexView, get_link_preview

app_name = 'core'

urlpatterns = [
    path('', IndexView.as_view(), name='index'),
    path('get_link_preview/', get_link_preview, name='get_link_preview')
]
