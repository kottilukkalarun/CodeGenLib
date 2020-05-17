from django.urls import path
from . import views
urlpatterns = [
    path("", views.HomeView.as_view(), name="home"),
    path("getresult", views.results, name="getresult"),
    path("viewall", views.viewall, name="viewall"),
    path("addreference", views.ReferenceBookCreate.as_view(), name="addreference"),
    path("signup", views.CreateeProfile.as_view(), name="signup"),
    path("editreference/<int:pk>", views.ReferenceBookEdit.as_view(), name="editreference"),
    path("deletereference/<int:pk>", views.ReferenceBookDelete.as_view(), name="deletereference"),
    path("detailView/<int:id>", views.detailView, name="detailView"),
    
]