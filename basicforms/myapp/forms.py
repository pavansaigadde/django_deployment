from django import forms
 
class FormName(forms.Form):

	#Class object attributes
	name=forms.CharField()
	email=forms.EmailField()
	text=forms.CharField(widget=forms.Textarea)


	def __str__(self):
		return 'self.name'