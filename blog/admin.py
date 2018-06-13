from django.contrib import admin
from .models import Gonderi, Comment, Categories


class CategoryAdmin(admin.ModelAdmin):
   list_display = ('name', 'slug')
   prepopulated_fields = {'slug': ('name',)}


admin.site.register(Gonderi)
admin.site.register(Comment)
admin.site.register(Categories, CategoryAdmin)
