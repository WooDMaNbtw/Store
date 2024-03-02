from django.contrib import admin
from django.urls import path, include
from django.conf.urls.static import static
from django.conf import settings

from rest_framework_swagger.views import get_swagger_view

schema_view = get_swagger_view(
    title='Portfolio API',
)


urlpatterns = [
    path('swagger-ui/', schema_view),
    path('admin/', admin.site.urls),
    path("api/v0/posts/", include("blog.urls"), name="blog"),
    path("api/v0/comments/", include("comments.urls"), name="comments"),
    path("api/v0/users/", include("accounts.urls"), name="accounts"),
    path("api/v0/biography/", include("biography.urls"), name="biography"),
    path("api/v0/projects/", include("projects.urls"), name="projects")
]

if settings.DEBUG:
    ''' MEDIA URL '''
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
