from django.shortcuts import render,redirect, get_object_or_404
from esipy import App, EsiClient, EsiSecurity
from django.conf import settings
from eveonline.models import Token, EveCharacter
from django.contrib.auth.models import User


# Create your views here.
def add_token(request):
    return redirect(settings.ESI_URL_CACHE)

def remove_token(request, user):
    if request.user.is_authenticated():
        current_user = request.user
        if current_user == user:
            token = get_object_or_404(Token, user=user)
            token.delete()
        return redirect('eve')
    else:
        return redirect('eve')

def receive_token(request):
    if request.user.is_authenticated():
        ## SSO PROCESS
        esi_app = settings.ESI_APP

        esi_security = settings.ESI_SECURITY

        esi_client = EsiClient(esi_security)

        code = request.GET.get('code', None)
        esi_token = esi_security.auth(code)
        esi_verified = esi_security.verify()

        ## CHECK IF TOKEN OF SAME CHARACTER EXISTS
        if Token.objects.filter(character_name=esi_verified['CharacterName']).count() > 0:
            token = Token.objects.get(character_name=esi_verified['CharacterName'])
            token.delete()


        ## CREATE TOKEN
        token = Token(
                character_id=esi_verified['CharacterID'],
                character_owner_hash=esi_verified['CharacterOwnerHash'],
                character_name=esi_verified['CharacterName'],
                access_token=esi_token['access_token'],
                refresh_token=esi_token['refresh_token'],
                expires_in=esi_token['expires_in'],
                user=request.user
                )
        token.save()

        ## CREATE CHARACTER
        esiclient = settings.ESI_CLIENT

        op = esi_app.op['get_characters_character_id_portrait'](character_id=token.character_id)

        portrait = esiclient.request(op)

        character = EveCharacter(
                character_name=esi_verified['CharacterName'],
                character_portrait=portrait.data['px64x64'],
                token=token,
                user=request.user
        )
        character.save()

        return redirect('/eve')
    else:
        return redirect('login')