from django import forms
COURCE_CHOICES=(
('NONE','NONE'),
('Website Development','Website Development'),
('Mobile Development','Mobile Development'),
('Vacation Cources','Vacation Cources'),
('Short Cources','Short Cources'),
('Live Project Training','Live Project Training'),
('BCA Coaching','BCA Coaching'),
)
class EnquiryForm(forms.Form):
    FirstName=forms.CharField(widget=forms.TextInput(attrs={
    'class': "form-control",
    'placeholder':'First Name',
    }),label="First Name")
    LastName=forms.CharField(widget=forms.TextInput(attrs={
    'class': "form-control",
    'placeholder':'Last Name',
    }),label="Last Name")
    PhoneNumber=forms.CharField(max_length=50,widget=forms.TextInput(attrs={
    'class': "form-control",
    }),label="Phone Number")
    Email = forms.EmailField(max_length=254,widget=forms.EmailInput(attrs={
    'placeholder':'abc@xyz.com',
    'class': "form-control",
    }),label="Email")
    Course=forms.CharField(widget=forms.Select(choices=COURCE_CHOICES,attrs={
    'class': "form-control",
    }))
    Message=forms.CharField(widget=forms.TextInput(attrs={
    'class': "form-control",
    }))

    def clean_course(self):
        course = self.cleaned_data['Course']
        if course <= 0:
            raise forms.ValidationError("You need to select a Course.")
