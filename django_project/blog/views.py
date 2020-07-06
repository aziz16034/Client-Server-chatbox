from django.shortcuts import render

# Create your views here.

posts =[
    {

    'author':'Abdul Aziz',
    'title': 'Blog Post 1',
    'content':'First post content',
    'date_posted': 'August 28 2020'
},
    {
   'author':'Abdul Rehman',
    'title': 'Blog Post 2',
    'content':'Second post content',
    'date_posted': 'August 29 2020'
}
]
def home(request):
    context = {
        'posts':posts,
    }
    return render(request, 'blog/home.html', context)



def about(request):
    return render(request, 'blog/about.html', {'title':'About'})

def contact_us(request):
    return render(request, 'blog/contact.html')


