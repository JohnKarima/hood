from django.shortcuts import render, redirect
from django.contrib import messages
from django.http  import HttpResponse
from .models import Profile, User, Post, Neighbourhood, Business, Services
from .forms import UserRegisterForm, UserUpdateForm, ProfileUpdateForm, PostUploadForm, BizUploadForm, HoodForm
from django.contrib.auth.decorators import login_required
from cloudinary.forms import cl_init_js_callbacks
from django.core.exceptions import ObjectDoesNotExist
from django.http.response import Http404

@login_required
def index(request):
    users = User.objects.all()
    posts = Post.objects.all()
    return render(request, 'index.html', {"posts":posts[::-1], "users": users})

def register(request):
    if request.method == 'POST':
        form = UserRegisterForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            messages.success(request, f'Successfully created account created for {username}! Please log in to continue')
            return redirect('login')
    else:
        form = UserRegisterForm()
    return render(request, 'users/register.html', {'form':form})

@login_required
def profile(request):

    users = User.objects.exclude(id=request.user.id)
    if request.method == "POST":
        form = HoodForm(request.POST, request.FILES)
        if form.is_valid():
            hood = form.save(commit = False)
            hood.prof_ref = request.user.profile
            hood.save()
            messages.success(request, f'Successfully saved your Hood!')
            return redirect('index')
    else:
        form = HoodForm()
    return render(request, 'users/profile.html', {"form": form, "users": users})

@login_required
def update(request):
    if request.method == "POST":
        u_form = UserUpdateForm(request.POST, instance=request.user)
        p_form = ProfileUpdateForm(request.POST, request.FILES,
        instance=request.user.profile)
        if u_form.is_valid() and p_form.is_valid():
            u_form.save()
            p_form.save()
            messages.success(request, f'Successfully updated your account!')
            return redirect('profile')
    else:
        u_form = UserUpdateForm(instance=request.user)
        p_form = ProfileUpdateForm(instance=request.user.profile)
    context = {
        'u_form': u_form,
        'p_form': p_form
    }
    return render(request, 'users/update.html', context)

@login_required
def upload_post(request):
    users = User.objects.exclude(id=request.user.id)
    if request.method == "POST":
        form = PostUploadForm(request.POST, request.FILES)
        if form.is_valid():
            post = form.save(commit = False)
            post.prof_ref = request.user.profile
            post.save()
            messages.success(request, f'Successfully uploaded your Post!')
            return redirect('index')
    else:
        form = PostUploadForm()
    return render(request, 'upload_post.html', {"form": form, "users": users})

@login_required
def business(request):
    users = User.objects.all()
    businesses = Business.objects.all()
    return render(request, 'business.html', {"businesses":businesses[::-1], "users": users})

@login_required
def upload_business(request):
    users = User.objects.exclude(id=request.user.id)
    if request.method == "POST":
        form = BizUploadForm(request.POST, request.FILES)
        if form.is_valid():
            biz = form.save(commit = False)
            biz.prof_ref = request.user.profile
            biz.save()
            messages.success(request, f'Successfully uploaded your Business!')
            return redirect('business')
    else:
        form = BizUploadForm()
    return render(request, 'upload_business.html', {"form": form, "users": users})

@login_required
def search_results(request):
    if 'business' in request.GET and request.GET["business"]:
        search_term = request.GET.get("business")
        searched_businesses = Business.search_business(search_term)
        message = f"{search_term}"
        return render(request, 'search.html', {"message":message,"businesses": searched_businesses})
    else:
        message = "You haven't searched for any businesses yet"
    return render(request, 'search.html', {'message': message})

@login_required
def services(request):
    users = User.objects.all()
    services = Services.objects.all()
    return render(request, 'services.html', {"services":services[::-1], "users": users})