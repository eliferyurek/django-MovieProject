from django.urls import path
from . import views


urlpatterns = [
    path('register/', views.registerPage, name="register"),
    path('login/', views.loginPage, name="login"),
    path('logout/', views.logoutUser, name="logout"),

    path('', views.home, name="home"),
    path('user/', views.movie, name="user-page"),
    path('movie/', views.movie, name="movies"),
    path('customer/<str:pk_test>/', views.customer, name="customer"),

    path('account/', views.accountSettings, name="account"),
    path('cart/', views.cart, name="cart"),
    path('address/', views.addressCustomer, name="address"),

    path('createmovie/', views.createMovie, name="createmovie"),
    path('updatemovie/<str:pk_movie>/', views.updateMovie, name="updatemovie"),
    path('deletemovie/<str:pk_movie>/', views.deleteMovie, name="deletemovie"),
    path('movie/movieview/<str:pk_movie>/', views.movieView, name="movieview"),

    path('createcustomer/', views.createCustomer, name="createcustomer"),
    path('updatecustomer/<str:pk_customer>', views.updateCustomer, name="updatecustomer"),
    path('deletecustomer/<str:pk_customer>', views.deleteCustomer, name="deletecustomer"),

    path('updatecart/', views.updateCart, name="updatecart"),
    path('processorder/', views.processOrder, name="processorder"),

    path('store/', views.store, name="store"),
    path('addstore/', views.addStore, name="addstore"),
    path('updatestore/<str:pk_store>/', views.updateStore, name="updatestore"),
    path('deletestore/<str:pk_store>/', views.deleteStore, name="deletestore"),

    path('addactor/', views.addActor, name="addactor"),
    path('updateactor/<str:pk_actor>/', views.updateActor, name="updateactor"),
    path('deleteactor/<str:pk_actor>/', views.deleteActor, name="deleteactor"),

    path('adddirector/', views.addDirector, name="adddirector"),
    path('updatedirector/<str:pk_director>/', views.updateDirector, name="updatedirector"),
    path('deletedirector/<str:pk_director>/', views.deleteDirector, name="deletedirector"),

]