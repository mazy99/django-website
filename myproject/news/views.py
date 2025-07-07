from django.shortcuts import render, redirect
from .models import News
from .forms import NewsForm
from django.views.generic import DetailView, UpdateView, DeleteView
from django.urls import reverse_lazy


def news_index(request):
    news_list = News.objects.order_by('-date')
    return render(request, 'news/news.html', {'news_list':news_list})


class NewsDetail(DetailView):
    model = News
    template_name = 'news/news_detail.html'
    context_object_name = 'news_detail'

class NewsDeleteView(DeleteView):
    model = News
    template_name = 'news/news_delete.html'
    success_url = reverse_lazy('news_index')


class NewsUpdateView(UpdateView):
    model = News
    template_name = 'news/news_update.html'
    form_class = NewsForm

def create_news(request):
    error = ''
    if request.method == 'POST':
        form = NewsForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('news_index')
        else:
            error = 'Невeрная форма'
    form = NewsForm()

    data = {
        'form': form, 
        'error': error
    }
    return render(request, 'news/create_news.html', data)