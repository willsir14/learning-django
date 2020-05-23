from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

def post_list(request):
    index = ""
    with open('blog/templates/blog/index.html','r') as file:
        index = file.read()
    return HttpResponse(index)
    # return render(
    #     request=request,
    #     template_name='index.html',
    #     context={"title": "Hello Django"}
    # )
