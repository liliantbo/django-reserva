from django.urls import path
from .views import login_request, logout_view, registro_request, comprar_entrada, index, compra_list, concierto_detalle

app_name = 'Concert'

urlpatterns = [
    path('', index, name='index'),
    path('login/', login_request, name='login'),
    path('logout/', logout_view, name='logout'),
    path('signup/', registro_request, name='signup'),
    path('comprar/<int:concierto_id>/', comprar_entrada, name='comprar_entrada'),
    path('compras/', compra_list, name='compra_list'),
    path('concierto/<int:concierto_id>/', concierto_detalle, name='concierto_detalle'),
]
