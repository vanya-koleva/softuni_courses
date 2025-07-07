from django.http import HttpResponseRedirect
from django.urls import reverse_lazy
from django.views.generic import CreateView, DetailView, UpdateView, DeleteView
from albums.forms import AlbumCreateForm, AlbumEditForm, AlbumDeleteForm
from albums.models import Album
from common.utils import get_profile


class AlbumCreateView(CreateView):
    model = Album
    form_class = AlbumCreateForm
    template_name = 'album-add.html'
    success_url = reverse_lazy('home')

    def form_valid(self, form: AlbumCreateForm) -> HttpResponseRedirect:
        form.instance.owner = get_profile()
        return super().form_valid(form)


class AlbumDetailsView(DetailView):
    model = Album
    template_name = 'album-details.html'
    pk_url_kwarg = 'id'


class AlbumEditView(UpdateView):
    model = Album
    form_class = AlbumEditForm
    template_name = 'album-edit.html'
    pk_url_kwarg = 'id'
    success_url = reverse_lazy('home')


class AlbumDeleteView(DeleteView):
    model = Album
    form_class = AlbumDeleteForm
    template_name = 'album-delete.html'
    pk_url_kwarg = 'id'
    success_url = reverse_lazy('home')

    def get_initial(self) -> dict:
        return self.object.__dict__

    def form_invalid(self, form: AlbumDeleteForm):
        return self.form_valid(form)
