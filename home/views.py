from django.shortcuts import render , redirect
from django.shortcuts import HttpResponse
from .models import Post, Author
from django.contrib.auth.forms import UserCreationForm
from django.contrib import messages
from django.views.generic import ListView





def register(request):
    if request.method == "POST":
        form = UserCreationForm(request.POST)
        if form.is_valid():
            print("abd")
            form.save()
            username = form.cleaned_data.get('username')
            messages.success(request, "Success. {}".format(username))
            return redirect('home')
    else:
        form = UserCreationForm()

    return render(request, 'users/register.html', {'form': form})


class BlogList(ListView):
    model = Post
    template_name = 'blog_list.html'
    context_object_name = 'post'
    paginate_by = 1




def home(request):
    post = Post.objects.all()
    context = {
        'post': post
    }
    return render(request, 'blog_list.html', context)






