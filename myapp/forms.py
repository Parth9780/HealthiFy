from django import forms
from.models import Register_Form,Appointment,ContactUs,AdminLogin

class RegisterForm(forms.ModelForm):
    class Meta:
        model = Register_Form
        fields = '__all__'

class LoginForm(forms.Form):
    Email = forms.EmailField()
    Password = forms.CharField(widget=forms.PasswordInput)
    
class UpdateProfile(forms.ModelForm):
    class Meta:
        model = Register_Form
        fields = ['Name','Mobile','Email','Password']

class AppointmentForm(forms.ModelForm):
    class Meta:
        model = Appointment
        fields = '__all__'
        
class ContactUsForm(forms.ModelForm):
    class Meta:
        model = ContactUs
        fields = ('Name', 'Phone', 'Email', 'Message')

class UpdateAppointment(forms.ModelForm):
    class Meta:
        model = Appointment
        fields = ('Name','Mobile','Email','Date')

class AdminLoginForm(forms.ModelForm):
    class Meta:
        model = AdminLogin
        fields = '__all__'