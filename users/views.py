from django.core import mail
from django.shortcuts import render, redirect
from .models import FirebaseUser
from firebase_admin.exceptions import FirebaseError
from django.contrib import messages
from firebase_admin import auth
import firebase_admin
from firebase_admin import credentials

# Initialize Firebase Admin SDK
cred = credentials.Certificate(
                'C:/Users/user/OneDrive/Documents/Firebase/web-development-fe6af-firebase-adminsdk-chwhp-bea71374ea.json')
firebase_admin.initialize_app(cred)

# Create your views here.
def signup_view(request):
        if request.method == 'POST':
                full_name = request.POST.get('full_name')
                email = request.POST.get('email')
                role = request.POST.get('role')
                password = request.POST.get('password')
                password_confirmation = request.POST.get('password_confirmation')

                # Validate form inputs
                if not all([full_name, email, role, password, password_confirmation]):
                        messages.error(request, "All fields are required.")
                        return redirect('users:signup')

                if password != password_confirmation:
                        messages.error(request, "Passwords do not match.")
                        return redirect('users:signup')

                # Check if the user already exists in Firebase
                try:
                        auth.get_user_by_email(email)
                        messages.error(request, "This email is already registered.")
                        return redirect('users:signup')
                except auth.UserNotFoundError:
                        pass  # User does not exist, proceed

                # Create the Firebase user
                try:
                        user = auth.create_user(
                                email=email,
                                password=password,
                                display_name=full_name
                        )
                except FirebaseError as e:
                        messages.error(request, f"Error creating user: {str(e)}")
                        return redirect('users:signup')

                # Save user in FirebaseUser model
                try:
                        FirebaseUser.objects.create(
                                uid=user.uid,
                                full_name=full_name,
                                email=email,
                                role=role
                        )
                except Exception as e:
                        auth.delete_user(user.uid)
                        messages.error(request, f"Error saving user: {e}")
                        return redirect('users:signup')

                # Success message
                messages.success(request, "Account created successfully!")
                return redirect('users:login')

        return render(request, 'users/signup.html')

def login_view(request):
        if request.method == 'POST':
                email = request.POST['email']
                password = request.POST['password']

                try:
                        user = auth.get_user_by_email(email)
                        # Simulate verification (Firebase Admin SDK doesn't handle passwords directly)
                        if verify_firebase_password(email, password):  # Custom helper function (mock)
                                request.session['firebase_uid'] = user.uid
                                messages.success(request, "Login successful.")
                                #next_url = request.GET.get('next', 'users:dashboard')
                                return redirect('app1:index')
                        else:
                                messages.error(request, "Invalid credentials.")
                                return render(request, 'users/login.html')
                except Exception as e:
                        messages.error(request, f"Login failed: {e}")
                        return redirect('users:login')

        return render(request, 'users/login.html')

def verify_firebase_password(email, password):
        # Use Firebase client-side SDK for real verification (mocking here for backend demo)
        return password == password  # Replace with actual verification in production



