from django.http import HttpResponse
from django.shortcuts import render, redirect
from .models import Show
from django.template import Context, Template 
from django.contrib import messages





def index(request):
    context={}
    if request.method=="GET":
        
        all_shows=Show.objects.all()
        
        context={
        "shows_temp":all_shows,

        }
    
        


    return render(request,"show_res.html",context)








def create_show(request):
    
    if request.method=="GET":
        
        return render (request,"show_add.html")
    
    
    if request.method=="POST":
        
        errors=Show.objects.basic_validator(request.POST)
        
        if len(errors)>0:
            for k,v in errors.items():
                messages.error(request,v)
            return redirect("/shows/new")
        
        
        
         
        new_show=Show.objects.create(
            title=request.POST["title_form"],
            desc=request.POST["desc_form"],
            network=request.POST["network_form"],
            release_date=request.POST["release_form"]
            )
        

    
        return redirect("/shows/"+str(new_show.id))





def show_all(request,id):
    context={}
    if request.method=="GET":
        get_title=Show.objects.get(id=id).title
        get_network=Show.objects.get(id=id).network
        get_release=Show.objects.get(id=id).release_date
        get_desc=Show.objects.get(id=id).desc
        
        
        context={
        "title_temp":get_title,
        "network_temp":get_network,
        "release_temp":get_release,
        "desc_temp":get_desc
        

        }
    
        


        return render(request,"show_create.html",context)



def show_edit(request,id):
    
    
    if request.method=="GET":
        
        return render (request,"show_edit.html")
    
    
    if request.method=="POST": 
        
        
        errors=Show.objects.basic_validator1(request.POST)
        
        if len(errors)>0:
            for k,v in errors.items():
                messages.error(request,v)
            return redirect("/shows/"+str(id)+"/edit")
        
        
        
        show_update=Show.objects.get(id=id)
        show_update.title=request.POST["title_form_new"]
        
        show_update.network=request.POST["network_form_new"]
        
        show_update.release_date=request.POST["release_form_new"]
        
        show_update.desc=request.POST["desc_form_new"]
        
        show_update.save()
        
        """show_update_title=Show.objects.get(id=id).title
        show_update.title=request.POST["title_form_new"]
        show_update.title.save()
        show_update.network=request.POST["network_form_new"]
        show_update.network.save()
        show_update.release_date=request.POST["release_form_new"]
        show_update.network.save()
        show_update.desc=request.POST["desc_form_new"]
        show_update.network.save()"""
        
        """show_update=Show.objects.get(id=id)
        new_title=request.POST["title_form_new"]
        show_update.title=new_title"""
        """show_update.network=request.POST["network_form_new"]
        
        show_update.release_date=request.POST["release_form_new"]
        
        show_update.desc=request.POST["desc_form_new"]"""
        
        return redirect("/shows/"+str(id))
    
    
 
 
 
 
def show_des(request,id):
    
    
    
    if request.method=="GET":
        get_title=Show.objects.get(id=id).title
        get_id=Show.objects.get(id=id).id
        
        context={
            "title_temp":get_title,
            "id_temp":get_id,
        }
        
        
        
        
        return render (request,"show_del.html",context)
    
    
    if request.method=="POST": 
        show_destroy=Show.objects.get(id=id).delete()
     
     
        return redirect("/shows")
     