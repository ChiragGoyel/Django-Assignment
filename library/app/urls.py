from django.urls import path
from .import views

urlpatterns = [
    path('', views.HomePageView.as_view(), name = 'home'),
    path('library/create', views.BookCreateView.as_view(), name = "create"),
    path('library/update/<int:pk>', views.BookUpdateView.as_view(), name = "update"),
    path('library/delete/<int:pk>', views.BookDeleteView.as_view(), name = "delete"),
    path('signup/', views.SignUpView.as_view(), name = "signup"),
]
