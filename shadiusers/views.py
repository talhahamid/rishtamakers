from django.core.checks import messages
from django.contrib import messages
from django.shortcuts import render, redirect,get_object_or_404
from django.urls import reverse
from django.contrib.auth.models import User, auth
from . models import User,Personal,Profilepic ,Subscribe,ProfileView
from django.contrib.auth.hashers import check_password
from django.conf import settings
import os
from django.contrib.auth import logout as django_logout
from django.utils import timezone
from datetime import timedelta
# Create your views here.

def home(request):
    return render(request, 'home.html')


def loginuser(request):
    if request.method == "POST":
        mobile = request.POST['mobile']
        password = request.POST['password']
        print(mobile)
        user = User.objects.get(mobile=mobile)
        if int(mobile)==int(user.mobile) and password==user.password:
            request.session['user_id'] = user.id
            try:
                user_id=request.session.get('user_id')
                user=User.objects.get(id=user_id)
                user_profile = Personal.objects.get(user=user)
                newurl = reverse('editpersonaldetails')
                return redirect(newurl)
            except Personal.DoesNotExist:
                url = reverse('personaldetails')
                return redirect(url)
    return render(request, 'loginuser.html')    


def logout(request):
    django_logout(request)    
    return render(request,'loginuser.html')

#signup

def register(request):
    if request.method == 'POST':
        name = request.POST.get('name',False)
        mobile = request.POST['mobile']
        password=request.POST['password']
        city = request.POST['city']
        state = request.POST['state']
        religion = request.POST['religion']
        gender = request.POST.get('gender',False)
        looking_for = request.POST.get('looking_for',False)
        marital_status = request.POST.get('marital_status',False)
        user = User(name=name, mobile=mobile, password=password, city=city, state=state, religion=religion, gender=gender, looking_for=looking_for, marital_status=marital_status)
        user.save()
        return render(request, 'loginuser.html') 
    else:
        return render(request, 'register.html')
       

        
def profile(request,id):
    user= User.objects.get(id=id)
    personaldetail=Personal.objects.get(user=user)
    try:
        profilepic=Profilepic.objects.get(user=user)
        return render(request, 'profile.html',{'user':user,'personaldetail':personaldetail,'profilepic':profilepic}) 
    except Profilepic.DoesNotExist:
        return render(request, 'profile.html',{'user':user,'personaldetail':personaldetail})
       
def personaldetails(request):
    try:
        user_id=request.session.get('user_id')
        user=User.objects.get(id=user_id)
        user_profile = Personal.objects.get(user=user)
        newurl = reverse('editpersonaldetails')
        return redirect(newurl)
    except Personal.DoesNotExist:
        if request.method == 'POST':
            education = request.POST['education']
            occupation = request.POST['occupation']
            status = request.POST['status']
            mother_tongue = request.POST['mother_tongue'] 
            religion_category = request.POST.get('religion_category',False)
            cast_category = request.POST['cast_category']
            income = request.POST['income']
            height = request.POST['height']
            weight = request.POST['weight']
            color = request.POST['color']
            user_id=request.session.get('user_id')
            user=User.objects.get(id=user_id)
            add = Personal(user=user,education=education, occupation=occupation,status=status, mother_tongue=mother_tongue,religion_category=religion_category,cast_category=cast_category,income=income,height=height,weight=weight,color=color )
            add.save()
            url = reverse('profile',kwargs={'id':user_id})
            return redirect(url)
    else:  
        return render(request, 'personaldetails.html')

def editpersonaldetails(request):
    user_id=request.session.get('user_id')
    user=User.objects.get(id=user_id)
    personal=Personal.objects.get(user=user)
    return render(request,'editpersonaldetails.html',{'personal':personal})

def updatepersonaldetails(request,id):
    personal_details=Personal.objects.get(id=id)
    personal_details.education = request.POST['education']
    personal_details.occupation = request.POST['occupation']
    personal_details.status = request.POST['status']
    personal_details.mother_tongue = request.POST['mother_tongue']
    personal_details.religion_category = request.POST.get('religion_category', False)
    personal_details.cast_category = request.POST['cast_category']
    personal_details.income = request.POST['income']
    personal_details.height = request.POST['height']
    personal_details.weight = request.POST['weight']
    personal_details.color = request.POST['color']
    personal_details.save()
    url=reverse('profile',kwargs={'id':id})
    return redirect(url)

def pics(request):
    return render(request,'addpics.html')

def addpics(request):
    user_id = request.session.get('user_id')
    user = User.objects.get(id=user_id)
    
    # Check if the user already has profile pictures
    profile = Profilepic.objects.filter(user=user).first()
    if profile:
        if request.method == "POST":
            # Update existing profile pictures
            profilepic1 = request.FILES.get('pic1')
            profilepic2 = request.FILES.get('pic2')
            profilepic3 = request.FILES.get('pic3')    
            profilepic4 = request.FILES.get('pic4')
            
            if all([profilepic1, profilepic2, profilepic3, profilepic4]):
                # Update the existing profile pictures
                profile.profilepic1 = profilepic1
                profile.profilepic2 = profilepic2
                profile.profilepic3 = profilepic3
                profile.profilepic4 = profilepic4
                profile.save()
        url = reverse('profile', kwargs={'id': user_id})
        return redirect(url)

    if request.method == "POST":
        profilepic1 = request.FILES.get('pic1')
        profilepic2 = request.FILES.get('pic2')
        profilepic3 = request.FILES.get('pic3')    
        profilepic4 = request.FILES.get('pic4')
        
        if all([profilepic1, profilepic2, profilepic3, profilepic4]):
            profile = Profilepic(user=user, profilepic1=profilepic1, profilepic2=profilepic2, profilepic3=profilepic3, profilepic4=profilepic4)
            profile.save()
            
        # Redirect to the profile page after saving the profile pictures
        url = reverse('profile', kwargs={'id': user_id})
        return redirect(url)
    
    return render(request, 'addpics.html')



