from django.shortcuts import render
from django.http import HttpResponse
from AppTwo.forms import NewUserForm, UploadFileForm
from AppTwo.functions import handle_uploaded_file

# Create your views here.
def index(response):
    return render(response,'app_two/index.html')

def help(response):
    return render(response,'app_two/help.html')

def users(request):

    form = NewUserForm()

    if request.method == "POST":
        form = NewUserForm(request.POST)

        if form.is_valid():
            form.save(commit=True)
            return index(request)
        else:
            print('ERROR FORM INVALID')

    return render(request,'app_two/user.html',{'form':form})

def upload_file(request):
    if request.method == 'POST':
        form = UploadFileForm(request.POST, request.FILES)
        if form.is_valid():
            DNL_IMG = open(handle_uploaded_file(request.FILES['file']),'rb').read()
            response = HttpResponse((DNL_IMG), content_type='image/jpeg')
            response['Content-Disposition'] = 'attachment;'
            return response
    else:
        form = UploadFileForm()
    return render(request, 'app_two/upload.html', {'form': form})