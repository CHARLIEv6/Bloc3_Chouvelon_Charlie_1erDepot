from django.shortcuts import render, redirect
from django.http import HttpResponse, HttpResponseRedirect
from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from .forms import InscriptionForm, AchatForm, LoginForm
from .models import Offre, Achat, Utilisateur
from io import BytesIO
import qrcode
from django.core.exceptions import ObjectDoesNotExist

def accueil_view(request):
    return render(request, "accueil.html")

def inscription_view(request):
    form = InscriptionForm(request.POST or None)
    if request.method == "POST" and form.is_valid():
        utilisateur = form.save()
        login(request, utilisateur)
        return redirect("accueil")
    return render(request, "inscription.html", {"form": form})

def login_view(request):
    form = LoginForm(request.POST or None)
    if request.method == "POST" and form.is_valid():
        utilisateur = authenticate(
            request, 
            username=form.cleaned_data["username"], 
            password=form.cleaned_data["password"]
        )
        if utilisateur:
            login(request, utilisateur)
            return redirect("accueil")
        else:
            messages.error(request, "Nom d'utilisateur ou mot de passe incorrect.")
    return render(request, "login.html", {"form": form})

@login_required(login_url='inscription')
def achat_billet(request):
    offre_nom = request.GET.get("offre")  
    if not offre_nom:
        messages.error(request, "Aucune offre sélectionnée.")
        return redirect("billetterie")

    form = AchatForm(request.POST or None)
    if request.method == "POST" and form.is_valid():
        try:
            utilisateur = request.user
            offre = Offre.objects.get(nom=offre_nom)  
            nombre_billets = form.cleaned_data["nombre_billets"]

            for _ in range(nombre_billets):
                achat = Achat(utilisateur=utilisateur, offre=offre)
                achat.save()

            buffer = achat.generer_qr_code()

            return HttpResponse(buffer, content_type="image/png")

        except ObjectDoesNotExist:
            messages.error(request, "L'offre sélectionnée n'existe pas.")
            return redirect("billetterie")

        except Exception as e:
            messages.error(request, f"Erreur lors de l'achat : {e}")
            return redirect("billetterie")

    else:
        messages.error(request, "")


    return render(request, "achat.html", {"form": form})


@login_required(login_url='inscription')
def billetterie_view(request):
    offres = Offre.objects.all()
    return render(request, 'billetterie.html', {"offres": offres})

def logout_view(request):
    logout(request)
    return redirect("accueil")
