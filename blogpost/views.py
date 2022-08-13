from django.views.generic import ListView, DetailView, CreateView, DeleteView, UpdateView
from django.urls import reverse_lazy

from .models import BlogModel

# Create your views here.
# class-based view方式での実装
# 一覧画面
class BlogList(ListView):
    template_name = 'list.html'
    model = BlogModel

# 詳細画面
class BlogDetail(DetailView):
    template_name = 'detail.html'
    model = BlogModel

# 投稿画面
class BlogCreate(CreateView):
    template_name = 'create.html'
    model = BlogModel
    fields = ('title', 'content', 'category')
    success_url = reverse_lazy('list')

# 削除画面
class BlogDelete(DeleteView):
    template_name = 'delete.html'
    model = BlogModel
    success_url = reverse_lazy('list')

# 編集画面
class BlogUpdate(UpdateView):
    template_name = 'update.html'
    model = BlogModel
    fields = ('title', 'content', 'category')
    success_url = reverse_lazy('list')
