from django.core.checks import messages
from django.contrib import messages
from django.shortcuts import render, redirect
from django.contrib.auth.models import User, auth
from . models import Demo,Users,Religion,Religion_category,Status,Education,Occupation,Mothertongue,Admin
#from shadiadmin.middleware.auth import auth_middleware
from django.utils.decorators import method_decorator 

# Create your views here.

def index(request):
    demo=Demo.objects.all().order_by('id').values()
    return render(request, 'index1.html', {'demo':demo})

def insert(request):
    if request.method == "POST":
        name= request.POST['name']
        add=Demo(name=name)
        add.save()
    return render(request, 'insert.html')    

def edit(request,id): 
    edits=Demo.objects.filter(id=id)
    return render(request, 'edit.html',{'edits':edits})

def update(request,id):
    if request.method == "POST": 
        name= request.POST['name']
        edit=Demo.objects.filter(id=id).update(name=name)
    return render(request,'update.html')    

def delete(request,id):
    dele=Demo.objects.get(id=id)
    dele.delete()
    return render(request, 'delete.html')        


def home(request):
    return render(request, 'home.html')

def login(request):
    if request.method == 'POST':
        uid = request.POST['uid']
        password = request.POST['uid']
        admin = Admin.objects.get(uid=uid)
        if Users.objects.filter(uid = uid).exists():           
           
                return render(request, 'home.html')
        else:
            messages.info(request, 'invalid credentials')
            #print("hiiiiii")
            return redirect('login')
    else:    
        return render(request,'login.html')



    return render(request, 'login.html')

# Users, 
def Usersindex(request):
    users=Users.objects.all().order_by('id').values()
    return render(request, 'users.html', {'users':users})

def Usersinsert(request):
    if request.method == "POST":
        name= request.POST['name']
        mobile=request.POST['mobile']
        city=request.POST['city']
        state=request.POST['state']
        address=request.POST['address']
        dob=request.POST['dob']
        gender=request.POST['gender']
        religion=request.POST['religion']
        status=request.POST['status']
        add=Users(name=name,mobile=mobile,city=city,state=state,address=address,dob=dob,gender=gender,religion=religion,status=status)
        add.save()
        return redirect('Usersindex')
    else:
        return render(request, 'usersadd.html')    
    

def Usersedit(request,id): 
    edits=Users.objects.filter(id=id)
    return render(request, 'usersedit.html',{'edits':edits})

def Usersupdate(request,id):
    if request.method == "POST": 
        name= request.POST['name']
        mobile=request.POST['mobile']
        city=request.POST['city']
        state=request.POST['state']
        address=request.POST['address']
        dob=request.POST['dob']
        gender=request.POST['gender']
        religion=request.POST['religion']
        status=request.POST['status']
        edit=Users.objects.filter(id=id).update(name=name,mobile=mobile,city=city,state=state,address=address,dob=dob,gender=gender ,religion=religion,status=status)
        user=Users.objects.all().order_by('id').values()
    #return render(request,'users.html',{'user':user})    
    return redirect('Usersindex')

def Usersdelete(request,id):
    dele=Users.objects.get(id=id)
    dele.delete()
    user=Users.objects.all().order_by('id').values()
    return render(request, 'users.html',{'user':user})        

                         
#userview

def userview(request):
    user=Users.objects.all()
    rel=Religion.objects.all()
    rc=Religion_category.objects.all()
    status=Status.objects.all()
    edu=Education.objects.all()
    ocu=Occupation.objects.all()
    mt=Mothertongue.objects.all()
    return render(request, 'userview.html',{'user':user,'rel':rel,'rc':rc,'status':status,'edu':edu,'ocu':ocu,'mt':mt})

 # Religion,

def Religionindex(request):
    rel=Religion.objects.all().order_by('id').values()
    return render(request, 'religion.html', {'rel':rel})

def Religioninsert(request):
    if request.method == "POST":
        name= request.POST['name']
        add=Religion(name=name)
        add.save()
        return redirect('Religionindex')
    else:
        return render(request, 'religionadd.html') 
    

