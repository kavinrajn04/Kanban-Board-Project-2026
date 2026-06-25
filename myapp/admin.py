from django.contrib import admin
from myapp.models import Note

# Register your models here.


class NoteAdmin(admin.ModelAdmin):
    list_display = ("user", "title", "content", "created_at")


admin.site.register(Note, NoteAdmin)
