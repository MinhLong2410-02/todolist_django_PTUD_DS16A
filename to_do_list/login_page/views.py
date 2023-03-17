from django.shortcuts import render
from .forms import LoginForm, RegisterForm

    
# Create your views here.
def login(request):
    if request.method == 'POST':
        form = LoginForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']
            print(username, password)
            return render(request, './login.html', 
                        #   {'username': username, 'password': password}
                        )
    return render(request, './login.html', {'form': LoginForm})

def register(request):
    if request.method == 'POST':
        form = RegisterForm(request.POST)
        if form.is_valid():
            firstname, lastname, username, password, _ = form.cleaned_data.keys()
    else:
        form = RegisterForm()
    return render(request, './register.html', {'form': form})