def Religionedit(request,id): 
    redits=Religion.objects.filter(id=id)
    return render(request, 'religionedit.html',{'redits':redits})

def Religionupdate(request,id):
    if request.method == "POST": 
        name= request.POST['name']
        redit=Religion.objects.filter(id=id).update(name=name)
        #rel=Religion.objects.all().order_by('id').values()
    #return render(request,'religion.html')    
    return redirect('Religionindex')

def Religiondelete(request,id):
    rdele=Religion.objects.get(id=id)
    rdele.delete()
    rel=Religion.objects.all().order_by('id').values()
    return render(request, 'religion.html',{'rel':rel})        



 # Religion_category,
 
def Religion_categoryindex(request):
    rc=Religion_category.objects.all().order_by('id').values()
    return render(request, 'religion_category.html', {'rc':rc})

def Religion_categoryinsert(request):
    if request.method == "POST":
        religion_name= request.POST['religion_name']
        sub_category= request.POST['sub_category']
        add=Religion_category(religion_name=religion_name,sub_category=sub_category)
        add.save()
        return redirect('Religion_categoryindex')
    else:    
        return render(request, 'Religion_categoryadd.html')    
    

def Religion_categoryedit(request,id): 
    rcedits=Religion_category.objects.filter(id=id)
    return render(request, 'religion_categoryedit.html',{'rcedits':rcedits})

def Religion_categoryupdate(request,id):
    if request.method == "POST": 
        religion_name= request.POST['religion_name']
        sub_category= request.POST['sub_category']
        rcedit=Religion_category.objects.filter(id=id).update(religion_name=religion_name,sub_category=sub_category)
        rc=Religion_category.objects.all().order_by('id').values()
    #return render(request,'religion_category.html',{'rc':rc})    
    return redirect('Religion_categoryindex')

def Religion_categorydelete(request,id):
    rcdele=Religion_category.objects.get(id=id)
    rcdele.delete()
    rc=Religion_category.objects.all().order_by('id').values()
    return render(request, 'religion_category.html',{'rc':rc})        



 # Status,

def Statusindex(request):
    status=Status.objects.all().order_by('id').values()
    return render(request, 'status.html', {'status':status})

def Statusinsert(request):
    if request.method == "POST":
        name= request.POST['name']
        add=Status(name=name)
        add.save()
        return redirect('Statusindex')
    else:
        return render(request, 'statusadd.html')    
    

def Statusedit(request,id): 
    sedits=Status.objects.filter(id=id)
    return render(request, 'statusedit.html',{'sedits':sedits})

def Statusupdate(request,id):
    if request.method == "POST": 
        name= request.POST['name']
        sedit=Status.objects.filter(id=id).update(name=name)
        status=Status.objects.all().order_by('id').values()
    #return render(request,'statusedit.html',{'status':status})
    return redirect('Statusindex')    

def Statusdelete(request,id):
    dele=Status.objects.get(id=id)
    dele.delete()
    status=Status.objects.all().order_by('id').values()
    return render(request, 'status.html',{'status':status}) 


 # Education,
 
def Educationindex(request):
    edu=Education.objects.all().order_by('id').values()
    return render(request, 'education.html', {'edu':edu})

def Educationinsert(request):
    if request.method == "POST":
        name= request.POST['name']
        add=Education(name=name)
        add.save()
        return redirect('Educationindex')
    else:
        return render(request, 'educationadd.html')    
    

def Educationedit(request,id): 
    ededits=Education.objects.filter(id=id)
    return render(request, 'educationedit.html',{'ededits':ededits})

def Educationupdate(request,id):
    if request.method == "POST": 
        name= request.POST['name']
        ededit=Education.objects.filter(id=id).update(name=name)
        edu=Education.objects.all().order_by('id').values()        
    #return render(request,'education.html',{'edu':edu}) 
    return redirect('Educationindex')

def Educationdelete(request,id):
    eddele=Education.objects.get(id=id)
    eddele.delete()
    edu=Education.objects.all().order_by('id').values()
    return render(request, 'education.html',{'edu':edu})        



 # Occupation,

