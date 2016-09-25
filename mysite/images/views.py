from django.shortcuts import render
from django.contrib.auth.decorators import login_required

from django.http import JsonResponse
from django.views.decorators.http import require_POST
from django.views.decorators.csrf import csrf_exempt
from .forms import ImageCreateForm
from .models import Image

@login_required(login_url='/account/login/')
def list_images(request):
    form = ImageCreateForm()
    return render(request, 'images/listimages.html', {"form": form})

@login_required(login_url='/account/login/')
@require_POST
@csrf_exempt
def upload_photo(request):
    if request.method == "POST":
        form = ImageCreateForm(data=request.POST)
        if form.is_valid():
            cd = form.cleaned_data
            try:
                new_item = form.save(commit=False)
                new_item.user = request.user
                new_item.save()
                return JsonResponse({'status':"1"})
            except:
                return JsonResponse({'status':"0"})