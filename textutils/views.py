# i have created this file:-pallav
from django.shortcuts import render
from django.shortcuts import render
from django.http import HttpResponse
from django.shortcuts import render
import string


# def index(request):
#     return HttpResponse('''<h1>Hello world! hue hue hat</h1> <a href="https://www.w3schools.com">Visit W3Schools.com!</a>''')
#
#
# def about(request):
#     return HttpResponse("<h1>Dogesh</h1>")

def index(response):
    return render(response, 'index.html')
    # return HttpResponse("Home")


# def removepunc(request):
#     print(request.GET.get('text', 'default'))
#     # default will be printed if no text is there is form
#     return HttpResponse("remove punc")
#
#
# def capfirst(request):
#     return HttpResponse("capitalize first")
#
#
# def newlineremove(request):
#     return HttpResponse("newline remover")
#
#
# def spaceremover(request):
#     return HttpResponse("space remover")
#
#
# def charcount(request):
#     return HttpResponse("char count")


def analyze(request):
    # get the text
    djtext = request.POST.get('text', 'default');
    # check checkbox values
    removepunc = request.POST.get('removepunc', 'off')
    fullcaps = request.POST.get('fullcaps', 'off')
    newlineremover = request.POST.get('newlineremover', 'off')
    extraspaceremover = request.POST.get('extraspaceremover', 'off')
    charcount = request.POST.get('charcount', 'off')

    punctuations = string.punctuation
    analyzed = ""
    if removepunc == "on":
        # analyzed = djtext
        # params = {'purpose': 'Removed Punctuations',
        #           'analyzed_text': analyzed}
        for char in djtext:
            if char not in punctuations:
                analyzed = analyzed + char
        params = {'purpose': 'Removed Punctuations',
                  'analyzed_text': analyzed}
        djtext=analyzed
        # return render(request, 'analyze.html', params)

    if fullcaps == "on":
        analyzed = ""
        for char in djtext:
            analyzed = analyzed + char.upper()

        params = {'purpose': 'Changed to Uppercase',
                  'analyzed_text': analyzed}
        djtext=analyzed
        # return render(request, 'analyze.html', params)

    if newlineremover=="on":
        analyzed=""
        for char in djtext:
            if char!="\n" and char!='\r':
                analyzed=analyzed+char
        params = {'purpose': 'Removed NewLines',
                  'analyzed_text': analyzed}
        djtext = analyzed
        # return render(request, 'analyze.html', params)

    if extraspaceremover=="on":
        analyzed="";
        for index,char in enumerate(djtext):
            if index==len(djtext)-1:
                pass
            elif djtext[index]==" " and djtext[index+1]==" ":
                pass
            else:
                analyzed=analyzed+char
        params = {'purpose': 'Extra Space Removed',
                  'analyzed_text': analyzed}
        djtext = analyzed
        # return render(request, 'analyze.html', params)

    # if charcount=="on":
    #     ans=0
    #     for char in djtext:
    #         if char==" " or char=="\n":
    #             pass
    #         else:
    #             ans=ans+1
    #     analyzed=str(ans)
    #     params = {'purpose': 'Char Count',
    #               'analyzed_text': analyzed}
    #     return render(request, 'analyze.html', params)
    # else:
    #     return HttpResponse("Error Aa Gaya😅")
    if removepunc!="on" and fullcaps!="on" and newlineremover!="on" and extraspaceremover!="on":
        return HttpResponse("Error")

    return render(request, 'analyze.html', params)
