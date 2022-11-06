#user created file
from django.http import HttpResponse
from django.shortcuts import render

def index(request):
    return render(request, 'index.html')

def about(request):
    return HttpResponse("About page")

def analyze(request):
    inputText = request.POST.get('inputText', 'No input text found')
    capitalizeFlag = request.POST.get('capitalize', 'off') == 'on'
    removeSpaceFlag = request.POST.get('removeSpace', 'off') == 'on'
    countCharsFlag = request.POST.get('countChars', 'off') == 'on'
    # print(capitalizeFlag, removeSpaceFlag, countCharsFlag)
    outputText = inputText
    charCount = 0
    if capitalizeFlag:
        outputText = capitalize(outputText)
    if removeSpaceFlag:
        outputText = removeSpace(outputText)
    if countCharsFlag:
        charCount = countChars(inputText)
    params = {"outputText": outputText, "charCount": charCount, "charCountFlag": countCharsFlag}
    return render(request, 'analyze.html', params)

def capitalize(inputText):
    textList = inputText.split(".")
    outputTextList = []
    for line in textList:
        newline = ""
        count = 0
        for ch in line:
            count += 1
            if ch.isalpha():
                newline += ch.upper()
                break
            else:
                newline += ch
        newline += line[count:]
        outputTextList.append(newline)
    outputText = ".".join(outputTextList)               
    return outputText

def removeSpace(inputText):
    return inputText.replace(" ", "")

def countChars(inputText):
    return len(inputText)

def navigator(request):
    urls = [["Netflix", "https://www.netflix.com"], ["Google", "https://www.google.com"]]
    res = "<h1>Navigation Bar</h1><br>"
    for url in urls:
        res += '''<a href="'''
        res += url[1]
        res += '''">'''
        res += url[0]
        res += '''</a>'''
        res += "<br>"
    return HttpResponse(res)