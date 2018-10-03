from django import forms

from pagedown.widgets import PagedownWidget

from .models import Post
from .models import Comment



class PostForm(forms.ModelForm):
	text=forms.CharField(widget=PagedownWidget)

	publish=forms.DateField(widget=forms.SelectDateWidget)

	class Meta:
		model = Post
		fields = ('title', 'text',)
class CommentForm(forms.ModelForm):
	class Meta:
		model=Comment
		fields=[
		'name',
		'email',
		'body'
		] 
