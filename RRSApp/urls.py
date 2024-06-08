from django.urls import path
from . import views
from django.contrib.auth import views as ad

urlpatterns = [
	path('',views.home,name="hm"),
	path('abt/',views.about,name="ab"),
	path('cnt/',views.contact,name="ct"),
	path('reg/',views.register,name="rg"),
	path('lgn/',ad.LoginView.as_view(template_name="html/login.html"),name="lg"),
	path('lgot/',ad.LogoutView.as_view(template_name="html/logout.html"),name="lgt"),
	path('pfle/',views.profile,name="pf"),
	path('upfle/',views.updprofile,name="upf"),
	path('chge/',views.chgepwd,name="cge"),
	path('trd/',views.traindetail,name="td"),
    path('adtr/',views.addtrain,name="adt"),
    path('rest/<int:t_id>/',views.reservation,name="res"),
    path('cnfr/<int:train_id>/',views.conres,name="cfr"),
    path('yourtickets/', views.your_tickets, name='your_tickets'),
    path('cancel/<int:ticket_id>/', views.cancel_ticket, name='cancel_ticket'),
    path('edit/<int:train_id>/', views.edit_train, name='edit_train'),
    path('delete_train/<int:train_id>/', views.delete_train, name='delete_train'),
    path('create_story/', views.writestory, name='create_story'),
    
]