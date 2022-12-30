
from django.urls import path
from .views import StaringPageView, AllPostView, SingelPostView,ReadLaterView

urlpatterns = [
    path("",StaringPageView.as_view(),name='starting_pages' ),
    path("posts",AllPostView.as_view() ,name='post_pages'),
    path("posts/<slug>", SingelPostView.as_view(),name='post_detail_pages'),
    path('read-later',ReadLaterView.as_view(),name='read_later')
]
