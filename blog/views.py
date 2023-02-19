from django.shortcuts import render


posts = [
    {
        'author':'Fernando DD',
        'title':'My Blog post 1',
        'content':'First post content',
        'date_posted':'February 15, 2023'
    },
    {
        'author':'Shiva DD',
        'title':'My Blog post 2',
        'content':'Second post content',
        'date_posted':'February 16, 2023'
    }
]


def home(request):

    context = {
        'posts': posts
    }
    
    return render(request, 'blog/home.html', context)


def about(request):
    return render(request, 'blog/about.html', {'title':'About'})
