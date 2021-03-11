# self created file
from django.http import HttpResponse #server returns an HTTP response (output) to the browser
from django.shortcuts import render
import string

'''
#Code for Video 6

def index(request):
    return HttpResponse('<h1>Hello</h1> <a href = "https://www.google.com/"> GOOGLE </a>')

def about(request):
    return HttpResponse('This is test project')

def readFile(request):
    with open(r'D:\GITHUB\DJANGO\DjangoPractice\textutils\textutils\textutils\one.txt') as f:
        data = f.read()
    return HttpResponse(data)

'''
'''
#Code for Video 7 - render and paramter passting to html page

def index(request):
    #return HttpResponse('Home')
    params = {'name': 'Neethu', 'place':'Pune'}
    return render(request,'index.html',params)


def index(request):
    return render(request,'index.html')


def removepunc(request):
    #get the text from index.html page
    djtext = request.GET.get('text','default') #gets text from the html page if nothing there return 'default'
    print(djtext)
    return HttpResponse('remove punc')


def capfirst(request):
    return HttpResponse('capitalize first')


def newlineremove(request):
    return HttpResponse('new line remove')


def spaceremove(request):
    return HttpResponse('space remove <br><a href = "/"> BACK </a>')


def charcount(request):
    return HttpResponse('char count')

'''
#code for video 11
def index(request):
    return render(request,'index.html')

def analyze(request):
    djtext = request.GET.get('text','default')
    #print(djtext)
    checkb_removepunc = request.GET.get('removepunc','off')
    checkb_fullcaps = request.GET.get('fullcaps','off')
    checkb_newlineremover = request.GET.get('newlineremover','off')
    checkb_spaceremover = request.GET.get('spaceremover','off')
    checkb_charcount = request.GET.get('charcount','off')

    #print(checkb_removepunc)
    analyzed = ""
    '''
    # for single checkboxes only -- BUG

    if checkb_removepunc == 'on':
        punctuations = string.punctuation
        for char in djtext:
            if char not in punctuations:
                analyzed = analyzed+char
    #else:
    #    analyzed = djtext
        params = {'purpose':'Analaysed Text!','analysed_text':analyzed}
        return render(request,'analyze.html',params)
    elif checkb_fullcaps == 'on':
        params = {'purpose':'Capitalised Text!','analysed_text':djtext.upper()}
        return render(request,'analyze.html',params)
    elif checkb_newlineremover == 'on':
        params = {'purpose':'Removed New Line!','analysed_text':djtext.replace('\n',' ')}
        return render(request,'analyze.html',params)
    elif checkb_spaceremover == 'on':

        for index, char in enumerate(djtext):
            if not(djtext[index] == ' ' and djtext[index+1] == ' '):
                analyzed = analyzed+char
        params = {'purpose':'Removed New Line!','analysed_text':analyzed}
        return render(request,'analyze.html',params)
    elif checkb_charcount == 'on':
        charcnt = len(djtext)-djtext.count(' ')
        params = {'purpose':'Removed New Line!','analysed_text':charcnt}
        return render(request,'analyze.html',params)
    else :
        return HttpResponse('Error')
    '''

    #for multiple checkboxes
    if checkb_removepunc == 'on':
        punctuations = string.punctuation
        for char in djtext:
            if char not in punctuations:
                analyzed = analyzed+char
        params = {'purpose':'Analaysed Text!','analysed_text':analyzed}
        #return render(request,'analyze.html',params)
    
    if checkb_fullcaps == 'on':
        params = {'purpose':'Capitalised Text!','analysed_text':djtext.upper()}
        #return render(request,'analyze.html',params)
    
    if checkb_newlineremover == 'on':
        params = {'purpose':'Removed New Line!','analysed_text':djtext.replace('\n',' ')}
        #return render(request,'analyze.html',params)
    
    if checkb_spaceremover == 'on':

        for index, char in enumerate(djtext):
            if not(djtext[index] == ' ' and djtext[index+1] == ' '):
                analyzed = analyzed+char
        params = {'purpose':'Removed New Line!','analysed_text':analyzed}
        #return render(request,'analyze.html',params)
    
    if checkb_charcount == 'on':
        charcnt = len(djtext)-djtext.count(' ')
        params = {'purpose':'Removed New Line!','analysed_text':charcnt}
        #return render(request,'analyze.html',params)
