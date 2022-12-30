from django import forms


class FO_addtask(forms.Form):
    title = forms.CharField(label="Task Title", max_length=200,
                            required=True,
                            widget=forms.TextInput(attrs={'class': 'inputt'}))
    description = forms.CharField(label="Task description",
                                  widget=forms.Textarea(attrs={'class': 'inputt'}))


class FO_addproject(forms.Form):
    name = forms.CharField(label="Project Name",
                           max_length=200,
                           required=True,
                           widget=forms.TextInput(attrs={'class': 'inputt'}))
