from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from users.models import User, Pet
from forum.models import Forum
from blog.models import Blog
from announcements.models import AdoptPet, FoundedPet, LostPet

# @login_required(login_url='login')
def admin_dashboard(request):
    profile = request.user
    pet_lover_account_count = User.objects.all().filter(user_type='petlover').count()
    business_account_count = User.objects.all().filter(user_type='business').count()
    pet_count = Pet.objects.all().count()
    forum_count = Forum.objects.all().count()
    blog_count = Blog.objects.all().count()
    adopt_count = AdoptPet.objects.all().count()
    founded_count = FoundedPet.objects.all().count()
    lost_count = LostPet.objects.all().count()

    context = {'pl_count': pet_lover_account_count, 'busi_count': business_account_count,
               'forum_count': forum_count, 'blog_count': blog_count, 'adopt_count': adopt_count,
               'founded_count': founded_count, 'lost_count':lost_count, 'pet_count': pet_count, 'profile': profile}
    return render(request, 'dashboard/dashboard.html', context)


# @login_required(login_url='login')
def admin_dashboard_petlover(request):
    profile = request.user
    pet_lover_accounts = User.objects.all().filter(user_type='petlover')

    context= {'petlovers': pet_lover_accounts, 'profile': profile}
    return render(request, 'dashboard/dashboard-petlover.html', context)

# @login_required(login_url='login')
def admin_dashboard_business(request):
    profile = request.user
    business_accounts = User.objects.all().filter(user_type='business')

    context = {'business': business_accounts, 'profile': profile}
    return render(request, 'dashboard/dashboard-business.html', context)

# @login_required(login_url='login')
def admin_dashboard_blogs(request):
    profile = request.user
    blogs = Blog.objects.all()

    context = {'blogs': blogs, 'profile': profile}
    return render(request, 'dashboard/dashboard-blogs.html', context)

# @login_required(login_url='login')
def admin_dashboard_forums(request):
    profile = request.user
    forums = Forum.objects.all()

    context = {'forums': forums, 'profile': profile}
    return render(request, 'dashboard/dashboard-forums.html', context)

# @login_required(login_url='login')
def admin_dashboard_adopted(request):
    profile = request.user
    adopted = AdoptPet.objects.all()

    context = {'adopted': adopted, 'profile': profile}
    return render(request, 'dashboard/dashboard-adopted.html', context)

# @login_required(login_url='login')
def admin_dashboard_founded(request):
    profile = request.user
    founded = FoundedPet.objects.all()

    context = {'founded': founded, 'profile': profile}
    return render(request, 'dashboard/dashboard-founded.html', context)

# @login_required(login_url='login')
def admin_dashboard_lost(request):
    profile = request.user
    lost = LostPet.objects.all()

    context = {'lost': lost, 'profile': profile}
    return render(request, 'dashboard/dashboard-lost.html', context)

# @login_required(login_url='login')
def admin_dashboard_announce_list(request):
    return render(request, 'dashboard/dashboard-list-announce.html')
