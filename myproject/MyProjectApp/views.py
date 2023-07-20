from cgitb import html
import chunk
import email
from email import message
from importlib.resources import path
from lib2to3.pytree import Base
from telnetlib import LOGOUT
from traceback import format_stack, format_tb
from unicodedata import name
from urllib import request
from warnings import formatwarning
from wsgiref.util import FileWrapper
from xml.parsers.expat import model
from django.shortcuts import render
from django.shortcuts import redirect
from django.http import HttpResponse
from django.views.generic import TemplateView, base
from django.template import RequestContext
from django.conf import settings
from MyProjectApp.modules.PhyloEasy import configuration, start
from django.http import StreamingHttpResponse
from .models import Contact
from django.core.mail import send_mail
import mimetypes
import os
from django.http.response import HttpResponse
import os
import subprocess

from django.contrib.auth.models import User
from django.contrib import messages
from django.contrib.auth import authenticate, login 
from django.views.generic import View
from django.http import HttpResponse
from MyProjectApp.models import details
from MyProjectApp.models import  count_check

from .models import ImageModel
class Home(TemplateView):
    template_name='firstpage.html'
# Create your views here.
def hi(request):
    return render(request,'MyProjectApp/hi.html',) 

def Tutorials(request):
    return render(request,'MyProjectApp/Tutorials.html') 

def About(request):
    return render(request,'MyProjectApp/About.html') 

def Contactpg(request):
    if request.method == "POST":
        contact=Contact() 
        name=request.POST.get('name')
        email=request.POST.get('email')
        subject=request.POST.get('subject')
        message=request.POST.get('message')
        contact.name=name
        contact.email=email
        contact.subject=subject
        contact.message=message
        contact.save()
        return HttpResponse('<h2 style="text-align: center; color: darkblue;">Thanks to get in touch with us.</h2>')

       
    return render(request,'MyProjectApp/Contactpg.html')   
from django.http import FileResponse   
def download_file(request):
    # Define Django project base directory
    fn=request.GET.get('name',None)
    if not fn:
        return HttpResponse('<h2 style="text-align: center; color: darkblue;">Enter Your Token ID</h2>')
   #BASE_DIR1 = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
    #BASE_DIR = (os.path.join(BASE_DIR1,fn,),)
    #print(BASE_DIR)
    response = FileResponse(open(fn+'/Alignment.aln', 'rb'))
    return response 
    # Define text file name
    filename = 'Alignment.aln'
    # Define the full file path
    filepath = BASE_DIR + '//' + filename
    # Open the file for reading content
    path = open(filepath, 'r')
    # Set the mime type
    mime_type, _ = mimetypes.guess_type(filepath)
    # Set the return value of the HttpResponse
    response = HttpResponse(path, content_type=mime_type)
    # Set the HTTP header for sending to browser
    response['Content-Disposition'] = "attachment; filename=%s" % filename
    # Return the response value
	
    return response
from django.http import FileResponse
def download_file2(request):
    fn=request.GET.get('name',None)
    if not fn:
        return HttpResponse('<h2 style="text-align: center; color: darkblue;">Enter Your Token ID</h2>')
    # Define Django project base directory
    #BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
    response = FileResponse(open(fn+'/Alignment.phy', 'rb'))
    return response 
    # Define text file name
    filename = 'Alignment.phy'
    # Define the full file path
    filepath = BASE_DIR + '//' + filename
    # Open the file for reading content
    path = open(filepath, 'r')
    # Set the mime type
    mime_type, _ = mimetypes.guess_type(filepath)
    # Set the return value of the HttpResponse
    response = HttpResponse(path, content_type=mime_type)
    # Set the HTTP header for sending to browser
    response['Content-Disposition'] = "attachment; filename=%s" % filename
    # Return the response value
	
    return response
from django.http import FileResponse
def download_file3(request):
    fn=request.GET.get('name',None)
    if not fn:
        return HttpResponse('<h2 style="text-align: center; color: darkblue;">Enter Your Token ID</h2>')
    # Define Django project base directory
    #BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
    response = FileResponse(open(fn+'/Alignment.fasta', 'rb'))
    return response 
    # Define text file name
    filename = 'Alignment.fasta'
    # Define the full file path
    filepath = BASE_DIR + '//' + filename
    # Open the file for reading content
    path = open(filepath, 'r')
    # Set the mime type
    mime_type, _ = mimetypes.guess_type(filepath)
    # Set the return value of the HttpResponse
    response = HttpResponse(path, content_type=mime_type)
    # Set the HTTP header for sending to browser
    response['Content-Disposition'] = "attachment; filename=%s" % filename
    # Return the response value
	
    return response
	
	
