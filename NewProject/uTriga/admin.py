from django.contrib import admin
from uTriga.models import Event,Advertiser,Category,User,News


class EventInline(admin.TabularInline):
    model=Event

    
class NewsInline(admin.TabularInline):
    model=News

    
class UserEventInline(admin.TabularInline):
    model=User.event.through

class UserNewsInline(admin.TabularInline):
    model=User.news.through    

class EventCategoryInline(admin.TabularInline):
    model=Event.event_category.through

class NewsCategoryInline(admin.TabularInline):
    model=News.event_category.through   


    
class AdvertiserInline(admin.TabularInline):
    model=Advertiser

class NewsAdmin(admin.ModelAdmin):
    list_display=('news_title','created')
    search_fields=('news_title',)
    list_filter=('created',)
    inlines=[UserNewsInline]
    
class EventAdmin(admin.ModelAdmin):
    list_display=('event_name','created','updated')
    search_fields=('event_name',)
    list_filter=('created',)
    inlines=[UserEventInline]

class AdvertiserAdmin(admin.ModelAdmin):
    list_display=('advertiser_name',)
    list_filter=('advertiser_name',)
    search_fields=('advertiser_name',)
    inlines=[EventInline]

class CategoryAdmin(admin.ModelAdmin):
    list_display=('category_name',)
    list_filter=('category_name',)
    search_fields=('category_name',)
    inlines=[EventCategoryInline,NewsCategoryInline]

class UserAdmin(admin.ModelAdmin):
    list_display=('mobile_num','username','email')
    list_filter=('mobile_num','username')
    #inlines=[EventInline]


admin.site.register(Event,EventAdmin)
admin.site.register(News,NewsAdmin)
admin.site.register(User,UserAdmin)
admin.site.register(Category,CategoryAdmin)
admin.site.register(Advertiser,AdvertiserAdmin)





