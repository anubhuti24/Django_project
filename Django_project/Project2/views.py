#This is a python program


#PROGRAM TO REMOVE PUNCTUATIONS FROM TEXT


from django.http import HttpResponse
from django.shortcuts import render

def index(request):
       return render(request,'1.html')


def analyze(request):
       #Get the text
       djtext=request.POST.get('text','default')
       
       #check checkbox values
       removepunc=request.POST.get('removepunc','off')
       uppercase=request.POST.get('uppercase','off')
       newline_remover=request.POST.get('newline_remover','off')
       extraspaces_remover=request.POST.get('extraspaces_remover','off')
       lowercase=request.POST.get('lowercase','off')
       
       if removepunc == 'on':
           analyzed=""
           punctuations='''!@#$%^&*()_+~`{}[]|\:;"'<,>.?/'''
           for i in djtext:
               if i not in punctuations:
                    analyzed=analyzed+i
           par={'purpose':'MODIFIED TEXT','analyzed_text':analyzed}
           djtext=analyzed
           
       if uppercase == 'on':
           analyzed=""
           for i in djtext:
               analyzed=analyzed+i.upper()
           par={'purpose':'MODIFIED TEXT','analyzed_text':analyzed}
           djtext = analyzed
           
       if lowercase == 'on':
           analyzed=""
           for num in djtext:
               analyzed=analyzed+num.lower()
           par={'purpose':'MODIFIED TEXT','analyzed_text':analyzed}
           djtext = analyzed
       if newline_remover == 'on':
           analyzed=""
           for j in djtext:
               if j!='\n' and j!='\r':
                   analyzed=analyzed+j
           par={'purpose':'MODIFIED TEXT','analyzed_text':analyzed}
           djtext=analyzed
           
       if extraspaces_remover == 'on':
           analyzed=""
           for index,str in enumerate(djtext):
             if str==djtext[-1]:  
                if not(djtext[index]==" "):
                     analyzed=analyzed+str
             elif not(djtext[index]==" " and djtext[index+1]==" "):
                     analyzed=analyzed+str
           par={'purpose':'MODIFIED TEXT','analyzed_text':analyzed}
           djtext=analyzed
                   
       if removepunc!='on' and uppercase!='on' and newline_remover!='on' and extraspaces_remover!='on':     
           print("Choose any of the following options!!!!")
       return render(request,'analyze.html',par)
