from django.contrib import admin
from django.urls import path, include
from django.conf.urls.static import static
from django.conf import settings
from rest_framework_swagger.views import get_swagger_view
from .settings import APP_ID

schema_view = get_swagger_view(
    title='Portfolio API',
)


urlpatterns = [
    path('swagger-ui/', schema_view),
    path('admin/', admin.site.urls),
]

# 3rd party services
urlpatterns += [
    path(f"api/v0/{APP_ID}/posts/", include("blog.urls"), name="blog"),
    path(f"api/v0/{APP_ID}/comments/", include("comments.urls"), name="comments"),
    path(f"api/v0/{APP_ID}/biography/", include("biography.urls"), name="biography"),
    path(f"api/v0/{APP_ID}/projects/", include("projects.urls"), name="projects"),
]

# Authentication
urlpatterns += [
    path(f"api/v0/{APP_ID}/", include("accounts.urls"), name="accounts"),
]

if settings.DEBUG:
    ''' MEDIA URL '''
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
