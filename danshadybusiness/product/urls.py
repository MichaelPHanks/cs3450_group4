from django.urls import path
from . import views
app_name = 'product'


urlpatterns = [

    path('', views.loginTest, name = "loginTest"),
    path('addFunds/', views.addFunds, name='addFunds'),
    # path('account/', views.customUser, name = "customUser"),
    path('addCarPage/', views.addCarPage, name = 'addCarPage'),
    path('addCarPage/addCar/',views.addCar, name='addCar'),
    path('index/', views.index, name='index'),
    path('aboutUs/', views.aboutUs, name='aboutUs'),
    path('login/', views.login, name='login'),
    path('signup/', views.signup, name='signup'),
    path('service/', views.service, name='service'),
    path('availableCars/', views.availableCars, name="availableCars"),
    path('account/logout/', views.logoutPage, name = "logoutPage"),
    path('reservation/', views.reservation, name='reservation'),


    path('account/', views.account, name='account'),

    
    path('hire/', views.hirePage, name='hirePage'),
    path('createserviceticket/', views.createTicketPage, name='createTicketPage'),
    path('employeeHours/', views.employeeHours, name='employeeHours'),
    path('employeeHours/logHours/',views.logHours, name='logHours'),
    path('payEmployeePage/', views.payEmployeePage, name="payEmployeePage"),
    path('payEmployeePage/payAll/', views.payAll, name='payAll'),
    path('reservation/<int:car_id>/<str:startDate>/<str:endDate>/', views.displayCar, name = 'displayCar'),
    path('reservation/<int:car_id>/reserveCar/', views.reserveCar, name = 'reserveCar'),
    path('inventory/',views.inventory,name = "inventory"),
    path('overdueReservations/',views.overdueReservations, name = "overdueReservations"),
    path('overdueReservations/lojackCar/',views.lojackCar, name='lojackCar'),
    path('account/currentReservations/',views.currentReservations, name = "currentReservations"),
    path('account/currentReservations/returnCar/',views.returnCar,name = "returnCar"),
    path('chatPage', views.chatPage, name = 'chatPage'),
    path('chatPage/<int:user_id>',views.customChat, name = "customChat"),
    path('chatPage/<int:user_id>/createChat',views.createChat, name = "createChat"),
    path('account/editProfile', views.editProfile, name = "editProfile"),
    path('account/editProfile/uploadProfilePic', views.uploadProfilePic, name = "uploadProfilePic"),




]