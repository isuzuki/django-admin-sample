from django.db import models
from django.utils import timezone


class HasTimestampModel(models.Model):
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        abstract = True


class SoftDeletionModel(models.Model):
    deleted_at = models.DateTimeField(blank=True, null=True)

    class Meta:
        abstract = True

    def delete(self):
        self.deleted_at = timezone.now()
        self.save()

    def hard_delete(self):
        super(MySoftDeletionModel, self).delete()


class Item(HasTimestampModel, SoftDeletionModel):
    name = models.CharField(max_length=255)
    category = models.ForeignKey('Category', on_delete=models.CASCADE)


class Category(HasTimestampModel, SoftDeletionModel):
    CATEGORY_CHOICES = (
        ('game', 'ゲーム'),
        ('fashion', 'ファッション'),
    )
    name = models.CharField(max_length=255)
    type = models.CharField(max_length=255, blank=True, null=True, choices=CATEGORY_CHOICES)

    def __str__(self):
        return self.name