from django.http import FileResponse
def download_file4(request):
    fn=request.GET.get('name',None)
    if not fn:
        return HttpResponse('<h2 style="text-align: center; color: darkblue;">Enter Your Token ID</h2>')
    # Define Django project base directory
    #BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
    response = FileResponse(open(fn+'/Pairwise Distance.txt', 'rb'))
    response['content_type'] = 'text/plain'
    response['Content-Disposition'] = 'attachment; filename=Pairwise Distance.txt'
    #response = HttpResponse(open(fn+'/Pairwise Distance.txt', 'rb'))
    return response 
    # Define text file name
    filename = 'Pairwise Distance.txt'
    # Define the full file path
    filepath = BASE_DIR + '//' + filename
    # Open the file for reading content
    path = open(filepath, 'r')
    # Set the mime type
    mime_type, _ = mimetypes.guess_type(filepath)
    # Set the return value of the HttpResponse
    #response = HttpResponse(path, content_type=mime_type)
    # Set the HTTP header for sending to browser
    response['Content-Disposition'] = "attachment; filename=%s" % filename
    #Return the response value
	
   # return response	

from django.http import FileResponse
def download_file5(request):
    fn=request.GET.get('name',None)
    if not fn:
        return HttpResponse('<h2 style="text-align: center; color: darkblue;">Enter Your Token ID</h2>')
    # Define Django project base directory
    #BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
    response = FileResponse(open(fn+'/Distance Matrix.csv', 'rb'))
    return response
    # Define text file name
    filename = 'Distance Matrix.csv'
    # Define the full file path
    filepath = BASE_DIR + '//' + filename
    # Open the file for reading content
    path = open(filepath, 'r')
    # Set the mime type
    mime_type, _ = mimetypes.guess_type(filepath)
    # Set the return value of the HttpResponse
    response = HttpResponse(path, content_type=mime_type)
    # Set the HTTP header for sending to browser
    response['Content-Disposition'] = "attachment; filename=%s" % filename
    # Return the response value
	
    return response	

from django.http import FileResponse
def download_file6(request):
    fn=request.GET.get('name',None)
    if not fn:
        return HttpResponse('<h2 style="text-align: center; color: darkblue;">Enter Your Token ID</h2>')
    # Define Django project base directory
    #BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
    response = FileResponse(open(fn+'/Tree.nwk', 'rb'))
    return response
    # Define text file name
    filename = 'Tree.nwk'
    # Define the full file path
    filepath = BASE_DIR + '//' + filename
    # Open the file for reading content
    path = open(filepath, 'r')
    # Set the mime type
    mime_type, _ = mimetypes.guess_type(filepath)
    # Set the return value of the HttpResponse
    response = HttpResponse(path, content_type=mime_type)
    # Set the HTTP header for sending to browser
    response['Content-Disposition'] = "attachment; filename=%s" % filename
    # Return the response value
	
    return response	

from django.http import FileResponse
def download_file7(request):
    fn=request.GET.get('name',None)
    if not fn:
        return HttpResponse('<h2 style="text-align: center; color: darkblue;">Enter Your Token ID</h2>')
    # Define Django project base directory
    #BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
    response = FileResponse(open(fn+'/Tree.nex', 'rb'))
    return response
    # Define text file name
    filename = 'Tree.nex'
    # Define the full file path
    filepath = BASE_DIR + '//' + filename
    # Open the file for reading content
    path = open(filepath, 'r')
    # Set the mime type
    mime_type, _ = mimetypes.guess_type(filepath)
    # Set the return value of the HttpResponse
    response = HttpResponse(path, content_type=mime_type)
    # Set the HTTP header for sending to browser
    response['Content-Disposition'] = "attachment; filename=%s" % filename
    # Return the response value
	
    return response

