from django import forms

class ArticleForm(forms.Form):
    title = forms.CharField()
    content = forms.CharField()

    def clean(self): # can also do clean_title or _content...
        cleaned_data = self.cleaned_data # dictionary
        print("cleaned_data", cleaned_data)
        title = cleaned_data.get('title')
        content = cleaned_data.get('content')
        if title.lower().strip() == "the office":
            self.add_error('title', 'This title is taken')
            # you'd do the below if its a clean_title method
            # raise forms.ValidationError('This title is taken')
        if "office" in content.lower():
            self.add_error('content', 'Office cannot be in content')
            raise forms.ValidationError('You may not speak of the office')
        print('cleaned title',title)
        return cleaned_data