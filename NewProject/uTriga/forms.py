from django import forms
from models import Event
from django.contrib.admin import widgets                                       


class EventForm(forms.ModelForm):
    class Meta:
        model = Event
    def __init__(self, *args, **kwargs):
        super(EventForm, self).__init__(*args, **kwargs)
        self.fields['event_date'].widget = widgets.AdminDateWidget()
        #self.fields['mytime'].widget = widgets.AdminTimeWidget()
        #self.fields['mydatetime'].widget = widgets.AdminSplitDateTime()
