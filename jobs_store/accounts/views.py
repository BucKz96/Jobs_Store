from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from .forms import SignUpForm
from .forms import UserProfileForm
from .models import UserProfile



def login_view(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('dashboard')  # Rediriger vers la page du tableau de bord après connexion
        else:
            messages.error(request, 'Identifiant ou mot de passe incorrect.')

    return render(request, 'accounts/login.html')

def logout_view(request):
    logout(request)
    return redirect('login')  # Rediriger vers la page de connexion après déconnexion

@login_required
def dashboard_view(request):

        # Données fictives pour les intitulés d'offres et leurs nombres
    offres_par_intitule = {
        'Dev Python': 20,
        'Data Scientist': 15,
        'Web Designer': 10,
        # ... Ajoutez d'autres intitulés avec leurs nombres
    }
    offres_par_region = {
        'Paris': 50,
        'Lyon': 30,
        'Marseille': 25,
        # ... Ajoutez d'autres régions avec le nombre d'offres
    }
    context = {
        'username': request.user.username,  # Si vous utilisez l'authentification utilisateur de Django
        'offres_par_intitule': offres_par_intitule,
        'offres_par_region': offres_par_region,
        # Ajoutez d'autres données à afficher sur le tableau de bord si nécessaire
    }
    return render(request, 'accounts/dashboard.html', context)

def signup_view(request):
    if request.method == 'POST':
        form = SignUpForm(request.POST)
        if form.is_valid():
            form.save()
            # Redirection après inscription réussie
            return redirect('dashboard')  # Change 'home' par le nom de l'URL vers la page d'accueil
    else:
        form = SignUpForm()
    return render(request, 'signup.html', {'form': form})

@login_required
def profile_view(request):
    user_profile, created = UserProfile.objects.get_or_create(user=request.user)
    form = UserProfileForm(request.POST or None, instance=user_profile)
    if form.is_valid():
        form.save()
        return redirect('profile')  # Redirige vers la même page après avoir enregistré les modifications

    return render(request, 'accounts/profile.html', {'form': form})

