from django.urls import path
from . import views

app_name = 'admin'
urlpatterns = [
    path('add_admin',views.add_admin, name='add_admin'),
    path('index_admin',views.index_admin, name='index_admin'),
    path('view_register',views.view_register, name='view_register'),
    path('update/<int:idd>',views.update, name='update'),
    path('register_students',views.register_students, name='register_students'),
    path('register_students1',views.register_students1, name='register_students1'),
    path('inactive_update/<int:inactive_id>',views.inactive_update, name='inactive_update'),
    path('/<int:active_id>',views.active_update, name='active_update'),






]