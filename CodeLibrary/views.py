from django.shortcuts import render, redirect, get_object_or_404
from .models import ReferenceBook
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic.list import ListView
from django.urls import reverse_lazy


# Create your views here.

# def home(request):
#     return render(request, "index.html")

def results(request):

    if not request.POST['searchQuery'] == "":

        context = {
            "searchQuery": request.POST['searchQuery'],
        }



        return render(request, "result.html", context)
    else:
        return redirect("home")

def viewall(request):
    context = {
        "database": ReferenceBook.objects.all()
    }

    return render(request, "view_all.html", context)

def detailView(request, id):
    context = {
        "data": get_object_or_404(ReferenceBook, pk=id)
    }
    return render(request,"detailed_view.html", context)


class HomeView(LoginRequiredMixin, ListView):
    template_name = "index.html"
    model = ReferenceBook
    context_object_name = "data"


class ReferenceBookCreate(CreateView):
    model = ReferenceBook
    template_name = "add_data.html"
    fields = ['article_title','article_topic_type','article_content','article_updated_by']
    success_url = "addreference"

class ReferenceBookEdit(UpdateView):
    model = ReferenceBook
    template_name = "edit_data.html"
    fields = ['article_title','article_topic_type','article_content','article_updated_by']
    success_url = "/viewall"

class ReferenceBookDelete(DeleteView):
    model = ReferenceBook
    template_name = "delete_data.html"
    # fields = ['article_title','article_content','article_updated_by']
    success_url = "/viewall"
class CreateeProfile(CreateView):
    form_class = UserCreationForm
    template_name  = 'registration/signup.html'
    success_url = reverse_lazy("home")