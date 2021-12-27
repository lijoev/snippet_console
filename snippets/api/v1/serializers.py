from django.urls import reverse
from rest_framework import serializers

from snippets.models import ShortSnippet, Tag


class ShortSnippetListSerializer(serializers.ModelSerializer):
    """
    Model serializer class for Listing ShortSnippet
    """
    detail_url = serializers.SerializerMethodField()

    class Meta:
        model = ShortSnippet
        fields = ('id', 'title', 'detail_url')

    @staticmethod
    def get_detail_url(obj):
        """
        Return detail url endpoint for a specific
        snippet
        """
        url = reverse(
            'snippets-detail',
            kwargs={'pk': obj.pk},
        )
        return url


class ShortSnippetDetailSerializer(serializers.ModelSerializer):
    """
    Model serializer class for ShortSnippet Detail view
    """

    class Meta:
        model = ShortSnippet
        fields = '__all__'


class TagListSerializer(serializers.ModelSerializer):
    """
    Model serializer class for Tags
    """

    class Meta:
        model = Tag
        fields = '__all__'


class TagDetailsSerializer(serializers.ModelSerializer):
    """
    Model serializer class for Tag detail view
    """
    shortsnippet_set = ShortSnippetListSerializer(read_only=True, many=True)

    class Meta:
        model = Tag
        fields = (
            'id',
            'title',
            'shortsnippet_set',
        )



