from django.shortcuts import render
from django.core.mail import send_mail
from django.conf import settings
from django.contrib import messages
from django.core.mail import send_mail, EmailMessage
from .models import Projet
from django.shortcuts import render, redirect
from .models import Message
from django.shortcuts import render
from django.shortcuts import redirect
from .models import Contact
from .forms import CreateNewUser
from .models import Projet
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from .forms import *
from django.contrib.auth.decorators import login_required
# import requests
from django.conf import settings

# from ArtyProd.views import *

# from django.http import HttpResponse
# Create your views here.


@login_required(login_url='login')
def index(request):
    return render(request, 'pages/index.html')
# def services(request):
#     services = Service.objects.all()
#     return render(request, 'pages/services.html', {'Service': services})
    # return HttpResponse('hammma')


def userLogin(request):

    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('home')
        else:
            messages.info(request, 'Credentials error')

    context = {}
    return render(request, 'pages/Login.html')


def userLogout(request):
    logout(request)
    return redirect('login')


def Register(request):
    form = CreateNewUser()
    if request.method == 'POST':
        form = CreateNewUser(request.POST)
        if form.is_valid():

            user = form.save()
            username = form.cleaned_data.get('username')
            messages.success(request, username + ' Created Successfully !')
            return redirect('login')
    else:
        messages.error(request,  ' invalid Recaptcha please try again!')

    context = {'form': form}
    return render(request, 'pages/Registre.html', context)


def Portfolio(request):
    projets = Projet.objects.all()
    context = {'projets': projets}
    return render(request, 'pages/portfolio.html', context)


def home(request):
    return render(request, 'pages/index.html')


def services(request):
    return render(request, 'pages/services.html')


def equipe(request):
    if request.method == 'POST':
        # Récupère le contenu du message depuis le formulaire
        content = request.POST.get('default-text', '')

        if content:
            message = Message(content=content)
            message.save()  # Enregistre le message dans l'admin
            # Redirige vers la même page 'equipe.html'
            return redirect('equipe')

    return render(request, 'pages/equipe.html')

from django.core.mail import send_mail

from django.shortcuts import render, redirect
from .forms import ContactForm

from django.core.mail import send_mail
from django.conf import settings

from django.core.mail import send_mail
from django.conf import settings


def contact(request):
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            # Enregistrer les données du formulaire dans la base de données
            form_data = form.save(commit=False)
            form_data.save()

            # Envoyer un e-mail avec les données du formulaire
            email = request.POST['email']
            subject = request.POST['subject']
            message = request.POST['message']
            message_body = f"Email: {email}\nSubject: {subject}\nMessage: {message}"

            send_mail(
                'Contact Form Submission',
                message_body,
                settings.DEFAULT_FROM_EMAIL,
                ['mohamedalizbaira@gmail.com'], # l'adresse de l'email de destination
                fail_silently=False,
            )

            return redirect('home')  # ou une autre page
    else:
        form = ContactForm()

    return render(request, 'pages/contact.html', {'form': form})



def Jobs(request):
    return render(request, 'pages/Jobs.html')

def Stage(request):
    stages = Stage.objects.all()
    return render(request, 'Stage.html', {'stages': stages})

from .models import Job

from .models import Stage

from .models import Personnel

from django.shortcuts import render, redirect
from .models import Personnel

def Personnel(request):
    if request.method == 'POST':
        nom = request.POST['nom']
        fichier_cv = request.FILES['fichier_cv']
        fichier_photo = request.FILES['fichier_photo']
        lien_linkedin = request.POST['lien_linkedin']
        
        Personnel = Personnel(nom=nom, fichier_cv=fichier_cv, fichier_photo=fichier_photo, lien_linkedin=lien_linkedin)
        Personnel.save()
        
        return redirect('Personnel')  # Rediriger vers une autre page après l'enregistrement
        
    return render(request, 'Personnel.html')



