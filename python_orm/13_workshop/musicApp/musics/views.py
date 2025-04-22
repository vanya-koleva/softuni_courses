from django.shortcuts import render, redirect

from musicApp.settings import session
from musicApp.utils import handle_session
from musics.forms import AlbumCreateForm
from musics.models import Album


@handle_session(session)
def index(request):
    context = {
        'albums': session.query(Album).all()
    }

    return render(request, 'common/index.html', context)


@handle_session(session)
def create_album(request):
    context = {
        'form': AlbumCreateForm(),
    }

    if request.method == 'POST':
        form = AlbumCreateForm(request.POST)

        if form.is_valid():
            new_album = Album(
                album_name=form.cleaned_data['album_name'],
                image_url=form.cleaned_data['image_url'],
                price=form.cleaned_data['price'],
            )

            session.add(new_album)

            return redirect('index')

    return render(request, 'albums/create-album.html', context)


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
    return render(request, 'songs/create-song.html')
