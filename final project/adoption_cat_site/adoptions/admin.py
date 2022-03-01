from django.contrib import admin
from .models import Cat, Cat_Details

class ChoiceInline(admin.TabularInline):
    model = Cat_Details
    extra = 0

class CatAdmin(admin.ModelAdmin):
    fieldsets = [(None, {'fields': ['cat_name_text']}),('Date information', {'fields': ['pub_date']}),
                 ("Adoption information", {'fields': ['adopted', 'adoption_date', 'human']})]

    inlines = [ChoiceInline]
    list_display = ('cat_name_text', 'pub_date')
    list_filter = ['pub_date']
    search_fields = ['cat_name_text']

admin.site.register(Cat, CatAdmin)

