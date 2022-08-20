# Copyright (c) 2020, DjaoDjin inc.
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
API URLs for readers who must be authenticated
"""
from ... import settings
from ...compat import re_path

from ...api.reactions import (FollowAPIView, UnfollowAPIView, UpvoteAPIView,
  DownvoteAPIView, CommentListCreateAPIView)

urlpatterns = [
    # Following
    re_path(r'^follow/(?P<path>%s)$' % settings.PATH_RE,
        FollowAPIView.as_view(), name='pages_api_follow'),
    re_path(r'^unfollow/(?P<path>%s)$' % settings.PATH_RE,
        UnfollowAPIView.as_view(), name='pages_api_unfollow'),
    # Votes
    re_path(r'^upvote/(?P<path>%s)$' % settings.PATH_RE,
        UpvoteAPIView.as_view(), name='pages_api_upvote'),
    re_path(r'^downvote/(?P<path>%s)$' % settings.PATH_RE,
        DownvoteAPIView.as_view(), name='pages_api_downvote'),
    # Comments
    re_path(r'^comments/(?P<path>%s)$' % settings.PATH_RE,
        CommentListCreateAPIView.as_view(), name='pages_api_comments'),
]
