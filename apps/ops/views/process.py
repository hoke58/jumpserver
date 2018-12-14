# -*- coding: utf-8 -*-
#

from django.utils.translation import ugettext as _
from django.conf import settings
from django.views.generic import ListView, DetailView, TemplateView, View
from common.mixins import DatetimeSearchMixin
from django.contrib.auth.mixins import LoginRequiredMixin
from common.permissions import SuperUserRequiredMixin, AdminUserRequiredMixin

__all__ = [
    'ProcessContrlView'
]


class ProcessContrlView(LoginRequiredMixin, TemplateView):
    template_name = 'ops/process.html'

    def get_context_data(self, **kwargs):
        context = {
            'app': _('Ops'),
            'action': _('Process Control'),
            'src_url': settings.SUPERVISORD_URL,
        }
        kwargs.update(context)
        return super().get_context_data(**kwargs)