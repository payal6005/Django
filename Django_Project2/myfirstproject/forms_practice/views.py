from django.shortcuts import render,redirect
from django.http import HttpResponse
from .forms import *
from .models import login

#insert data and get data from database
def detail(request):
    data=login.objects.all()
    form=loginForm()
    if request.method == 'POST':
        
        form =loginForm(request.POST)
        if form.is_valid():

            name=form.cleaned_data['username']
            email=form.cleaned_data['emailid']
            obj=login(username=name,emailid=email)
            obj.save()
            return redirect('/forms_practice')
        
    context = {'data':data,'form':form}
    return render(request ,'forms_practice/Home.html',context)
#delete data
def delete(request,id):
    if request.method == 'GET':

     
    
        login.objects.filter(id=id).delete()
    return redirect("detail")  
#update data
def update(request,id):
    data1={}
    instance={}
    if request.method == 'GET':

        data1 = login.objects.get(id=id)
        print(data1)
        return render(request, 'forms_practice/update.html', {'form': data1}) 
       
    else:
       
        name=request.POST['username']
        email=request.POST['emailid']
        login.objects.filter(id=id).update(username=name,emailid=email)
         
        return redirect("detail") 



