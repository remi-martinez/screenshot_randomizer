from django.shortcuts import render
from app.screenshot_finder import get_random_url


def homePageView(request):
    context = {
        'imgUrl': get_random_url()
    }
    return render(request, 'index.html', context)
