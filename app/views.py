from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.
def home(request):
    return render(request,'index.html')

def Analyzetext(request):
    djtext= request.GET.get('text','gefault')

    removepunc = request.GET.get('removepunc','off')
    fullcaps = request.GET.get('fullcaps','off')
    newlineremover = request.GET.get('newlineremover','off')
    extraspaceremover = request.GET.get('extraspaceremover','off')
    charcount = request.GET.get('charcount','off')

    if removepunc =='on':
        puncatutions='''!()-{}[];:'"\,.<>/?@#$%^&*_+~'''
        analyzed =""
        for char in djtext:
            if char not in puncatutions:
                analyzed = analyzed + char
        params = {'purpose':'Remove Punctustions','analyzed_text':analyzed}

        djtext=analyzed
    
    if(fullcaps=='on'):
        analyzed=''
        for char in djtext:
            analyzed= analyzed+char.upper()
        params = {'purpose':'Remove Punctustions','analyzed_text':analyzed}

        djtext=analyzed
    
    if(newlineremover=='on'):
        analyzed=''
        for char in djtext:
            if char != '\n' and char != '\r':
                analyzed= analyzed + char
        params = {'purpose':'Remove Punctustions','analyzed_text':analyzed}
        djtext=analyzed

    
    if(extraspaceremover =='on'):
        analyzed=''
        for index, char in enumerate(djtext):
            if not (djtext[index]==" " and djtext[index+1]==" "):
                analyzed= analyzed + char
        params = {'purpose':'Remove Punctustions','analyzed_text':analyzed}

        djtext=analyzed
    
    if(charcount=='on'):
        analyzed=''
        for char in djtext:
            analyzed =len(djtext)
        params = {'purpose':'Remove Punctustions','analyzed_text':analyzed}
        djtext=analyzed

    if(charcount !='on' and extraspaceremover !='on' and newlineremover !='on' and fullcaps !='on' and removepunc !='on'):
        return HttpResponse("Errror")
    
    return render(request,'new.html',params)