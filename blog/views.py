from django.shortcuts import render
from django.http import HttpResponse
from .forms import PostForm


# Create your views here.
def new_post(request):
    if request.method == "POST":
        form = PostForm(data=request.POST)
        if form.is_valid():
            post = form.save(commit=False)
            return redirect(post.get_absolute_url())
    else:
        form = PostForm()
    return render(request, 'blog/blog.html', {'form': form})


def about(request):
	return HttpResponse('<h1>About</h1>')