def ReadMoreJob(request):
    stages = Stage.objects.all()
    return render(request, 'pages/ReadMoreJob.html', {'stages': stages})
from .models import Candidat

def candidats_view(request):
    candidats = Candidat.objects.all()
    return render(request, 'pages/candidat.html', {'Candidat': candidats})
from .models import Message

def formation(request):
    stages = Stage.objects.all()
    candidats = Candidat.objects.all()
    users = User.objects.all()

    if request.method == 'POST':
        message_content = request.POST.get('default-text')
        user_id = request.POST.get('user-id')

        message = Message.objects.create(user_id=user_id, content=message_content)
        message.save()

    return render(request, 'pages/formation.html', {'stages': stages, 'candidats': candidats, 'users': users})

from django.core.mail import send_mail
from django.shortcuts import redirect


def send_email(request):
    if request.method == 'POST':
        message = request.POST.get('message')

        users = User.objects.all()

        for user in users:
            email_body = f"Bonjour {user.username},\n\n{message}"  # Include the username and message in the email body
            send_mail(
                'Subject of the Email',
                email_body,  # Use the updated email body
                'sender@example.com',
                [user.email],
                fail_silently=False,
            )

        return redirect('formation')  # Redirect to a success page or desired page after sending the email

    return redirect('formation')  # Redirect back to the formation page if the request method is not POST


def postuler(request):
    if request.method == 'POST':
        nom = request.POST.get('nom')
        prenom = request.POST.get('prenom')
        num_telephone = request.POST.get('num_telephone')
        niveau = request.POST.get('niveau')
        cv = request.FILES.get('cv')
        experience = request.POST.get('experience')
        lettre_motivation = request.POST.get('lettre_motivation')

        # Create an instance of the Job model and save the data to the database
        job = Job(
            nom=nom,
            prenom=prenom,
            num_telephone=num_telephone,
            niveau=niveau,
            cv=cv,
            experience=experience,
            lettre_motivation=lettre_motivation
        )
        job.save()

        return redirect('home')
    return render(request, 'pages/postuler.html')
#-------------------------------------------------------------------------------------------------
from django.shortcuts import render, redirect
from .models import Stage
from .forms import StageForm

def ajouter_stage(request):
  
    if request.method == 'POST':
        form = StageForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('nom_de_votre_vue')
    else:
        form = StageForm()
    return render(request, 'ajouter_stage.html', {'form': form})


# # def contact(request):
#     if request.method == 'POST':
#         email = request.POST.get('email')
#         subject = request.POST.get('subject')
#         message = request.POST.get('message')
#         Contact.objects.create(email=email, subject=subject, message=message)
#         # Faites ici d'autres opérations si nécessaire, comme l'envoi d'un e-mail de confirmation, etc.

#         # Afficher un message de succès
#         messages.success(request, 'Le message a été envoyé avec succès.')

#         # Redirection vers la page d'accueil
#         return redirect('home')

#     return render(request, 'pages/contact.html')

# def acceuil(request):
#     return render (request,'pages/AdminDash/acceuil.html')

#-------------------------------------acceuil-----------------------------------------------------------
def acceuil(request):
    contacts = Contact.objects.all()
    return render(request, 'pages/AdminDash/acceuil.html', {'contacts': contacts})
#-------------------------------------admin---------------------------------------------------------

def admin(request):
    return render(request, '/admin/')
#-------------------------------------ReadMore---------------------------------------------------------

from django.shortcuts import redirect, render
def ReadMore(request):
    projets = Projet.objects.all()
    context = {'projets': projets}
    return render(request, 'pages/ReadMore.html', context)
def delete_projet(request, projet_id):
    projet = Projet.objects.get(id=projet_id)
    projet.delete()
    return redirect('ReadMore')
def edit_projet(request, projet_id):
    projet = Projet.objects.get(id=projet_id)
    # Handle the edit logic here
    # ...
    return redirect('ReadMore')

