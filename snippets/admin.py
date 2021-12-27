from django.contrib import admin

from snippets.models import ShortSnippet, Tag


class ShortSnippetAdmin(admin.ModelAdmin):
    """
    ShortSnippet Admin for ShortSnippet model
    """

    search_fields = ['title']
    list_display = ['created_by', 'created_on', 'modified_on']
    exclude = ('created_by', 'modified_by')

    def save_model(self, request, obj, form, change):
        if change:
            obj.modified_by = request.user
        else:
            obj.created_by = request.user
            obj.modified_by = request.user
        super(ShortSnippetAdmin, self).save_model(request, obj, form, change)


class TagAdmin(admin.ModelAdmin):
    """
    Tag Admin for Tag model
    """

    search_fields = ['title']


admin.site.register(ShortSnippet, ShortSnippetAdmin)
admin.site.register(Tag, TagAdmin)
