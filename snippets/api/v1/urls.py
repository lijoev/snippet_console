from rest_framework import routers

from snippets.api.v1.views import SnippetViewSet, TagViewSet

router = routers.SimpleRouter()
router.register(r'snippets', SnippetViewSet, basename='snippets')
router.register(r'tags', TagViewSet, basename='tags')

urlpatterns = router.urls
