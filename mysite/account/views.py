from django.shortcuts import render
from django.http import HttpResponse
from django.contrib.auth import authenticate, login
from .forms import LoginForm, UserRegistrationForm, UserEditForm, ProfileEditForm
from .models import Profile 
from django.contrib.auth.decorators import login_required
from django.views.decorators.csrf import csrf_exempt
from django.contrib.auth.models import User

# Create your views here.
def user_login(request):
	if request.method == "POST":
		form = LoginForm(request.POST)
		if form.is_valid():
			cd = form.cleaned_data
			user = authenticate(username=cd['username'], password=cd['password'])
			if user:
				login(request, user)
				return HttpResponse('Authenticated successfully')
			else:
				return HttpResponse('Disabled account')
		else:
			return HttpResponse('Invalid login')

	if request.method == "GET":
		form = LoginForm()
	return render(request, "account/login.html", {"form": form})

def register(request):
	if request.method == "POST":
		user_form = UserRegistrationForm(request.POST)
		if user_form.is_valid():
			new_user = user_form.save(commit=False)
			new_user.set_password(user_form.cleaned_data['password'])
			new_user.save()
			profile = Profile.objects.create('new_user=new_user',)
			return render(request, 'account/register_done.html', {'new_user':new_user})

	else:
		user_form = UserRegistrationForm()
	return render(request, "account/register.html", {"user_form":user_form})

@login_required(login_url="/account/login/")
@csrf_exempt
def edit(request):
    if request.method == "POST":
        user_user = User.objects.get(username=request.user)
        user_profile = Profile.objects.get(user=request.user)
        data = request.POST
        user_user.first_name = data["first_name"]
        user_user.last_name = data['last_name']
        user_user.email = data['email']
        type(user_user.email)
        user_user.save()
        user_profile.phone = data['phone']
        user_profile.date_birth = data['date_birth']

        user_profile.save()
        return HttpResponse("1")

    if request.method == "GET":
        user_form = UserEditForm(instance=request.user)
        profile_form = ProfileEditForm(instance=request.user)
    return render(request, "account/editpic.html", {"profile_form":profile_form, "user_form":user_form})

@login_required(login_url='/account/login/')
@csrf_exempt
def upload_img(request):
	if request.method == "POST":
		img = request.POST['img']
		user_form = Profile.objects.get(user=request.user)
		user_form.photo = img
		user_form.save()
		return HttpResponse("1")