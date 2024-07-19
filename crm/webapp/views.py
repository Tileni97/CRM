from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login as auth_login, logout as auth_logout
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from .forms import CreateUserForm, LoginForm, CreateRecordForm, UpdateRecordForm
from .models import Records
from django.core.paginator import Paginator


# Home page view
def home(request):
    return render(request, 'webapp/index.html')

# Register a user view
def register(request):
    form = CreateUserForm()
    if request.method == 'POST':
        form = CreateUserForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('login')
    context = {'form': form}
    return render(request, 'webapp/register.html', context)

# Login a user view
def my_login(request):
    form = LoginForm()
    if request.method == 'POST':
        form = LoginForm(request, data=request.POST)
        if form.is_valid():
            username = request.POST.get('username')
            password = request.POST.get('password')
            user = authenticate(request, username=username, password=password)
            if user is not None:
                auth_login(request, user)
                return redirect('dashboard')
            else:
                messages.info(request, 'Username OR password is incorrect')
    context = {'form': form}
    return render(request, 'webapp/my-login.html', context)

# Logout a user view
def user_logout(request):
    auth_logout(request)
    return redirect('login')

# Dashboard view
@login_required(login_url='login')
def dashboard(request):
    records_list = Records.objects.all()
    paginator = Paginator(records_list, 10)  # Show 10 records per page

    page_number = request.GET.get('page')
    records = paginator.get_page(page_number)

    context = {'records': records}
    return render(request, 'webapp/dashboard.html', context)


#- Creat a record view
@login_required(login_url='login') # This decorator ensures that only authenticated users can access this view
def create_record(request):

    form = CreateRecordForm() # This is the form instance that will be rendered in the template
    if request.method == 'POST': # If the request method is POST, then the form data is validated and saved
        form = CreateRecordForm(request.POST) # This is the form instance that will be rendered in the template
        if form.is_valid(): # If the form data is valid, then the form data is saved
            form.save() # This saves the form data to the database
            return redirect('dashboard') # Redirects the user to the dashboard page
    context = {'form': form} # This is the context dictionary that will be passed to the template
    return render(request, 'webapp/create-record.html', context) # This renders the create_record.html template with the context dictionary

# Update a record view

@login_required(login_url='login') # This decorator ensures that only authenticated users can access this view
def update_record(request, pk):
    
        record = Records.objects.get(id=pk) # This gets the record with the id that is passed in the URL
        form = UpdateRecordForm(instance=record) # This is the form instance that will be rendered in the template
        if request.method == 'POST': # If the request method is POST, then the form data is validated and saved
            form = UpdateRecordForm(request.POST, instance=record) # This is the form instance that will be rendered in the template
            if form.is_valid(): # If the form data is valid, then the form data is saved
                form.save() # This saves the form data to the database
                return redirect('dashboard') # Redirects the user to the dashboard page

            context = {'form': form} # This is the context dictionary that will be passed to the template
            return render(request, 'webapp/update-record.html', context) # This renders the update_record.html template with the context dictionary    

            #Rea/ view a record view

@login_required(login_url='login') # This decorator ensures that only authenticated users can access this view
def view_record(request, pk):

    all_records = Records.objects.all() # This gets all the records from the database

    return render(request, 'webapp/view-record.html', context) # This renders the view_record.html template with the context dictionary})
    