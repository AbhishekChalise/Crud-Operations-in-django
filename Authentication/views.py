from django.shortcuts import render,redirect
from .forms import SignUpForm
from django.contrib.auth import login, authenticate
# from django.shortcuts import messages
# Create your views here.
def register(request):
    print("Request Method:", request.method)  # Debugging
    
    if request.method == "POST":
        form = SignUpForm(request.POST)
        if form.is_valid():
            user = form.save()  # Save the user to the database
            login(request, user)  # Log the user in after successful registration
            print("User registered and logged in successfully")
            return redirect('showTeacher')  # Redirect to another page (URL name should match your `urls.py`)
        else:
            print("Form is not valid:", form.errors)  # Debugging invalid form
            #messages.error(request,'Values given are not correct!!!')
            return redirect('register')

    else:
        form = SignUpForm()
    
    return render(request, 'register.html', {'form': form})