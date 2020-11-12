from django.shortcuts import render

def post_list(request):
    return render(request, 'blogDB/post_list.html', {})
