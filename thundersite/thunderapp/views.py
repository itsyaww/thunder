from django.shortcuts import render, get_object_or_404
from django.views.decorators.csrf import csrf_exempt


@csrf_exempt
def home(request):
    return render(request, 'thunderapp/base.html', {})