from . import views
from django.urls import path
urlpatterns = [
    path("",views.home,name="home"),
    path("search-hole/",views.search_hole,name="search-hole"),
    path("selected_product/<int:id>",views.selected_product,name="selected_product"),
    path("sign-up/",views.showformat,name="sign-up"),
    path("sign-in/",views.loginformat,name="sign-in"),
    path("sign-out/",views.logoutformat,name="sign-out"),    
    path("buy/<int:id>",views.buy,name="buy"),    
    path("cart/<int:id>",views.cart,name="cart"),
    path("address/",views.address,name="address"),
    path("address-form/",views.address_form,name="address-form"),
    path("set_default/<int:id>",views.set_default,name="set_default"),
    path("remove/<int:id>",views.remove_address,name="remove_address"),
    path('remove_cart/<int:id>',views.remove_cart,name="remove_cart"),
    path('show_cart/',views.show_cart,name="showcart"),
    path('order_placed/',views.order_placed,name="orderplaced"),
    path('placeorder/<int:id>',views.place_order,name="place_order"),
    path('cancel_order/<int:id>',views.cancel_order,name="cancel_order")   
]
