from typing import Optional

from django.db.models import QuerySet
from django.views.generic import DetailView
from common.utils import get_profile


class ProfileDetailView(DetailView):
    template_name = 'profile-details.html'

    def get_object(self, queryset: Optional[QuerySet] = None) -> QuerySet:
        return get_profile()