from django.http import FileResponse
def download_file8(request):
    fn=request.GET.get('name',None)
    if not fn:
        return HttpResponse('<h2 style="text-align: center; color: darkblue;">Enter Your Token ID</h2>')
    # Define Django project base directory
    #BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
    response = FileResponse(open(fn+'/Tree.xml', 'rb'))
    response['content_type'] = 'xml'
    response['Content-Disposition'] = 'attachment; filename=Tree.xml'
    return response
    # Define text file name
    filename = 'Tree.xml'
    # Define the full file path
    filepath = BASE_DIR + '//' + filename
    # Open the file for reading content
    path = open(filepath, 'r')
    # Set the mime type
    mime_type, _ = mimetypes.guess_type(filepath)
    # Set the return value of the HttpResponse
    response = HttpResponse(path, content_type=mime_type)
    # Set the HTTP header for sending to browser
    response['Content-Disposition'] = "attachment; filename=%s" % filename
    # Return the response value
	
    return response


def download_file9(request):
    # Define Django project base directory
    BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
    # Define text file name
    filename = 'Welcome To PhyloEasy User Tutorial.pdf'
    # Define the full file path
    filepath = BASE_DIR + '//' + filename
    # Open the file for reading content
    path = open(filepath, 'rb')
    # Set the mime type
    mime_type, _ = mimetypes.guess_type(filepath)
    # Set the return value of the HttpResponse
    response = HttpResponse(path, content_type=mime_type)
    # Set the HTTP header for sending to browser
    response['Content-Disposition'] = "attachment; filename=%s" % filename
    # Return the response value
	
    return response



from django.http import FileResponse
def download_image(request):
    fn=request.GET.get('name',None)
    if not fn:
        return HttpResponse('<h2 style="text-align: center; color: darkblue;">Enter Your Token ID</h2>')
    response = FileResponse(open(fn+'/Tree.png', 'rb'))
    response['content_type'] = 'png'
    response['Content-Disposition'] = 'attachment; filename=Tree.png'
    return response
    #BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
    filename = 'Tree.png'
    filepath = BASE_DIR + '//' + filename
    path = open(filepath, 'rb')
    content_type = mimetypes.guess_type(filepath)[0]  # Use mimetypes to get file type
    response     = HttpResponse(path,content_type=content_type)  
  
    response['Content-Disposition'] = "attachment; filename=%s" %  filename
    return response

from django.http import FileResponse
def download_image1(request):
    fn=request.GET.get('name',None)
    if not fn:
        return HttpResponse('<h2 style="text-align: center; color: darkblue;">Enter Your Token ID</h2>')
    response = FileResponse(open(fn+'/Tree.jpg', 'rb'))
    response['content_type'] = 'jpg'
    response['Content-Disposition'] = 'attachment; filename=Tree.jpg'
    return response
    #BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
    filename = 'Tree.jpg'
    filepath = BASE_DIR + '//' + filename
    path = open(filepath, 'rb')
    content_type = mimetypes.guess_type(filepath)[0]  # Use mimetypes to get file type
    response     = HttpResponse(path,content_type=content_type)  
  
    response['Content-Disposition'] = "attachment; filename=%s" %  filename
    return response

from django.http import FileResponse
def download_image2(request):
    fn=request.GET.get('name',None)
    if not fn:
      return HttpResponse('<h2 style="text-align: center; color: darkblue;">Enter Your Token ID</h2>') 
    response = FileResponse(open(fn+'/Tree.pdf', 'rb'))
    response['content_type'] = 'pdf'
    response['Content-Disposition'] = 'attachment; filename=Tree.pdf'
    return response
    #BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
    filename = 'Tree.pdf'
    filepath = BASE_DIR + '//' + filename
    path = open(filepath, 'rb')
    content_type = mimetypes.guess_type(filepath)[0]  # Use mimetypes to get file type
    response     = HttpResponse(path,content_type=content_type)  
  
    response['Content-Disposition'] = "attachment; filename=%s" %  filename
    return response



def xyz(request):
    y=0
    if request.method=="POST":
        print("DELETION ",request.POST.get("deletion"))
        print("ALGORITHM ",request.POST.get("ctype"))
        deletion = request.POST.get("deletion")
        clustering_type = request.POST.get("ctype")
        uploaded_file = request.FILES["document"]
        preccessFile = open(uploaded_file.name, "wb")
        contentOfFile = tuple(uploaded_file.readlines())
        for line in contentOfFile:
           preccessFile.write(line)
        preccessFile.close()        
        y=start(uploaded_file.name, "Alignment.aln", "clustal", "nexus", "", "", deletion, clustering_type)  
        # 
        # print(contentOfFile)  
    print("completed....")  
    return render(request,'MyProjectApp/xyz.html',{'y':y})

def send(request):
    count_check.objects.create(pid=1)
  



