from django.contrib import admin
from .models import Comment,Category,Blog,Tags
from parler.admin import TranslatableAdmin

# Register your models here.

@admin.register(Category)
class CategoryAdmin(TranslatableAdmin):
    list_display = ['name','slug']
admin.site.register(Blog)
admin.site.register(Comment)
admin.site.register(Tags)