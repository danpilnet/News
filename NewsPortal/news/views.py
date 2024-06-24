from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from.models import Post
from datetime import datetime
from .filters import PostFilter
from .forms import PostForm
from django.contrib.auth.mixins import LoginRequiredMixin, PermissionRequiredMixin





class PostList(ListView):
    model = Post
    ordering = '-add_time'
    template_name = 'news.html'
    context_object_name = 'news'
    paginate_by =10
    queryset = Post.objects.filter(pole_ar_ne='NE')


    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['time_now'] = datetime.utcnow()
        return context




class PostDetail(DetailView):
    model = Post
    template_name = 'new.html'
    context_object_name = 'new'


    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['time_now'] = datetime.utcnow()
        return context



class PostSearch(ListView):
    model = Post
    template_name = 'news_search.html'
    context_object_name = 'search'


    def get_queryset(self):
        queryset = super().get_queryset()
        self.filterset = PostFilter(self.request.GET, queryset)
        return self.filterset.qs


    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['filterset'] = self.filterset
        context['time_now'] = datetime.now()
        return context



class PostCreate(PermissionRequiredMixin, CreateView, LoginRequiredMixin):
    form_class = PostForm
    model = Post
    template_name = 'news_create.html'
    context_object_name = 'create'
    success_url = '/news/'
    permission_required = 'news.add_post'


    # def form_valid(self, form):
        # post = form.save(commit=False)
        # today = datetime.today()
        # post_limit = Post.objects.filter(author=post.author, add_time__date=today).count()
        # if post_limit >= 3:
        #     return render(self.request, 'news_limit.html', {'author': post.author})
        # if self.request.path =='/news/create/':
        #     post.pole_ar_ne = 'NE'
        # post.save()
        # send_email_task.delay(post.pk)
        # return super().form_valid(form)



class PostEdit(PermissionRequiredMixin, UpdateView, LoginRequiredMixin):
    form_class = PostForm
    model = Post
    template_name = 'news_edit.html'
    context_object_name = 'edit'
    success_url = '/news/'
    permission_required = 'news.change_post'



class PostDelete(DeleteView):
    model = Post
    template_name = 'news_delete.html'
    context_object_name = 'delete'
    success_url = '/news/'
