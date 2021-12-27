from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework.viewsets import ModelViewSet

from snippets.api.v1.serializers import (ShortSnippetListSerializer,
                                         ShortSnippetDetailSerializer,
                                         TagListSerializer,
                                         TagDetailsSerializer)
from snippets.models import ShortSnippet, Tag


class SnippetViewSet(ModelViewSet):
    """
    Class which lists, filter Snippets
    """
    permission_classes = [IsAuthenticated]
    serializer_class = ShortSnippetListSerializer
    model = ShortSnippet
    queryset = ShortSnippet.objects.all()

    def list(self, request, *args, **kwargs):
        """
        List api for ShortSnippet
        @param request: current request object
        @param args:
        @param kwargs:
        @return: list of ShortSnippet
        """
        queryset = self.filter_queryset(self.get_queryset())
        page = self.paginate_queryset(queryset)
        if page is not None:
            serializer = self.get_serializer(page, many=True)
            return self.get_paginated_response(serializer.data)

        serializer = self.get_serializer(queryset, many=True)
        return self.get_paginated_response(serializer.data)

    def retrieve(self, request, *args, **kwargs):
        """
        Retrieve snippet object
        """
        instance = self.get_object()
        serializer = ShortSnippetDetailSerializer(instance)
        return Response(serializer.data)

    def create(self, request, *args, **kwargs):
        """
        Create method to create a snippet and link a tag to it
        """
        data = request.data.copy()
        title = data.get('title', None)
        serializer_data = ShortSnippetDetailSerializer(data=data)
        if serializer_data.is_valid():
            tag_obj, created = Tag.objects.get_or_create(
                title=title,
            )
            obj = serializer_data.save()
            obj.tag = tag_obj
            obj.save(update_fields=["tag"])
            return Response(serializer_data.data)
        else:
            return Response(serializer_data.errors)

    def update(self, request, *args, **kwargs):
        """
        update a snippet object
        """
        partial = kwargs.pop('partial', False)
        instance = self.get_object()
        serializer = ShortSnippetDetailSerializer(instance, data=request.data,
                                                  partial=partial)
        serializer.is_valid(raise_exception=True)
        self.perform_update(serializer)
        if getattr(instance, '_prefetched_objects_cache', None):
            # If 'prefetch_related' has been applied to a queryset, we need to
            # forcibly invalidate the prefetch cache on the instance.
            instance._prefetched_objects_cache = {}

        return Response(serializer.data)

    def destroy(self, request, *args, **kwargs):
        """
        Delete a snippet object
        """
        instance = self.get_object()
        self.perform_destroy(instance)
        queryset = self.filter_queryset(self.get_queryset())
        page = self.paginate_queryset(queryset)
        if page is not None:
            serializer = self.get_serializer(page, many=True)
            return self.get_paginated_response(serializer.data)

        serializer = self.get_serializer(queryset, many=True)
        return self.get_paginated_response(serializer.data)


class TagViewSet(ModelViewSet):
    """
    Class which lists, filter Tag
    """
    permission_classes = [IsAuthenticated]
    serializer_class = TagListSerializer
    model = Tag
    queryset = Tag.objects.all()

    def list(self, request, *args, **kwargs):
        """
        List api for Tags
        @param request: current request object
        @param args:
        @param kwargs:
        @return: list of Tags
        """
        queryset = self.filter_queryset(self.get_queryset())
        page = self.paginate_queryset(queryset)
        if page is not None:
            serializer = self.get_serializer(page, many=True)
            return self.get_paginated_response(serializer.data)

        serializer = self.get_serializer(queryset, many=True)
        return self.get_paginated_response(serializer.data)

    def retrieve(self, request, *args, **kwargs):
        """
        Retrieve tag object
        """
        instance = self.get_object()
        serializer = TagDetailsSerializer(instance)
        return Response(serializer.data)
