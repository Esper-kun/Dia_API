from django.urls import path, register_converter
from datetime import datetime
from dias_api.apps.Dias import views


class DateConverter:
    regex = '\d{4}-\d{2}-\d{2}'

    def to_python(self, value):
        return datetime.strptime(value, '%Y-%m-%d')

    def to_url(self, value):
        return value

register_converter(DateConverter, 'yyyy')


urlpatterns=[
    path('', views.ListaDiaView.as_view(), name="lista_dias"),
    path('<yyyy:id_dia>', views.DetalhesDiaView.as_view(), name="detalhes_dias")
]

