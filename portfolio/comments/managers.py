from django.contrib.contenttypes.models import ContentType
from django.db import models


class CommentManager(models.Manager):

    def all(self):
        queryset = super(CommentManager, self).filter(parent=None)
        return queryset

    def filter_by_instance(self, instance):
        content_type = ContentType.objects.get_for_model(instance.__class__)
        object_id = instance.id

        queryset = super(CommentManager, self).filter(
            content_type=content_type,
            object_id=object_id,
        ).filter(parent=None)

        return queryset

    def create_by_model_type(self, model_type, slug, content, user, parent_obj=None):
        model_queryset = ContentType.objects.filter(model=model_type)
        if model_queryset.exists():
            SomeModel = model_queryset.first().model_class()
            obj_queryset = SomeModel.objects.filter(slug=slug)
            if obj_queryset.exists() and obj_queryset.count() == 1:
                instance = self.model()
                instance.slug = slug
                instance.content = content
                instance.user = user
                instance.content_type = model_queryset.first()
                instance.object_id = obj_queryset.first().id
                if parent_obj:
                    instance.parent = parent_obj

                instance.save()

                return instance

        return None
