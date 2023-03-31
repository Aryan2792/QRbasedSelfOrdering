from django.contrib import admin
from .models import *
# Register your models here.

class CategoryAdmin(admin.ModelAdmin):
    pass

class DishesAdmin(admin.ModelAdmin):
    list_display = ('id',"__str__",'price','show_image','category')
    list_display_links = ()
    list_filter = ('category',)
    list_select_related = False
    list_per_page = 100
    list_max_show_all = 200
    list_editable = ()
    search_fields = ()
    search_help_text = None
    date_hierarchy = None
    save_as = False
    save_as_continue = True
    save_on_top = False
    preserve_filters = True
    inlines = []
    # Actions
    actions = []
    actions_on_top = True
    actions_on_bottom = False
    actions_selection_counter = True


admin.site.register(Category, CategoryAdmin)
admin.site.register(Dishes, DishesAdmin)