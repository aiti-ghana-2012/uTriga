
from tastypie.resources import ModelResource, ALL, ALL_WITH_RELATIONS
from tastypie import fields
from models import *

class UserResource(ModelResource):
    class Meta:
        queryset = AppUser.objects.all()
        resource_name = 'user'
        allowed_methods = ['get']

class CategoryResource(ModelResource):
    class Meta:
        queryset = Category.objects.all()
        resource_name = 'category'
        allowed_methods = ['get']
        filtering = {
            'id': ALL,
            }

class EventResource(ModelResource):
    category = fields.ToManyField(CategoryResource,'event_category')
    class Meta:
        queryset = Event.objects.all()
        resource_name = 'event'
        allowed_methods = ['get']
        filtering = {
            'category': ALL_WITH_RELATIONS,
            }