def Occupationindex(request):
    ocu=Occupation.objects.all().order_by('id').values()
    return render(request, 'occupation.html', {'ocu':ocu})

def Occupationinsert(request):
    if request.method == "POST":
        name= request.POST['name']
        sub_category=request.POST['sub_category']
        add=Occupation(occupation_name=name,sub_category=sub_category)
        add.save()
        return redirect('Occupationindex')
    else:
        return render(request, 'occupationadd.html')   

def Occupationedit(request,id): 
    ocedits=Occupation.objects.filter(id=id)
    return render(request, 'occupationedit.html',{'ocedits':ocedits})

def Occupationupdate(request,id):
    if request.method == "POST": 
        name= request.POST['name']
        sub_category=request.POST.get['sub_category']
        oedit=Occupation.objects.filter(id=id).update(name=name,sub_category=sub_category)
        ocu=Occupation.objects.all().order_by('id').values()    
    #return render(request,'occupation.html',{'ocu':ocu})    
    return redirect('Occupationindex')

def Occupationdelete(request,id):
    odele=Occupation.objects.get(id=id)
    odele.delete()
    ocu=Occupation.objects.all().order_by('id').values() 
    return render(request, 'occupation.html',{'ocu':ocu})        





 # Mothertongue   
 
def Mothertongueindex(request):
    mt=Mothertongue.objects.all().order_by('id').values()
    return render(request, 'mothertongue.html', {'mt':mt})

def Mothertongueinsert(request):
    if request.method == "POST":
        name= request.POST['name']
        add=Mothertongue(name=name)
        add.save()
        return redirect('Mothertongueindex')
    else:
        return render(request, 'mothertongueadd.html')    
    

def Mothertongueedit(request,id): 
    mtedits=Mothertongue.objects.filter(id=id)
    return render(request, 'mothertongueedit.html',{'mtedits':mtedits})

def Mothertongueupdate(request,id):
    if request.method == "POST": 
        name= request.POST['name']
        mtedit=Mothertongue.objects.filter(id=id).update(name=name)
        mt=Mothertongue.objects.all().order_by('id').values()    
    #return render(request,'mothertongue.html',{'mt':mt})  
    return redirect('Mothertongueindex')

def Mothertonguedelete(request,id):
    mtdele=Mothertongue.objects.get(id=id)
    mtdele.delete()
    mt=Mothertongue.objects.all().order_by('id').values()        
    return render(request, 'mothertongue.html',{'mt':mt})        



#signin 

def signin(request):
    if request.method == 'POST':
        mobile = request.POST['mobile']
        password = request.POST['pass']
        user = Users.objects.get(mobile=mobile)
        if Users.objects.filter(mobile = mobile).exists():           
            #if Users.objects.filter(password = password).exists():    
                # try:
                #     request.session['uid']=user.id
                #     print('.....',request.session['uid'])
                #     #sid=request.session['uid']
                                        
                # except Users.DoesNotExist:
                #     return render('login')

                #data=Users.objects.get(id=request.session.get('uid'))
                return render(request, 'home.html')#,{'data':data})
        else:
            messages.info(request, 'invalid credentials')
            #print("hiiiiii")
            return redirect('login')
    else:    
        return render(request,'login.html')



# #signup

# def signup(request):
#     if request.method == 'POST':
#         first_name = request.POST['first_name']
#         last_name = request.POST['last_name']
#         username = request.POST['username']
#         password1 = request.POST['password']
#         password2 = request.POST['confirm_password']
#         email = request.POST['email']

#         if password1==password2:
#             if User.objects.filter(username=username).exists():
#                 messages.info(request,'username taken')
#                 return redirect('signup')
#             elif User.objects.filter(email=email).exists():
#                 messages.info(request,'email taken')
#                 return redirect('signup')
#             else:    
#                 user = User.objects.create_user(username=username, password=password1, email=email, first_name=first_name, last_name=last_name)
#                 user.save()
#                 print('user created')
#                 return redirect('signin')
#         else:
#             messages.info(request,'password not matched...') 
#             return redirect('signup')

#         return redirect('/')

#     else:    
#         return render(request, 'signup.html')


