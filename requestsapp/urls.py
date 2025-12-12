from django.urls import path
from .views import StudentRequestsView, RequestDetailView

# URL patterns for the requestsapp API
urlpatterns = [

    # GET → list all requests for the logged-in student
    # POST → create a new service request
    path('', StudentRequestsView.as_view(), name='my-requests'),

    # GET → retrieve a specific request by its ID (primary key)
    path('<int:pk>/', RequestDetailView.as_view(), name='request-detail'),
]