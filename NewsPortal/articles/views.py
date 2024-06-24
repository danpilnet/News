from datetime import datetime
from django.views.generic import ListView, DetailView, CreateView, DeleteView, UpdateView
from news. models import Post
from. forms import PostForm
from django.views import View
from django.shortcuts import redirect, render


class ArticlesList(ListView):
    model = Post
    ordering = '-add_time'
    template_name = 'news.html'
    context_object_name = 'news'
    paginate_by = 10
    queryset = Post.objects.filter(pole_ar_ne='AR')


    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['time_now'] = datetime.utcnow()
        context['next_sale'] = None
        return context


class ArticlesDetail(DetailView):
    model = Post
    template_name = 'new.html'
    context_object_name = 'new'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['time_now'] = datetime.utcnow()
        context['next_sale'] = None
        return context




class ArticlesCreate(CreateView):
    form_class = PostForm
    model = Post
    template_name = 'news_create.html'
    context_object_name = 'create'
    success_url = '/articles/'
    permission_required = 'news.add_post'

    # def form_valid(self, form):
    #     post = form.save(commit=False)
    #     today = datetime.today()
    #     post_limit = Post.objects.filter(author=post.author, add_time__date=today).count()
    #     if post_limit >= 3:
    #         return render(self.request, 'news_limit.html', {'author': post.author})
    #     if self.request.path =='/articles/create/':
    #         post.pole_ar_ne = 'AR'
    #     post.save()
    #
    #     return super().form_valid(form)


class ArticlesEdit(UpdateView):
    form_class = PostForm
    model = Post
    template_name = 'news_edit.html'
    context_object_name = 'edit'
    success_url = '/articles/'
    permission_required = 'news.change_post'

class ArticlesDelete(DeleteView):
    model = Post
    template_name = 'news_delete.html'
    context_object_name = 'delete'
    success_url = '/articles/'