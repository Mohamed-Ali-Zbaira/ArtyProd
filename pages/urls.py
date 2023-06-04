from django.conf import settings
from django.conf.urls.static import static
from django.urls import path
from . import views
from django.urls import path
from .views import ReadMore, delete_projet, edit_projet
from django.contrib.auth import views as authViews
from .models import Job
from django.urls import path
from . import views
urlpatterns = [
    # path('',views.index,name='index'),
    path('', views.home, name='home'),
    path('Register', views.Register, name="register"),
    path('login', views.userLogin, name="login"),
    path('logout', views.userLogout, name="logout"),


    
    path('formation/', views.formation, name='formation'),
    path('send_email/', views.send_email, name='send_email'),

    path('Personnel/', views.Personnel, name='Personnel'),

    path('formation/', views.formation, name='formation'),
    path('postuler', views.postuler, name='postuler'),
    path('candidats/', views.candidats_view, name='candidats'),
    path('ReadMore', views.ReadMore, name='ReadMore'),
    path('Portfolio', views.Portfolio, name='Portfolio'),
    path('services', views.services, name='services'),
    path('equipe', views.equipe, name='equipe'),
    path('contact', views.contact, name='contact'),

    path('Jobs', views.Jobs, name='Jobs'),
    path('ajouter_stage', views.ajouter_stage, name='ajouter_stage'),
     path('ReadMoreJob', views.ReadMoreJob, name='ReadMoreJob'),
    # path('insertion', views.insertion, name='insertion'),  # Ajout de l'URL pour l'insertion des données
    path('acceuil', views.acceuil, name='acceuil'),
    path('admin/', views.admin, name='admin'),
    
    path('read-more/', ReadMore, name='ReadMore'),
    path('delete-projet/<int:projet_id>/', delete_projet, name='delete_projet'),
    path('edit-projet/<int:projet_id>/', edit_projet, name='edit_projet'),



    path('reset_password/' ,authViews.PasswordResetView.as_view(template_name= "bookstore/password_reset.html") , name="reset_password"),
    path('reset_password_sent/' ,authViews.PasswordResetDoneView.as_view(template_name= "bookstore/password_reset_sent.html") , name="password_reset_done"),
    path('reset/<uidb64>/<token>/' ,authViews.PasswordResetConfirmView.as_view(template_name= "bookstore/password_reset_form.html") , name="password_reset_confirm"),
    path('reset_password_complete/' ,authViews.PasswordResetCompleteView.as_view(template_name= "bookstore/password_reset_done.html") , name="password_reset_complete"),

]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
