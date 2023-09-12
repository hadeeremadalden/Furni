from django.contrib import admin

# Register your models here.
from .models import *

admin.site.register(Services)
admin.site.register(Team)
admin.site.register(Testimonials)
admin.site.register(Header)

