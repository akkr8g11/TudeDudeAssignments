from django.shortcuts import render, redirect 
from .forms import CustomUserCreationForm 
from django.urls import reverse_lazy # For reverse_lazy
from django.contrib.auth.decorators import login_required # For protecting views
from django.contrib.auth.views import LoginView as AuthLoginView, LogoutView as AuthLogoutView # Import LogoutView 


def home(request): 
 context = { 
 'name': 'Alice', 
 'age': 30, 
 'city': 'New York', 
 'is_admin': True, 
 'items': ['apple', 'banana', 'cherry'], 
 'result': None # Initialize result to None 
 } 

 if request.method == 'POST': 
    try: 
        num1 = float(request.POST.get('num1')) 
        num2 = float(request.POST.get('num2')) 
        context['result'] = num1 + num2 
    except (ValueError, TypeError): 
        context['result'] = "Invalid input. Please enter numbers." 
 return render(request, 'myapp/index.html', context) 

def register(request): 
    if request.method == 'POST': 
        form = CustomUserCreationForm(request.POST) 
        if form.is_valid(): 
            form.save() # Save the new user to the database 
            return redirect('login') # Redirect to a login page (will create later) 
    else: 
        form = CustomUserCreationForm() # Create a blank form for GET request 
    return render(request, 'myapp/register.html', {'form': form})

class CustomLoginView(AuthLoginView): 
    template_name = 'myapp/login.html' # Specify your login template 
    fields = '__all__' # Use all fields (username, password) 
    redirect_authenticated_user = False # Redirect logged-in users away from login page 
 
def get_success_url(self): 
    return reverse_lazy('home') # Redirect to 'home' after successful login

class CustomLogoutView(AuthLogoutView): 
    next_page = reverse_lazy('home') # Redirect to home page after logout 
    
    def get(self, request, *args, **kwargs):
        return self.post(request, *args, **kwargs)
