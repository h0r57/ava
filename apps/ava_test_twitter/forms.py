from django.forms import ModelForm, Form
from apps.ava_test_twitter.models import *


class TwitterTestForm(ModelForm):
    class Meta:
        model = TwitterTest
        #fields = ('name',  'description', 'testtype', 'timingtype','targettype')