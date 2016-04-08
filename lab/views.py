from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User
from django.shortcuts import redirect
from django.shortcuts import render

from .forms import AuthenticationForm
from .forms import RegistrationForm

from .models import Reservation
from .models import ReservationDate

# Create your views here.
def index(request):
	return render(request, 'lab/base.html')

def aboutus(request):
	return render(request, 'lab/aboutus.html')

def contactus(request):
	return render(request, 'lab/contactus.html')

def learn(request):
	return render(request, 'lab/learn.html')

def live(request):
	return render(request, 'lab/live.html')

def play(request):
	return render(request, 'lab/play.html')

def design(request):
	return render(request, 'lab/design.html')

def makeit(request):
	return render(request, 'lab/makeit.html')

def friends(request):
	return render(request, 'lab/friends.html')

def reserve(request):
    """
    View for creating a reservation.
    """
    confirm = False

    # Get existing reservations.
    try:
        existing_reservations = ReservationDate.objects.all()
        print 'Got existing'
    except:
        print 'none existing'
        existing_reservations = []

    # Reservation has been submitted.
    if (request.method == 'POST') and (request.user.is_authenticated()):

        # Create new reservation.
        reservation = Reservation.objects.create(user=request.user)
        reservation.save();

        # Add dates to the reservation.
        for date in request.POST.getlist('date'):
            reservationDate = ReservationDate.objects.create(reservation=reservation, date=date)
            reservationDate.save()

        confirm = True

    return render(request, 'lab/reserve.html', {'reservations': existing_reservations, 'authenticated': request.user.is_authenticated(), 'confirm': confirm})

def reserve_existing(request):
    """
    View for seeing existing reservations.
    """
    try:
        reservations = Reservation.objects.filter(user=request.user)
    except:
        reservations = []

    print len(reservations)

    total = []
    for reservation in reservations:
        reservationDates = ReservationDate.objects.filter(reservation=reservation)
        total.append(reservationDates)

    print len(total)

    return render(request, 'lab/reserve_existing.html', {'reservations': total})

def account_register(request):
    """
    View for account registration.

    Shows the registration form. If the form is submitted and the form has an
    error, the view will continue showing the registration form, with a
    description of the error.

    If the form is submitted successfully, a new user is created.
    """

    # Create an empty registration form.
    form = RegistrationForm()

    # Form has been submitted.
    if request.method == 'POST':
        
        # Fill our form class with the registration details.
        form = RegistrationForm(request.POST)

        # Check if the form inputs are valid.
        if form.is_valid():

            # Create the user.
            user = User.objects.create_user(form.cleaned_data['email'], None, form.cleaned_data['password'], first_name=form.cleaned_data['first_name'], last_name=form.cleaned_data['last_name'])

            # Show a screen explaining the successful registration.
            return render(request, 'lab/account_register_success.html')

    # Form has not been submitted, or the form was submitted and had errors.
    return render(request, 'lab/account_register.html', {'form': form})


def account_sign_in(request):
    """
    View for signing into an account.

    Shows the sign-in form. Works similarly to the account registration form.
    """

    # Track whether an authentication attempt has failed.
    authentication_failed = False

    # Create an empty sign-in form.
    form = AuthenticationForm()

    # Form has been submitted.
    if request.method == 'POST':

        # Fill our form class with the sign-in details.
        form = AuthenticationForm(request.POST)

        # Check if form inputs are valid.
        if form.is_valid():

            # Try authenticating.
            user = authenticate(username=form.cleaned_data['email'], password=form.cleaned_data['password'])

            # Authenticated successfully. Go home.
            if user is not None:
                login(request, user)
                return redirect('index');

            # Authentication failed.
            authentication_failed = True
        
    return render(request, "lab/account_sign_in.html", {'form': form, 'failed': authentication_failed})

def account_sign_out(request):
    """
    View for signing out of an account.

    Signs the user out, and returns them to the home page.
    """
    logout(request)
    return redirect('index')
