from django.contrib import admin
from .models import *

# Register your models here.
admin.site.register(Novel)
admin.site.register(Reader)
admin.site.register(Marker)
admin.site.register(Bookmark)
admin.site.register(Setting)
admin.site.register(Comment)
admin.site.register(Request)
