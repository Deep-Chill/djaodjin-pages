# Copyright (c) 2022, DjaoDjin inc.
# All rights reserved.
#
# Redistribution and use in source and binary forms, with or without
# modification, are permitted provided that the following conditions are met:
#
# 1. Redistributions of source code must retain the above copyright notice,
#    this list of conditions and the following disclaimer.
# 2. Redistributions in binary form must reproduce the above copyright
#    notice, this list of conditions and the following disclaimer in the
#    documentation and/or other materials provided with the distribution.
#
# THIS SOFTWARE IS PROVIDED BY THE COPYRIGHT HOLDERS AND CONTRIBUTORS
# "AS IS" AND ANY EXPRESS OR IMPLIED WARRANTIES, INCLUDING, BUT NOT LIMITED
# TO, THE IMPLIED WARRANTIES OF MERCHANTABILITY AND FITNESS FOR A PARTICULAR
# PURPOSE ARE DISCLAIMED. IN NO EVENT SHALL THE COPYRIGHT HOLDER OR
# CONTRIBUTORS BE LIABLE FOR ANY DIRECT, INDIRECT, INCIDENTAL, SPECIAL,
# EXEMPLARY, OR CONSEQUENTIAL DAMAGES (INCLUDING, BUT NOT LIMITED TO,
# PROCUREMENT OF SUBSTITUTE GOODS OR SERVICES; LOSS OF USE, DATA, OR PROFITS;
# OR BUSINESS INTERRUPTION) HOWEVER CAUSED AND ON ANY THEORY OF LIABILITY,
# WHETHER IN CONTRACT, STRICT LIABILITY, OR TORT (INCLUDING NEGLIGENCE OR
# OTHERWISE) ARISING IN ANY WAY OUT OF THE USE OF THIS SOFTWARE, EVEN IF
# ADVISED OF THE POSSIBILITY OF SUCH DAMAGE.

"""
API URLs for EnumeratedProgress objects
"""

from ...api.progress import EnumeratedProgressAPIView
from django.urls import re_path
from ... import settings

urlpatterns = [
    re_path(r'^(?P<sequence_slug>%s)$' % settings.SLUG_RE,
         EnumeratedProgressAPIView.as_view(
             {'get': 'list', 'post': 'create'}),
         name='api_enumerated_progress_list_create'),
    re_path(r'^(?P<sequence_slug>%s)/(?P<username>%s)$' % (settings.SLUG_RE, settings.SLUG_RE),
         EnumeratedProgressAPIView.as_view(
             {'get': 'list'}),
         name='api_enumerated_progress_user_list'),
    re_path(r'^(?P<sequence_slug>%s)/(?P<username>%s)/(?P<rank>\d+)$' % (settings.SLUG_RE, settings.SLUG_RE),
         EnumeratedProgressAPIView.as_view(
             {'get': 'retrieve', 'delete': 'destroy'}),
         name='api_enumerated_progress_user_detail'),
    re_path(r'^(?P<sequence_slug>%s)/(?P<username>%s)/(?P<rank>\d+)/ping$' % (settings.SLUG_RE, settings.SLUG_RE),
         EnumeratedProgressAPIView.as_view(
             {'post': 'ping'}),
         name='enumerated_progress_ping'),
]
