from django.http import HttpResponse
from django.shortcuts import render

def index(request):
    return render(request,'index.html')
def analyze(request):
    djtext = request.GET.get('text','default')
    tremovepunc= request.GET.get('removepunc','off')
    tfullcaps= request.GET.get('fullcaps','off')
    tnewlineremover= request.GET.get('newlineremover','off')
    tspaceremover= request.GET.get('spaceremover','off')
    tcharcnt= request.GET.get('charcnt','off')
    
    print(djtext)
    print(tremovepunc)
    if tremovepunc == "on":
        analyzed = ""
        punctuations = '''!()-[]{};:'"\,<>./?@#$%^&*_~'''
        for char in djtext:
            if char not in punctuations:
                analyzed = analyzed + char
        params= {'Purpose': 'Remove Punctuations', 'analyzed_text':analyzed}
        return render(request,'analyze.html',params)
    if tnewlineremover == "on":
        analyzed = ""
        for char in djtext:
            if char != '\n':
                analyzed = analyzed + char
        params= {'Purpose': 'new line remove', 'analyzed_text':analyzed}
        return render(request,'analyze.html',params)  
    if tfullcaps == "on":
        analyzed = ""
        for char in djtext:
            analyzed = analyzed + char.upper()
        params= {'Purpose': 'Uppercase', 'analyzed_text':analyzed}
        return render(request,'analyze.html',params)
    if tspaceremover == "on":
        analyzed = ""
        for index, char in enumerate(djtext):
            if djtext[index]==" " and djtext[index+1]==" ":
                pass
            else:
                analyzed = analyzed + char
        params= {'Purpose': 'Extra Space Remove', 'analyzed_text':analyzed}
        return render(request,'analyze.html',params)   
    elif tcharcnt == "on":
        analyzed=len(djtext)
        params= {'Purpose': 'Char Count', 'analyzed_text':analyzed}
        return render(request,'analyze.html',params) 
    else:
        return HttpResponse("Error")