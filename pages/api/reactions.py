# Copyright (c) 2020, DjaoDjin inc.
# All rights reserved.
#
# Redistribution and use in source and binary forms, with or without
# modification, are permitted provided that the following conditions are met:
#
# 1. Redistributions of source code must retain the above copyright notice,
#    this list of conditions and the following disclaimer.
# 2. Redistributions in binary form must reproduce the above copyright notice,
#    this list of conditions and the following disclaimer in the documentation
#    and/or other materials provided with the distribution.
#
# THIS SOFTWARE IS PROVIDED BY THE COPYRIGHT HOLDERS AND CONTRIBUTORS "AS IS"
# AND ANY EXPRESS OR IMPLIED WARRANTIES, INCLUDING, BUT NOT LIMITED TO,
# THE IMPLIED WARRANTIES OF MERCHANTABILITY AND FITNESS FOR A PARTICULAR
# PURPOSE ARE DISCLAIMED. IN NO EVENT SHALL THE COPYRIGHT HOLDER OR
# CONTRIBUTORS BE LIABLE FOR ANY DIRECT, INDIRECT, INCIDENTAL, SPECIAL,
# EXEMPLARY, OR CONSEQUENTIAL DAMAGES (INCLUDING, BUT NOT LIMITED TO,
# PROCUREMENT OF SUBSTITUTE GOODS OR SERVICES; LOSS OF USE, DATA, OR PROFITS;
# OR BUSINESS INTERRUPTION) HOWEVER CAUSED AND ON ANY THEORY OF LIABILITY,
# WHETHER IN CONTRACT, STRICT LIABILITY, OR TORT (INCLUDING NEGLIGENCE OR
# OTHERWISE) ARISING IN ANY WAY OUT OF THE USE OF THIS SOFTWARE, EVEN IF
# ADVISED OF THE POSSIBILITY OF SUCH DAMAGE.
from __future__ import unicode_literals

from rest_framework import generics, status
from rest_framework.response import Response

from ..mixins import PageElementMixin
from ..models import Follow, Vote
from ..serializers import CommentSerializer, PageElementSerializer


class FollowAPIView(PageElementMixin, generics.CreateAPIView):
    """
    Follow a page element

    The authenticated user making the request will receive notification
    whenever someone comments on the practice.

    **Tags**: content

    **Examples**

    .. code-block:: http

         POST /api/content/follow/adjust-air-fuel-ratio HTTP/1.1

    .. code-block:: json

         {}

    responds

    .. code-block:: json

        {
            "slug": "water-user",
            "title": "How to reduce water usage?"
        }
    """
    serializer_class = PageElementSerializer

    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        self.perform_create(serializer)
        headers = self.get_success_headers(serializer.data)
        return Response(PageElementSerializer().to_representation(
            self.get_object()), status=status.HTTP_201_CREATED, headers=headers)

    def perform_create(self, serializer):
        if self.request.user.is_authenticated():
            Follow.objects.subscribe(self.get_object(), user=self.request.user)


class UnfollowAPIView(PageElementMixin, generics.CreateAPIView):
    """
    Unfollow a page element

    The authenticated user making the request will stop receiving notification
    whenever someone comments on the practice.

    **Tags**: content

    **Examples**

    .. code-block:: http

         POST /api/content/unfollow/adjust-air-fuel-ratio HTTP/1.1

    .. code-block:: json

         {}

    responds

    .. code-block:: json

        {
            "slug": "water-user",
            "title": "How to reduce water usage?"
        }
    """
    serializer_class = PageElementSerializer

    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        self.perform_create(serializer)
        headers = self.get_success_headers(serializer.data)
        return Response(PageElementSerializer().to_representation(
            self.get_object()), status=status.HTTP_201_CREATED, headers=headers)

    def perform_create(self, serializer):
        if self.request.user.is_authenticated():
            Follow.objects.unsubscribe(
                self.get_object(), user=self.request.user)


class UpvoteAPIView(PageElementMixin, generics.CreateAPIView):
    """
    Upvote a page element

    The authenticated user making the request indicates the practice is
    considered worthwhile implementing.

    **Tags**: content

    **Examples**

    .. code-block:: http

         POST /api/content/upvote/adjust-air-fuel-ratio HTTP/1.1

    .. code-block:: json

         {}

    responds

    .. code-block:: json

        {
            "slug": "water-user",
            "title": "How to reduce water usage?"
        }
    """
    serializer_class = PageElementSerializer

    def perform_create(self, serializer):
        if self.request.user.is_authenticated():
            Vote.objects.vote_up(self.get_object(), user=self.request.user)


class DownvoteAPIView(PageElementMixin, generics.CreateAPIView):
    """
    Downvote a page element

    The authenticated user making the request indicates the practice is
    not worth implementing.

    **Tags**: content

    **Examples**

    .. code-block:: http

         POST /api/content/downvote/adjust-air-fuel-ratio HTTP/1.1

    .. code-block:: json

         {}

    responds

    .. code-block:: json

        {
            "slug": "water-user",
            "title": "How to reduce water usage?"
        }
    """
    serializer_class = PageElementSerializer

    def perform_create(self, serializer):
        if self.request.user.is_authenticated():
            Vote.objects.vote_down(self.get_object(), user=self.request.user)


class CommentListCreateAPIView(PageElementMixin, generics.ListCreateAPIView):

    serializer_class = CommentSerializer

    def get(self, request, *args, **kwargs):
        """
        List comments on a page element

        **Tags**: content

        **Examples**

        .. code-block:: http

             GET /api/content/comments/adjust-air-fuel-ratio HTTP/1.1

        responds

        .. code-block:: json

            {
              "count": 1,
              "next": null,
              "previous": null,
              "results": [
                {
                  "created_at": "2020-09-28T00:00:00.0000Z",
                  "user": "steve",
                  "text": "How long does it take to see improvements?"
                }
              ]
            }
        """
        #pylint:disable=useless-super-delegation
        return super(CommentListCreateAPIView, self).get(
            request, *args, **kwargs)

    def post(self, request, *args, **kwargs):
        """
        Comment on a page element

        **Tags**: content

        **Examples**

        .. code-block:: http

             POST /api/content/comments/adjust-air-fuel-ratio HTTP/1.1

        .. code-block:: json

            {
                "text": "How long does it take to see improvements?"
            }

        responds

        .. code-block:: json

            {
              "created_at": "2020-09-28T00:00:00.0000Z",
              "user": "steve",
              "text": "How long does it take to see improvements?"
            }
        """
        #pylint:disable=useless-super-delegation
        return super(CommentListCreateAPIView, self).post(
            request, *args, **kwargs)
