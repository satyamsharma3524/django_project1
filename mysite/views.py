# this file is created by me... new file..

from django.http import HttpResponse
from django.shortcuts import render


def index(request):
    # return HttpResponse('Hello World!')
    return render(request, 'index2.html')


def about(request):
    return render(request, './about.html')

def contact(request):
    return render(request, './contact.html')


def analyse(request):
    # get the text
    djtext = request.POST.get('text', 'default')

    # check Checkbox value 
    removepunc = request.POST.get('removepunc', 'off')
    capitalize = request.POST.get('capitalize', 'off')
    newlineremover = request.POST.get('newlineremover', 'off')
    extraspaceremover = request.POST.get('extraspaceremover', 'off')
    charcounter = request.POST.get('charcounter', 'off')

    # check which checkbox is on
    if(removepunc == "on"):
        Punctuations = '''!()-[]{},.:;"'/?|\+=*&^%$#@~`'''
        analysed = ""

        for char in djtext:
            if char not in Punctuations:
                analysed = analysed + char

        params = {'Analyse': 'Remove Punctuations', 'inputtext': analysed}
        djtext=analysed
        # return render(request, 'analyse2.html', params)

    if(capitalize=="on"):
        analysed=""
        for char in djtext:
            analysed = analysed + char.upper()

        params = {'Analyse': 'Change to UPPERCASE', 'inputtext': analysed}
        djtext=analysed
        # return render(request,"analyse2.html",params)

    if(newlineremover=="on"):
        analysed=""
        for char in djtext:
            if char !="\n" and char !="\r":
                analysed= analysed+char

        params = {'Analyse': 'Remove New Lines', 'inputtext': analysed}
        djtext=analysed
        # return render(request,"analyse2.html",params)

    if(extraspaceremover=="on"):
        Punctuation = "  "
        analysed = ""

        for index,char in enumerate(djtext):
            if not(djtext[index]==" " and djtext[index+1]==" "):
                analysed=analysed+char

        params = {'Analyse': 'Remove Extra Spaces', 'inputtext': analysed}
        djtext=analysed
        # return render(request, 'analyse2.html', params)

    if(charcounter=="on"):
        analysed = 0 
        for i in range(len(djtext)):
            analysed=analysed + 1

        params = {'Analyse': 'Change to UPPERCASE', 'inputtext': analysed}

    if(removepunc != "on" and capitalize !="on" and newlineremover != "on" and extraspaceremover != "on" and charcounter != "on"):
        return HttpResponse("Error")

    return render(request,"analyse2.html",params)


