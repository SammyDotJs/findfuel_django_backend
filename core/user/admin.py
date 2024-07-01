from django.contrib import admin
from .models import User,Profile

class UserAdmin(admin.ModelAdmin):
    list_display=['email','first_name','last_name','is_active']
    list_editable=['is_active']
    
    
    
    
    
    
    
    
    
class ProfileAdmin(admin.ModelAdmin):
    list_display=['user_full_name','premium','user_bio','profile_image']
    list_editable=['premium']
    def user_full_name(self, obj):
        return obj.get_user_full_name()



admin.site.register(User,UserAdmin)
admin.site.register(Profile,ProfileAdmin)