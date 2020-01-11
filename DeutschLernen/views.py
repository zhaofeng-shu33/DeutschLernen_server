from django.shortcuts import redirect
def index(request):
    '''page redirection to index.html'''
    return redirect('/static/index.html')
