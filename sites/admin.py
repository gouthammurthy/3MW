from django.contrib import admin
from .models import Site, Detail

# To be able to edit in the admin page
admin.site.register(Site)
admin.site.register(Detail)
