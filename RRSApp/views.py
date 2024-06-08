from django.shortcuts import render,redirect,get_object_or_404
from django.core.mail import send_mail
from .forms import AusForm,UsuserForm,ChgPwdForm,UspForm,AddTrainForm,Rtform,StoryForm
from django.contrib import messages
from .models import User,Train,Rform
from RRSProject import settings
from django.template.loader import get_template
from xhtml2pdf import pisa
from io import BytesIO
from django.core.mail import EmailMessage
from django.http import HttpResponse

# Create your views here.
def home(request):
	return render(request,'html/home.html')

def about(request):
	return render(request,'html/about.html')

def contact(request):
	return render(request,'html/contact.html')

def register(request):
	if request.method == "POST":
		f = UsuserForm(request.POST)
		if f.is_valid():
			f.save()
			messages.success(request,"User Created Successfully")
			return redirect('/lgn')
	else:
		f = UsuserForm()
	return render(request,'html/register.html',{'g':f})

def profile(request):
	return render(request,'html/profile.html')

def updprofile(request):
	k = User.objects.get(id=request.user.id)
	if request.method == "POST":
		h = UspForm(request.POST,request.FILES,instance=k)
		if h.is_valid():
			h.save()
			return redirect('/pfle')
	h = UspForm(instance=k)
	return render(request,'html/updateprofile.html',{'e':h})

def chgepwd(request):
	if request.method == "POST":
		n = ChgPwdForm(user=request.user,data=request.POST)
		if n.is_valid():
			n.save()
			return redirect('/lgn')
	n = ChgPwdForm(user=request)
	return render(request,'html/changepaswd.html',{'h':n})


def traindetail(request):
	trains = Train.objects.all()
	return render(request,'html/traindetails.html',{'trains':trains})

def addtrain(request):
    if request.method == "POST":
        form = AddTrainForm(request.POST)
        if form.is_valid():
            # Get the selected weekdays as a list
            weekdays = request.POST.getlist('weekdays')
            # Update the form's cleaned data with the list of weekdays
            form.cleaned_data['weekdays'] = weekdays
            form.save()
            messages.success(request, "Train Added Successfully")
            return redirect('/adtr')
    else:
        form = AddTrainForm()
    return render(request, 'html/addtrains.html', {'a': form})

def delete_train(request, train_id):
    train = get_object_or_404(Train, pk=train_id)
    if request.method == 'POST':
        train.delete()
        return redirect('td')
    return render(request, 'html/train_confirm_delete.html', {'train': train})
    
def reservation(request,t_id):
	train = Train.objects.get(id=t_id)
	return render(request,'html/reservation.html',{'train':train})

def send_ticket_email(request, train):
    template = get_template('html/ticket_pdf.html')
    context = {'train': train}
    html_content = template.render(context)

    # Create a PDF file
    pdf_data = BytesIO()
    pdf = pisa.pisaDocument(BytesIO(html_content.encode("UTF-8")), pdf_data)

    if not pdf.err:
        pdf_file = pdf_data.getvalue()
        subject = 'Ticket Booking Confirmation'
        message = 'Your ticket details are attached.'
        recipient_email = request.user.email

        # Create EmailMessage object
        email = EmailMessage(
            subject=subject,
            body=message,
            from_email='your_email@gmail.com',
            to=[recipient_email],
        )
        
        # Attach PDF file
        email.attach('Ticket.pdf', pdf_file, 'application/pdf')

        # Send email
        email.send()
        
        return HttpResponse(pdf_file, content_type='application/pdf')
    else:
        return HttpResponse("Error generating PDF: {}".format(pdf.err))

def send_cancellation_email(ticket, user):
    template = get_template('html/cancellation_pdf.html')
    context = {'ticket': ticket}
    html_content = template.render(context)

    # Create a PDF file
    pdf_data = BytesIO()
    pdf = pisa.pisaDocument(BytesIO(html_content.encode("UTF-8")), pdf_data)

    if not pdf.err:
        pdf_file = pdf_data.getvalue()
        subject = 'Ticket Cancellation Confirmation'
        message = 'Your ticket for train {} from {} to {} has been canceled.'.format(ticket.train.trainnum, ticket.train.trainsrc, ticket.train.traindes)
        recipient_email = user.email

        # Create EmailMessage object
        email = EmailMessage(
            subject=subject,
            body=message,
            from_email='your_email@gmail.com',
            to=[recipient_email],
        )
        
        # Attach PDF file
        email.attach('Cancellation.pdf', pdf_file, 'application/pdf')

        # Send email
        email.send()

        return HttpResponse(pdf_file, content_type='application/pdf')
    else:
        return HttpResponse("Error generating PDF: {}".format(pdf.err))

def conres(request, train_id):
    train = Train.objects.get(id=train_id)
    if request.method == 'POST':
        form = Rtform(request.POST)
        if form.is_valid():
            rform = form.save(commit=False)
            rform.train = train
            rform.save()
            send_ticket_email(request, train)
            #return redirect('/')  
            return render(request, 'html/index.html', {'form': form, 'train': train})
    else:
        form = Rtform(initial={'train': train})
    return render(request, 'html/confres.html', {'form': form, 'train': train})

def your_tickets(request):
    user_tickets = Rform.objects.filter(usname=request.user.username)
    return render(request, 'html/yourtickets.html', {'user_tickets': user_tickets})

def cancel_ticket(request, ticket_id):
    ticket = get_object_or_404(Rform, pk=ticket_id)
    user = User.objects.get(username=ticket.usname)  
    ticket.delete()

    send_cancellation_email(ticket, user)

    return redirect('/yourtickets') 

def edit_train(request, train_id):
    train = get_object_or_404(Train, pk=train_id)
    if request.method == 'POST':
        form = AddTrainForm(request.POST, instance=train)
        if form.is_valid():
            form.save()
            return redirect('/trd')
    else:
        form = AddTrainForm(instance=train)
    return render(request, 'html/edit_train.html', {'form': form})

def writestory(request):
    if request.method == 'POST':
        form = StoryForm(request.POST)
        if form.is_valid():
            form.save()  
            return redirect('/create_story')
    else:
        form = StoryForm()
    return render(request, 'html/story.html', {'form': form})