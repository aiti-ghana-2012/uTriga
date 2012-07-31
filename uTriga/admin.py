from django.contrib import admin
from uTriga.models import Event,Advertiser,Category,AppUser


class EventInline(admin.TabularInline):
    model=Event

    
##class NewsInline(admin.TabularInline):
##    model=News

    
class UserEventInline(admin.TabularInline):
    model=AppUser.event.through

##class UserNewsInline(admin.TabularInline):
##    model=AppUser.news.through    

class EventCategoryInline(admin.TabularInline):
    model=Event.event_category.through

##class NewsCategoryInline(admin.TabularInline):
##    model=News.event_category.through   
##

    
class AdvertiserInline(admin.TabularInline):
    model=Advertiser

    
class EventAdmin(admin.ModelAdmin):
    list_display=('event_name','event_date','event_time','created','updated')
    search_fields=('event_name','event_date','event_time','created','updated')
    list_filter=('event_name','event_date','event_time','created','updated')
    inlines=[UserEventInline]

class AdvertiserAdmin(admin.ModelAdmin):
    list_display=('brand_name','licence_ticket','num_of_posts','phone_number')
    list_filter=('brand_name','num_of_posts','licence_ticket')
    search_fields=('brand_name','num_of_posts','licence_ticket')
    inlines=[EventInline]

class CategoryAdmin(admin.ModelAdmin):
    list_display=('category_name',)
    list_filter=('category_name',)
    search_fields=('category_name',)
    inlines=[EventCategoryInline]

class UserAdmin(admin.ModelAdmin):
    list_display=('mobile_num','username','email','birth_date')
    list_filter=('mobile_num','username')
    inlines=[UserEventInline]

##class NewsAdmin(admin.ModelAdmin):
##    list_display=('news_title','created')
##    search_fields=('news_title',)
##    list_filter=('created',)
##    inlines=[UserNewsInline]


admin.site.register(Event,EventAdmin)
#admin.site.register(News,NewsAdmin)
admin.site.register(AppUser,UserAdmin)
admin.site.register(Category,CategoryAdmin)
admin.site.register(Advertiser,AdvertiserAdmin)





