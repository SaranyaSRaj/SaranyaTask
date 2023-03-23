from django.urls.conf import path
from.import views

urlpatterns = [
    path('add/', views.firstname_create_view, name='firstname_add'),
    path('<int:pk>/', views.firstname_update_view, name='firstname_change'),

    path('ajax/load-branch/', views.load_branch, name='ajax_load_branch'),
]