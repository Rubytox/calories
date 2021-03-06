from datetime import datetime, timedelta, time

from django.utils import timezone

from django.shortcuts import render, redirect
from django.urls import reverse_lazy
from django.views import generic, View

from django.contrib.auth import login, authenticate
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.mixins import LoginRequiredMixin

from .forms import AddFoodManualForm, AddFoodFormManual
from .models import Food
from .utils import get_product_from_barcode

class DashboardView(LoginRequiredMixin, View):
    login_url = reverse_lazy('calories_app:home')

    template_name = 'calories_app/dashboard.html'

    def get(self, request):
        today = timezone.now().date()
        tomorrow = today + timedelta(1)
        today_start = datetime.combine(today, time())
        today_end = datetime.combine(tomorrow, time())

        food_today = Food.objects \
                    .filter(user_id=request.user.id) \
                    .filter(register_date__lte=today_end, register_date__gte=today_start) \
                    .order_by('register_date')

        total_today = sum(map(lambda f: f.quantity * f.energy / 100, food_today))

        return render(request, self.template_name, {
            'food_today': food_today,
            'total_today': total_today
        })

def index(request):
    if request.user.is_authenticated:
        return redirect('calories_app:dashboard')
    return render(request, 'calories_app/index.html')

def register(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data["username"]
            raw_password = form.cleaned_data["password1"]
            user = authenticate(username=username, password=raw_password)
            login(request, user)
            return redirect('calories_app:home')
    else:
        form = UserCreationForm()
    
    return render(request, 'registration/register.html', {'form': form})


class AddFoodView(LoginRequiredMixin, View):
    login_url = reverse_lazy('calories_app:home')

    def get(self, request):
        return render(request, 'calories_app/add_food.html', {
            'form': AddFoodManualForm()
        })

    def post(self, request):
        form = AddFoodManualForm(request.POST)
        if form.is_valid():
            barcode = form.cleaned_data["barcode"]
            product = get_product_from_barcode(barcode)
            if product is not None:
                nutr = product["product"]["nutriments"]
                name = form.cleaned_data["name"]
                
                food = Food(
                    name=name,
                    register_date=timezone.now(),
                    energy=nutr.get("energy-kcal", 0),
                    fat=nutr.get("fat", 0.0),
                    saturated_fat=nutr.get("saturated-fat", 0.0),
                    carbohydrates=nutr.get("carbohydrates", 0.0),
                    sugars=nutr.get("sugars", 0.0),
                    fibers=nutr.get("fiber", 0.0),
                    proteins=nutr.get("proteins", 0.0),
                    salt=nutr.get("sodium", 0.0),
                    quantity=form.cleaned_data["quantity"],
                    user=request.user
                )
                food.save()
                return redirect('calories_app:home')
            else:
                # Redirect to manual data insertion
                request.session['status'] = 'Could not find barcode, please enter data manually'
                return redirect('calories_app:add_food_manual')

class AddFoodManualView(LoginRequiredMixin, View):
    login_url = reverse_lazy('calories_app:home')

    def get(self, request):
        status = request.session.get("status")
        if status is not None:
            del request.session["status"]
        
        form = AddFoodFormManual()
        nutriments_table = filter(lambda f: f.name not in ['name', 'quantity'], list(form))

        return render(request, 'calories_app/add_food_manual.html', {
            'form': AddFoodFormManual(),
            'nutriments_table': list(nutriments_table),
            'status_message': status,
        })
    
    def post(self, request):
        form = AddFoodFormManual(request.POST)
        if form.is_valid():
            name = form.cleaned_data["name"]
            
            food = Food(
                name=name,
                register_date=timezone.now(),
                energy=form.cleaned_data["energy"],
                fat=form.cleaned_data["fat"],
                saturated_fat=form.cleaned_data["saturated_fat"],
                carbohydrates=form.cleaned_data["carbohydrates"],
                sugars=form.cleaned_data["sugars"],
                fibers=form.cleaned_data["fibers"],
                proteins=form.cleaned_data["proteins"],
                salt=form.cleaned_data["salt"],
                quantity=form.cleaned_data["quantity"],
                user=request.user
            )
            food.save()
            return redirect('calories_app:home')