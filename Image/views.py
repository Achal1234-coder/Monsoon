from django.shortcuts import render, redirect
from django.views import generic
from .forms import FormImage
from django.contrib import messages
from django.http import HttpResponse
from .models import Image
from Account.models import User


class ImageUpload(generic.FormView):
    form_class = FormImage
    template_name = 'Image/upload.html'

    def get(self, request):
        try:
            email = request.COOKIES['email']
        except KeyError:
            return redirect('/login')
        user = User.objects.get(email=email)
        name = user.username
        return render(request, self.template_name, {'form': self.form_class, 'name': name})
    
    def post(self, request):
        
        if 'login_status' in request.COOKIES and 'email' in request.COOKIES:

            email = request.COOKIES['email']
            user = User.objects.get(email=email)
            name = user.username

            form = FormImage(request.POST, request.FILES)
            if form.is_valid():
                image = Image(title=form.cleaned_data['title'], image=form.cleaned_data['image'], descreption=form.cleaned_data['descreption'], user=user)
                image.save()
                messages.info(request, 'Image Saved')
                
                
            else:
                messages.info(request, form.errors)
            return render(request, self.template_name, {'form': self.form_class, 'name': name})
        
        return redirect('/login')
    

class ImageView(generic.FormView):
    template_name = "Image/view.html"

    def get(self, request):
        if 'login_status' in request.COOKIES and 'email' in request.COOKIES:
            email = request.COOKIES['email']
            user = User.objects.get(email=email)
            user_id = user.id
            name = user.username

            images = Image.objects.filter(user=user_id).values()

            return render(request, self.template_name, {'image': images, 'name': name})
        
        return redirect('/login')
    

def delete_image(request, id):
    Image.objects.filter(id=id).delete()
    return redirect('/view')











