from tastypie.resources import ModelResource
from models import *

class UserResource(ModelResource):
    class Meta:
        queryset = AppUser.objects.all()
        resource_name = 'user'
        allowed_methods = ['get']

class EventResource(ModelResource):
    class Meta:
        queryset = Event.objects.all()
        resource_name = 'event'
        allowed_methods = ['get']

class CategoryResource(ModelResource):
    class Meta:
        queryset = Category.objects.all()
        resource_name = 'category'
        allowed_methods = ['get']
