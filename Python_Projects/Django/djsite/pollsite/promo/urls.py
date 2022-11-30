from django.urls import path
from .views import *
from django.views.decorators.cache import cache_page

urlpatterns = [
    path('', PromoHome.as_view(), name='home'),
    path('about/', about, name='about'),
    path('addpage/', AddPage.as_view(), name='add_page'),
    path('cotnact/', ContactFormView.as_view(), name='contact'),
    path('login/', LoginUser.as_view(), name='login'),
    path('logout/', logout_user, name='logout'),
    path('register/', RegisterUser.as_view(), name='register'),
    path('post/<slug:post_slug>/', ShowPost.as_view(), name='post'),
    path('cities/<slug:city_slug>/', PromoCities.as_view(), name='cities'),
    path('streets/str:street_slug/', show_streets, name='streets'),
    path('homes/int:home_slug/', show_homes, name='homes'),
    path('entrances/int:entrance_slug/', show_entrances, name='entrances'),
    path('flats/int:flat_slug/', show_flats, name='flats'),
]
