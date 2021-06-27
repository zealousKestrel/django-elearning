from django.forms import ModelForm
from .models import Assignment, Answer 

class AssignmentForm(ModelForm):
    class Meta:
        model = Assignment
        fields = ['title','lesson','content','status']

    def __init__(self,*args,**kwargs):
        super().__init__(*args,**kwargs)
        self.fields['title'].widget.attrs.update(
            {'class':'form-control'})
        self.fields['lesson'].widget.attrs.update(
            {'class':'form-control'})
        self.fields['content'].widget.attrs.update(
            {'class':'form-control'})
class AnsewrForm(ModelForm):
    class Meta:
        model = Answer
        fields = '__all__'

