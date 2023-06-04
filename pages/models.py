from django.db import models


class Service(models.Model):
    type = models.CharField(max_length=100)
    description = models.TextField()


class Projet(models.Model):
    libelle = models.CharField(max_length=100)
    description = models.TextField()
    date_debut = models.DateField()
    date_fin = models.DateField()
    acheve = models.BooleanField()


class Personnel(models.Model):
    nom = models.CharField(max_length=100)
    fichier_cv = models.FileField(upload_to='cvs/')
    fichier_photo = models.ImageField(upload_to='photos/')
    lien_linkedin = models.URLField()


class Detail(models.Model):
    fichier = models.FileField(upload_to='details/')


class Equipe(models.Model):
    # À remplir avec les champs et les relations appropriés pour cette table
    pass
class Contact(models.Model):
    email = models.EmailField()
    subject = models.CharField(max_length=200)
    message = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
from django.db import models

class Message(models.Model):
    content = models.TextField()

    def __str__(self):
        return self.content
#--------------------------Job----------------------------------

class Job(models.Model):
    nom = models.CharField(max_length=255)
    prenom = models.CharField(max_length=255)
    num_telephone = models.CharField(max_length=20)
    niveau = models.CharField(max_length=100)
    cv = models.FileField(upload_to='cv/')
    experience = models.TextField()
    lettre_motivation = models.TextField()

    def __str__(self):
        return self.nom
#----------------ajouter_stage-----------------------------------
from django.db import models

class Stage(models.Model):
    description = models.TextField()
    image = models.ImageField(upload_to='stage_images')
    poste = models.CharField(max_length=100)

    def __str__(self):
        return self.poste
from django.db import models

class Candidat(models.Model):
    description = models.TextField()
    image = models.ImageField(upload_to='images/')
    poste = models.CharField(max_length=100)

    def __str__(self):
        return self.poste
    
from django.db import migrations
from django.contrib.auth.models import User

def set_default_user(apps, schema_editor):
    Message = apps.get_model('pages', 'Message')
    User = apps.get_model('auth', 'User')
    for message in Message.objects.all():
        user = User.objects.first()  # Change this according to your logic to retrieve the current user
        message.user = user
        message.save()

class Migration(migrations.Migration):

    dependencies = [
        ('pages', '0001_initial'),
    ]

    operations = [
        migrations.RunPython(set_default_user),
    ]

