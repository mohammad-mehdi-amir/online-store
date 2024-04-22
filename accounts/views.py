from django.shortcuts import redirect, render
from django.urls import reverse_lazy
# from .forms import,CustomUserChangeForm,CustomUserCreationForm
from django.views import generic
from django.contrib.auth.decorators import login_required
from .forms import *
class AccountDetailView(generic.TemplateView):
    login_required=True
    template_name='account/account_detail.html'
    
    
    
def account_nfo(request):
    user=request.user

    if request.method == 'POST':
        
        c_form=ChangeInfoForm(request.POST)
        if c_form.is_valid():
            claened_date = c_form.cleaned_data
            user.username=claened_date['username']
            user.email=claened_date['email']
            user.first_name=claened_date['first_name']
            user.last_name=claened_date['last_name']
            user.phone_number=claened_date['phone_number']
            user.save()
            return redirect('profile_info')
            
        else:
     
          
            return render(request,'account/account_info.html',{
                'form':c_form
            
        })
            
    else:        
        return render(request,'account/account_info.html',{
            'form':ChangeInfoForm()
            })