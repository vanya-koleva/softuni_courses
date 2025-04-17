from django.shortcuts import render

from musicApp.settings import session
from musicApp.utils import handle_session


@handle_session(session)
def index(request):
    ...


@handle_session(session)
def create_album(request):
    ...


@handle_session(session)
def edit_album(request, pk: int):
    ...


@handle_session(session)
def delete_album(request, pk: int):
    ...


@handle_session(session)
def album_details(request, pk: int):
    ...


@handle_session(session)
def create_song(request):
    ...
