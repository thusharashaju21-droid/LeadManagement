

from django.urls import path

from business.views import LeadCreateView,LeadListView,LeadRetrieveUpdateDeleteView

urlpatterns = [

    # route to creating lead view
    path("leads/add/",LeadCreateView.as_view()),

    # route to listing lead
    path("leads/all/",LeadListView.as_view()),

    # route to lead retrieve,update,delete view
    path("leads/<int:pk>/",LeadRetrieveUpdateDeleteView.as_view()),
]