def profileslist(request):
    user_id=request.session.get('user_id')
    user=User.objects.get(id=user_id)
    looking_for=user.looking_for
    users=User.objects.filter(gender=looking_for)
    return render(request,'profilelist.html',{'users':users})



def userprofile(request, id):
    user = get_object_or_404(User, id=id)
    personaldetail = get_object_or_404(Personal, user=user)
    
    # Get the logged-in user
    user_id = request.session.get('user_id')
    logged_in_user = get_object_or_404(User, id=user_id)

    try:
        profilepic = Profilepic.objects.get(user=user)
    except Profilepic.DoesNotExist:
        profilepic = None

    try:
        subscription = Subscribe.objects.get(user=logged_in_user)
    except Subscribe.DoesNotExist:
        subscription = None

    # Check if the profile has been previously viewed
    previously_viewed = ProfileView.objects.filter(user=logged_in_user, viewed_profile=user).exists()
    show_data = previously_viewed
    error_message = None

    if request.method == 'POST':
        if subscription:
            if 'show_data' in request.POST:
                if subscription.plan == 'free' and ProfileView.objects.filter(user=logged_in_user).count() >= 1:
                    error_message = f"You have reached the maximum profile limit of {subscription.users} for the {subscription.plan} plan."
                else:
                    show_data = True
                    if not previously_viewed:
                        ProfileView.objects.create(user=logged_in_user, viewed_profile=user)
        else:
            if 'subscribe' in request.POST:
                return redirect('subscribe')  # Redirect to your subscription page

    context = {
        'user': user,
        'personaldetail': personaldetail,
        'profilepic': profilepic,
        'subscription': subscription,
        'show_data': show_data,
        'error_message': error_message,
    }

    return render(request, 'userprofile.html', context)





# def userprofile(request, id):
#     user = get_object_or_404(User, id=id)
#     personaldetail = get_object_or_404(Personal, user=user)
    
#     # Get the logged-in user
#     user_id = request.session.get('user_id')
#     logged_in_user = get_object_or_404(User, id=user_id)

#     try:
#         profilepic = Profilepic.objects.get(user=user)
#     except Profilepic.DoesNotExist:
#         profilepic = None

#     try:
#         subscription = Subscribe.objects.get(user=logged_in_user)
#     except Subscribe.DoesNotExist:
#         subscription = None

#     # Check show count from session
#     show_count = request.session.get('show_count', 0)
#     error_message = None
#     show_data = False

#     if request.method == 'POST':
#         if subscription:
#             if 'show_data' in request.POST:
#                 if subscription.plan == 'free' and show_count >= 1:
#                     error_message = f"You have reached the maximum profile limit of {subscription.users} for the {subscription.plan} plan, now you cant see hidden data."
#                 else:
#                     print(show_count)
#                     show_data = True
#                     request.session['show_count'] = show_count + 1
#         else:
#             if 'subscribe' in request.POST:
#                 return redirect('subscribe')  # Redirect to your subscription page

#     context = {
#         'user': user,
#         'personaldetail': personaldetail,
#         'profilepic': profilepic,
#         'subscription': subscription,
#         'show_data': show_data,
#         'error_message': error_message,
#     }

#     return render(request, 'userprofile.html', context)




def subscribe(request,id):
    user_id=request.session.get('user_id')
    user=User.objects.get(id=user_id)
    return render(request,'subscribe.html',{'user':user,'id':id})    



def freeplan(request,id):
    user_id=request.session.get('user_id')
    user=User.objects.get(id=user_id)   
    subscription=Subscribe(user=user,plan='free',duration=7,users=1,price=0)
    subscription.save()
    url= reverse('userprofile',kwargs={'id':id})
    return redirect(url)




def myplans(request, id):
    user = User.objects.get(id=id)
    subscriptions = Subscribe.objects.filter(user=user)
    expiry_dates = []
    for subscription in subscriptions:
        expiry_date = subscription.createdat + timedelta(days=subscription.duration)
        expiry_dates.append(expiry_date)
    return render(request, 'myplans.html', {'subscriptions': subscriptions, 'expiry_dates': expiry_dates, 'user': user})



def profiles_list(request):
    filters = {
        'education': request.GET.get('education'),
        'occupation': request.GET.get('occupation'),
        'status': request.GET.get('status'),
        'mother_tongue': request.GET.get('mother_tongue'),
        'religion_category': request.GET.get('religion_category'),
        'cast_category': request.GET.get('cast_category'),
        'income': request.GET.get('income'),
        'height': request.GET.get('height'),
        'weight': request.GET.get('weight'),
        'color': request.GET.get('color'),
    }
    filter_args = {k: v for k, v in filters.items() if v}
    user_id=request.session.get('user_id')
    user=User.objects.get(id=user_id)
    profiles = Personal.objects.filter(**{f"{k}__icontains": v for k, v in filter_args.items()}).exclude(user=user)
    context = {
        'profiles': profiles,
        'filters': filters,
    } 
    return render(request, 'profilelist.html', context)