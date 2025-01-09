from django.db.models.base import Model as Model
from django.db.models.query import QuerySet
from django.forms import BaseModelForm
from django.http import HttpResponse
from django.shortcuts import render
from django.urls import reverse, reverse_lazy
from django.views.generic import ListView, DetailView, CreateView, UpdateView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.core.exceptions import PermissionDenied
from .models import Cartoon, Review

def index_view(request):
    object_list = Cartoon.objects.all()
    return render(request, 'history/index.html', {'object_list': object_list})

class ListCartoonView(ListView):
    template_name = 'history/history_list.html'
    model = Cartoon

class DetailCartoonView(DetailView):
    template_name = 'history/history_detail.html'
    model = Cartoon

class CreateCartoonView(LoginRequiredMixin, CreateView):
    template_name ='history/history_create.html'
    model = Cartoon
    fields = ('era', 'thumbnail', 'year', 'description')
    success_url = reverse_lazy('list-cartoon')
    def form_valid(self, form):
        form.instance.user = self.request.user
        return super().form_valid(form)

class UpdateCartoonView(UpdateView):
    model = Cartoon
    fields = ('era', 'thumbnail', 'year', 'description')
    template_name = 'history/history_update.html'
    
    def get_success_url(self):
        return reverse('detail-cartoon', kwargs={'pk': self.object.id})

class CreateReview(LoginRequiredMixin, CreateView):
    model = Review
    fields = ('cartoon', 'title', 'content', 'rating', 'is_spoiler')
    template_name = 'history/review_form.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['cartoon'] = Cartoon.objects.get(pk=self.kwargs['cartoon_id'])
        return context
    
    def form_valid(self, form):
        form.instance.user = self.request.user
        return super().form_valid(form)
    def get_success_url(self):
        return reverse('detail-cartoon', kwargs={'pk': self.object.cartoon.id})