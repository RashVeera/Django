from django.shortcuts import render
from .models import Profile
# Create your views here.
import pdfkit
from django.template import loader
from django.http import HttpResponse,HttpRequest
import io
import os
def accept(request):
    if request.method=='POST':
        name=request.POST.get("name","")
        email=request.POST.get("email","")
        phone=request.POST.get("phone","")
        summary=request.POST.get("summary","")
        degree=request.POST.get("degree","")
        school=request.POST.get("school","")
        university=request.POST.get("university","")
        previous_Work=request.POST.get("previous_Work","")
        skills=request.POST.get("skills","")

        profile=Profile(name=name,email=email,phone=phone,summary=summary,degree=degree,school=school,university=university,previous_Work=previous_Work,skills=skills)
        profile.save()
    return render(request,'pdf/accept.html')

def resume(request,id):
    user_profile=Profile.objects.get(pk=id)
    template=loader.get_template('pdf/resume.html')
    html=template.render({'user_profile':user_profile})
    options={
        'page-size':'Letter',
        'encoding':'UTF-8',
    }
    pdf=pdfkit.from_string(html,False,options)
    response=HttpResponse(pdf,content_type='application/pdf')
    response['Content-Disposition']='attachment'
    filename='resume.pdf'
    return response

def list(request):
    profile=Profile.objects.all()
    return render(request,'pdf/list.html',{'profile':profile})