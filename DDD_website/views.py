from django.shortcuts import render
from django.views import generic
from scraping.models import RedditPostData, RedditReplyData

# Create your views here.
class HomePageView(generic.ListView):
    template_name = 'home.html'
    context_object_name = 'Reddit Posts' 
    # assign "News" object list to the object "articles"
    # pass news objects as queryset for listview
    def get_queryset(self):
        return RedditPostData.objects.all()
    
def all_posts(request):
    post_lists = RedditPostData.objects.all()
    return render(request, 'home.html',
                  {'post_lists': post_lists})

def explore(request):
    post_lists = RedditPostData.objects.all()
    return render(request, 'home.html',
                  {'post_lists': post_lists})

def about(request):
    return render(request, 'about.html')