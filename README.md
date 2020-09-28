# Python-Projects

Python modules and solutions. Most projects were completed in about 2 hours except two: The "Live-Project" was a two-week project to create a Python/Django dynamic and fully reactive investment portfolio traker website from scratch. The "Phonebook Demo" was a four-day project to create a tKinter contact list interface with database with export features.   

## CONTENTS
- [Django Project: Investment Portfolio Tracker](#django-project)  
  1. [Story 1: Base/Home](#story-1-base)
  2. [Story 2: Create](#story-2-create)
  3. [Story 3: Index Page](#story-3-index)
  4. [Story 4: Details Page](#story-4-details)
- [Webpage Generator](#webpage-generator)

## Django Project
During this two-week project I built a simple database driven fully functioning Django website with special attention placed on custom Boostrap styling and mobile friendly responsive webpages. This application was designed as a standalone website, but also resided in a larger web application with interactions to an existing codebase that had continuous contribution from 5 other programmers.     

### Description
The Investment Portfolio Tracker is a web application designed to keep track of your investment portfolio profit and loss. Users have CRUD functionality for stock/mutual/index and/or trade trackers. The interface provides cross-reference data for all trades related to stocks that are tracked. The stock and trade tracker index pages allow details access and easy updates.

### Backend
- [Views](#views)
- [Models](#models)
- [Forms](#forms)

### Stories
1. [Story 1: Base/Home](#story-1-base)
2. [Story 2: Create](#story-2-create)
3. [Story 3: Index Page](#story-3-index)
4. [Story 4: Details Page](#story-4-details)

### Views
```python
from django.http import HttpResponseRedirect
from django.shortcuts import render, redirect, get_object_or_404
from django.contrib import messages
from .models import Trade, Stock
from .forms import *

# ===== HOME
def investHome(request):
    return render(request, 'InvestmentApp/InvestmentApp_home.html')


# ========== PORTFOLIO
def investPortfolio(request):
    stocks = Stock.objects.all()
    trades = Trade.objects.all()
    return render(request, 'InvestmentApp/InvestmentApp_portfolio.html', {'stocks': stocks, 'trades': trades})


# ========== STOCK CREATE - Blank create form
def investCreate(request):
    stock_form = StockForm()
    trade_form = TradeForm()
    return render(request, 'InvestmentApp/InvestmentApp_create.html',
                  {'stock_form': stock_form, 'trade_form': trade_form})


# ========== STOCK CREATE - Stock Form
def stockCreate(request):
    # ===== STOCK FORM
    if request.method == 'POST':
        # ----- create a form instance and populate it with data from the request
        stock_form = StockForm(request.POST)
        # check whether it's valid
        if stock_form.is_valid():
            # process the data in form.cleaned_data as required
            stock_form.save()
            # create message for display - using extra_tag to direct message to a specific message element on html page
            messages.success(request, 'Stock Tracker Successfully Added', extra_tags='stock')
            # redirect to same URL with message - use ID reference at that end of the URL for positioning
            return redirect('/InvestmentApp/create/#stock-form')
        else:
            # create message for display - using extra_tag to direct message to a specific message element on html page - use ID reference at that end of the URL for positioning
            print(stock_form.errors)
            messages.warning(request, 'Please correct errors in stock form', extra_tags='stock')
            return redirect('/InvestmentApp/create/#stock-form')
    # ===== GET (or any other method) create a blank form
    else:
        stock_form = StockForm()
        trade_form = TradeForm()
    return render(request, 'InvestmentApp/InvestmentApp_create.html',
                  {'stock_form': stock_form, 'trade_form': trade_form})


# ========== TRADE CREATE - Trade Form
def tradeCreate(request):
    # ===== TRADE FORM
    if request.method == 'POST':
        # ----- create a form instance and populate it with data from the request
        trade_form = TradeForm(request.POST)
        # check whether it's valid
        if trade_form.is_valid():
            # process the data in form.cleaned_data as required
            trade_form.save()
            # create message for display - using extra_tag to direct message to a specific message element on html page
            messages.success(request, 'Trade Tracker Successfully Added', extra_tags='trade')
            # redirect to same URL with message - use ID reference at that end of the URL for positioning
            return redirect('/InvestmentApp/create/#trade-form')
        else:
            # create message for display - using extra_tag to direct message to a specific message element on html page - use ID reference at that end of the URL for positioning
            print(trade_form.errors)
            messages.warning(request, 'Please correct errors in trade form', extra_tags='trade')
            return redirect('/InvestmentApp/create/#trade-form')
    # ===== GET (or any other method) create a blank form
    else:
        stock_form = StockForm()
        trade_form = TradeForm()
    return render(request, 'InvestmentApp/InvestmentApp_create.html',
                  {'stock_form': stock_form, 'trade_form': trade_form})


# ========== STOCK DETAIL
def stockDetail(request, pk):
    pk = int(pk)
    # ===== Get the requested item from the model
    stock = Stock.objects.get(id=pk)
    # ===== Get all trades recorded to requested stock
    trades = stock.trade_set.all()
    trade_count = trades.count()
    # ===== Create form that is populated with requested item
    stock_instance = get_object_or_404(Stock, pk=pk)
    stock_form = StockForm(data=request.POST or None, instance=stock_instance)  # NOTE - the "or None" is required
    return render(request, 'InvestmentApp/InvestmentApp_stock.html',
                  {'stock': stock, 'trades': trades, 'stock_form': stock_form, 'trade_count': trade_count})


# ========== STOCK UPDATE
def stockUpdate(request, pk):
    pk = int(pk)
    # ===== Create form that is populated with requested item
    stock_instance = get_object_or_404(Stock, pk=pk)
    stock_form = StockForm(data=request.POST, instance=stock_instance)  # NOTE - the "or None" is required
    if stock_form.is_valid():
        stock_form.save()
        messages.success(request, 'Update Successful', extra_tags='stock')
    else:
        print(stock_form.errors)
        messages.warning(request, 'Update Failed', extra_tags='stock')
    return redirect('StockDetail', pk)


# ========== DELETE STOCK
def deleteStock(request, pk):
    pk = int(pk)
    instance = get_object_or_404(Stock, pk=pk)
    instance.delete()
    return redirect('InvestPortfolio')


# ========== TRADE DETAIL
def tradeDetail(request, pk):
    pk = int(pk)
    trade = Trade.objects.get(id=pk)  # Get the requested item from the model
    stock = trade.stock
    # ===== Create form that is populated with requested item
    trade_instance = get_object_or_404(Trade, pk=pk)
    trade_form = TradeForm(data=request.POST or None, instance=trade_instance)  # NOTE - the "or None" is required
    return render(request, 'InvestmentApp/InvestmentApp_trade.html', {'trade': trade, 'stock': stock, 'trade_form': trade_form})


# ========== TRADE UPDATE
def tradeUpdate(request, pk):
    pk = int(pk)
    # ===== Create form that is populated with requested item
    trade_instance = get_object_or_404(Trade, pk=pk)
    trade_form = TradeForm(data=request.POST, instance=trade_instance)  # NOTE - the "or None" is required
    if trade_form.is_valid():
        trade_form.save()
        messages.success(request, 'Update Successful', extra_tags='trade')
    else:
        print(trade_form.errors)
        messages.warning(request, 'Update Failed', extra_tags='trade')
    return redirect('TradeDetail', pk)


# ========== DELETE TRADE
def deleteTrade(request, pk):
    pk = int(pk)
    instance = get_object_or_404(Trade, pk=pk)
    instance.delete()
    return redirect('InvestPortfolio')
```

### Models
```python
from django.core.validators import MinValueValidator, URLValidator
from django.db import models
from datetime import datetime


# ========== STOCK

class Stock(models.Model):
    SS = 'S'
    MF = 'M'
    IF = 'I'
    ET = 'E'
    CATEGORY_CHOICES = [
        (SS, 'Stock'),
        (MF, 'Mutual Fund'),
        (IF, 'Index Fund'),
        (ET, 'ETF'),
    ]

    symbol = models.CharField("Symbol", max_length=5, null=False)
    name = models.CharField("Name", max_length=50, default="", null=False)
    category = models.CharField("Category", max_length=1, choices=CATEGORY_CHOICES, default=SS)
    link = models.CharField("Website", max_length=200, default="", blank=True, null=True, validators=[URLValidator])
    notes = models.TextField("Notes", max_length=300, default="", blank=True, null=True)
    cat_name = {
            'S': 'Stock',
            'M': 'Mutual Fund',
            'I': 'Index Fund',
            'E': 'ETF'
        }

    class Meta:
        ordering = ["name"]
        verbose_name_plural = "Stocks"

    def __str__(self):
        return self.name


# ========== TRADE
class Trade(models.Model):
    stock = models.ForeignKey(Stock, on_delete=models.CASCADE)
    open = models.DateField("Open Date", default=datetime.now)
    quantity = models.PositiveIntegerField("Quantity", default=1, validators=[MinValueValidator(1)])
    open_cost = models.DecimalField("Open/Share", max_digits=7, decimal_places=2, default=0,
                                    validators=[MinValueValidator(0.01)])
    close = models.DateField("Close Date", null=True, blank=True)
    close_cost = models.DecimalField("Close/Share", max_digits=7, decimal_places=2, null=True, blank=True,
                                     validators=[MinValueValidator(0.00)])
    paper = models.BooleanField("Paper Trade", default=False)

    @property
    def total_open(self):
        return "${:,}".format(self.quantity * self.open_cost)

    @property
    def total_close(self):
        if self.close and self.close_cost is not None:
            return "${:,}".format(self.quantity * self.close_cost)
        else:
            return 'Still Open'

    @property
    def gain(self):
        if self.close and self.close_cost is not None:
            return "${:,}".format((self.quantity * self.close_cost) - (self.quantity * self.open_cost))
        else:
            return 'Still Open'

    @property
    def percent_gain(self):
        if self.close and self.close_cost is not None:
            calc = ((self.quantity * self.close_cost) - (self.quantity * self.open_cost)) / (self.quantity * self.open_cost)
            return "{:.2%}".format(calc)
        else:
            return 'Still Open'

    @property
    def win(self):
        if self.close and self.close_cost is not None:
            if ((self.quantity * self.close_cost) - (self.quantity * self.open_cost)) >= 0:
                return True
            else:
                return False
        else:
            return None

    objects = models.Manager()

    class Meta:
        ordering = ["open"]
        verbose_name_plural = "Trades"

    def __str__(self):
        if self.paper:
            return "{} Paper Trade".format(self.stock.symbol)
        else:
            return "{} Trade".format(self.stock.symbol)
```

### Forms
```python
from datetime import datetime
from django.forms import ModelForm
from django.forms.widgets import *
from .models import Stock, Trade


# ========== STOCK
class StockForm(ModelForm):
    class Meta:
        model = Stock
        fields = '__all__'
        widgets = {
            'symbol': TextInput(attrs={'class': 'form-control'}),
            'name': TextInput(attrs={'class': 'form-control'}),
            'category': Select(attrs={'class': 'form-control'}),
            'link': TextInput(attrs={'placeholder': 'optional', 'class': 'form-control', 'type': 'url'}),
            'notes': TextInput(attrs={'placeholder': 'optional', 'class': 'form-control'})
        }


# ========== TRADE
class TradeForm(ModelForm):
    class Meta:
        model = Trade
        fields = '__all__'
        widgets = {
            'stock': Select(attrs={'class': 'form-control'}),
            'open': DateInput(attrs={'class': 'form-control', 'type': 'date'}),
            'quantity': NumberInput(attrs={'class': 'form-control'}),
            'open_cost': NumberInput(attrs={'class': 'form-control'}),
            'close': DateInput(attrs={'placeholder': 'optional', 'class': 'form-control', 'type': 'date'}),
            'close_cost': NumberInput(attrs={'class': 'form-control'}),
            'paper': CheckboxInput(attrs={'class': 'form-check-input'}),
        }

    # Logic for raising error if close_date < open_date
    def clean(self):
        cleaned_data = super().clean()
        open_date = cleaned_data.get('open')
        close_date = cleaned_data.get('close')
        close_cost = cleaned_data.get('close_cost')
        try:
            if close_date is not None:
                if close_date < open_date:
                    msg = 'Close date should be greater than open date.'
                    self._errors['close'] = self.error_class([msg])
                if close_cost is None:
                    msg = 'Must have a closing cost to close the trade.'
                    self._errors['close_cost'] = self.error_class([msg])
        except ValueError:
            print('Invalid Close date format')
```

## Story 1: Base

### Commit
- Version control with team on larger app
-	Create new app via startapp
-	Register app from within MainProject
-	Create base and home templates in a new template folder
-	Add function to views to render the home page
-	Register urls with MainApp and create urls.py for app and homepage
-	Link app home page to the main home page by adding an image on the main home page.
-	Customize Navigation bar and footer
-	Add logo to tab and navigation bar
-	Add homepage content: title, subtitle, description, image, with basic styling.
-	Add responsive styling to Home page and base templates.

### Interface
![alt text](https://github.com/alex-moffat/Python-Projects/blob/master/Live-Project-Python/Screenshot_home_full.jpg "Home_Page_Full")
![alt text](https://github.com/alex-moffat/Python-Projects/blob/master/Live-Project-Python/Screenshot_home_iphone.jpg "Home_Page_Mobile")

### Base
```HTML
{% load staticfiles %}

<!DOCTYPE html>

<html lang="en">
    <!--========================================
                HEAD
    =========================================-->
    <head>
        <!-- META TAGS -->
        <meta charset="utf-8">
        <meta name="viewport" content="width=device-width, initial-scale=1">
        <meta name="description" content="InvestmentApp is designed to keep track of your investment portfolio as well as get recent news and research for stocks and mutual funds.">
        <meta name="keywords" content="HTML, CSS, JavaScript, XML, Bootstrap, SQL, Python, Django, Alex Moffat">
        <meta name="author" content="Alex Moffat">
        <!-- TITLE & TAB -->
        <title>{% block title %}Python Live Project{% endblock %}</title>
        <link rel="icon" href="{% block tab-icon %}{% static 'InvestmentApp/img/logo/bull_icon_light.ico' %}{% endblock %}">
        <!-- Fonts -->
        <link href='https://fonts.googleapis.com/css?family=Public Sans:200,400,600,800' rel='stylesheet'/>
        <!-- External css -->
        <link rel="stylesheet" href="https://stackpath.bootstrapcdn.com/bootstrap/4.3.1/css/bootstrap.min.css" integrity="sha384-ggOyR0iXCbMQv3Xipma34MD+dH/1fQ784/j6cY/iJTQUOhcWr7x9JvoRxT2MZw1T" crossorigin="anonymous">
        <!-- Internal stylesheet -->
        <link rel="stylesheet" type="text/css" href="{% static 'InvestmentApp/css/InvestmentApp.css' %}" />
    </head>
    <!--========================================
                BODY
    =========================================-->
    <body>
        <!--========== NAV ==========-->
        <nav class="sticky-top navbar navbar-expand-lg navbar-dark bg-dark">
            <a class="navbar-brand" href="{% url 'InvestHome' %}">
                <img src="{% block app-icon %}{% static 'InvestmentApp/img/logo/bull_icon_light.ico' %}{% endblock %}" width="30" height="30" class="d-inline-block align-top" alt="InvestmentApp-Logo" loading="lazy">
                InvestmentApp
            </a>
            <button class="navbar-toggler" type="button" data-toggle="collapse" data-target="#navbarNavAltMarkup" aria-controls="navbarNavAltMarkup" aria-expanded="false" aria-label="Toggle navigation">
                <span class="navbar-toggler-icon"></span>
            </button>
            <div class="collapse navbar-collapse" id="navbarNavAltMarkup">
                <div class="navbar-nav">
                    <a class="nav-link {% block active1 %}{% endblock %}" href="{% url 'InvestHome' %}">Home</a>
                    <a class="nav-link {% block active2 %}{% endblock %}" href="{% url 'InvestPortfolio' %}">Portfolio</a>
                    <a class="nav-link {% block active3 %}{% endblock %}" href="{% url 'InvestCreate' %}">Tracker</a>
                    <a class="nav-link {% block active4 %}{% endblock %}" href="#">Research</a>
                    <a class="nav-link {% block active5 %}{% endblock %}" href="#">News</a>
                    <a class="nav-link" href="{% url 'home' %}">AppBuilder</a>
                </div>
            </div>
        </nav>

        <!--========== HEADER ==========-->
        <header>
            {% block header %}
            <div class="header-container">
                <img class="{% block header-img-css %}{% endblock %}" src="{% block header-img %}{% endblock %}" alt="header-img">
                <div class="container">
                    <div class="header-banner jumbotron text-center text-white">
                        <h1 class="display-4">{% block page-title %}{% endblock %}</h1>
                        <p class="lead font-weight-bold">{% block page-subtitle %}{% endblock %}</p>
                        {% block header-line %}<hr class="my-4 bg-white">{% endblock %}
                        <p>{% block page-description %}{% endblock %}</p>
                        <p class="lead">
                            {% block header-button1 %}{% endblock %}
                            {% block header-button2 %}{% endblock %}
                            {% block header-button3 %}{% endblock %}
                            {% block header-button4 %}{% endblock %}
                            {% block header-button5 %}{% endblock %}
                        </p>
                    </div>
                </div>
            </div>
            {% endblock %}
        </header>

        <!--========== MAIN ==========-->
        <main class="pb-5">
            {% block main %}{% endblock %}
        </main>

        <!--========== FOOTER ==========-->
        <footer class="bg-secondary my-0 py-3 text-center">
            <div class="container">
                <span class="text-white"><a class="text-white" href="https://a-moffat.com/">Alex Moffat</a> &nbsp; | &nbsp; &copy; {% now 'Y' %}</span>
            </div>
        </footer>

        <!--========== SCRIPT - jQuery first, then Popper.js, then Bootstrap JS ==========-->
        {% block javascript %}
        <script src="https://code.jquery.com/jquery-3.3.1.slim.min.js" integrity="sha384-q8i/X+965DzO0rT7abK41JStQIAqVgRVzpbzo5smXKp4YfRvH+8abtTE1Pi6jizo" crossorigin="anonymous"></script>
        <script src="https://cdnjs.cloudflare.com/ajax/libs/popper.js/1.14.3/umd/popper.min.js" integrity="sha384-ZMP7rVo3mIykV+2+9J3UJ46jBk0WLaUAdn689aCwoqbBJiSnjAK/l8WvCWPIPm49" crossorigin="anonymous"></script>
        <script src="https://stackpath.bootstrapcdn.com/bootstrap/4.1.3/js/bootstrap.min.js" integrity="sha384-ChfqqxuZUCnJSK3+MXmPNIyE6ZbWh2IMqE241rYiqJxyMiZ6OW/JmZQ5stwEULTy" crossorigin="anonymous"></script>
        <!-- Used for tooltip style -->
        <script type="text/javascript">
        $(document).ready(function() {
            $("body").tooltip({ selector: '[data-toggle=tooltip]', delay: {show: 1000, hide: 200}});
        });
        </script>
        {% endblock %}
    </body>
</html>
```

### Home
```HTML
{% extends 'InvestmentApp/InvestmentApp_base.html' %}
{% load staticfiles %}

<!--========== HEAD ==========-->
{% block title %}InvestmentApp{% endblock %}

<!--========== HEADER ==========-->
{% block header-img-css %}header-home{% endblock %}
{% block header-img %}{% static 'InvestmentApp/img/wallstreet_bull_1920.jpg' %}{% endblock %}
{% block page-title %}Stock Portfolio Tracker{% endblock %}
{% block page-subtitle %}Research &nbsp; | &nbsp; Invest &nbsp; | &nbsp; Grow{% endblock %}
{% block page-description %}Keep track of your investment portfolio as well as get recent news and research for stocks and mutual funds.{% endblock %}
<!-- Buttons -->
{% block header-button1 %}<a class="mt-3 mx-2 btn btn-outline-light btn-lg" data-toggle="tooltip" data-placement="bottom" title="View an index of all tracked stocks" href="{% url 'InvestPortfolio' %}" role="button">Portfolio</a>{% endblock %}
{% block header-button2 %}<a class="mt-3 mx-2 btn btn-outline-light btn-lg" data-toggle="tooltip" data-placement="bottom" title="Add a stock or trade to track" href="{% url 'InvestCreate' %}" role="button">Add Tracker</a>{% endblock %}
{% block header-button3 %}<a class="mt-3 mx-2 btn btn-outline-light btn-lg" data-toggle="tooltip" data-placement="bottom" title="View research for stocks you are tracking" href="#" role="button">Research</a>{% endblock %}
{% block header-button4 %}<a class="mt-3 mx-2 btn btn-outline-light btn-lg" data-toggle="tooltip" data-placement="bottom" title="The latest news stories for the entire market" href="#" role="button">News</a>{% endblock %}
{% block header-button5 %}{% endblock %}

<!--========== NAVBAR active page ==========-->
{% block active1 %}active{% endblock %}
{% block active2 %}{% endblock %}
{% block active3 %}{% endblock %}
{% block active4 %}{% endblock %}
{% block active5 %}{% endblock %}

<!--========== MAIN CONTENT ==========-->
{% block main %}{% endblock %}
```

## Story 2: Create

### Commit
- Create two linked models and add a migration
-	Create a model form that will include any inputs the user needs to make
-	Add a template app folder for creating a new item in either model.
-	Add a views function that renders the create page and utilizes the model form to save the collection item to the database.
-	Validation added to models.
-	Add responsive styling to form and templates to use Bootstrap.
-	Add message routing to specific form on template.

### Interface
![alt text](https://github.com/alex-moffat/Python-Projects/blob/master/Live-Project-Python/Screenshot_create_full.jpg "Create_Full")

### Create
```HTML
<!--========== MAIN CONTENT ==========-->
{% block main %}
<!-- Bootstrap card deck - includes stock and trade forms as cards -->
<div class="container my-5">
    <div class="card-deck">
        <!--===== STOCK FORM =====-->
        <div id="stock-form" class="card shadow">
            <img src="{% static 'InvestmentApp/img/stock-picks_800_wide.jpg' %}" class="card-img-top" alt="stock-pick">
            <!--===== CARD BODY =====-->
            <div class="card-body">
                <h4 class="card-title text-center font-weight-bold">Stock Tracker</h4>
                <p class="card-text">
                    <form name="stockForm" method="POST" action="{% url 'StockCreate' %}">
                        <!-- Cross Site Request Forgery (csrf_token) protection -->
                        {% csrf_token %}
                        <!-- Render each field  -->
                        {% for field in stock_form %}
                        <div class="form-group {%if field.errors %}is-invalid{%endif%}">
                            {{ field.label_tag }}
                            {{ field }}
                            <!-- FIELD ERROR message -->
                            <small class="form-text text-danger">{{ field.errors }}</small>
                        </div>
                        {% endfor %}
                        <div class="pt-3 px-5">
                            <button name="stockForm" type="submit" class="btn btn-secondary btn-block shadow">Save Stock/Index</button>
                        </div>
                    </form>
                </p>
            </div>
            <!--===== CARD FOOTER - MESSAGE - Success/Error =====-->
            {% if messages %}
                <!-- check if message is for the STOCK form -->
                {% for message in messages %}
                    {% if 'stock' in message.tags %}
                        <div class="card-footer text-center alert-{{ message.level_tag }}">
                            <small>{{ message }}</small>
                        </div>
                    {% endif %}
                {% endfor %}
            {% endif %}
        </div>

        <!--===== TRADE FORM =====-->
        <div id="trade-form" class="card shadow">
            <img src="{% static 'InvestmentApp/img/stock-trade_800_wide.jpg' %}" class="card-img-top" alt="stock-trade">
            <!-- CARD BODY Title and form in main body -->
            <div class="card-body">
                <h4 class="card-title text-center font-weight-bold">Trade Tracker</h4>
                <p class="card-text">
                    <form name="tradeForm" method="POST" action="{% url 'TradeCreate' %}">
                        <!-- Cross Site Request Forgery (csrf_token) protection -->
                        {% csrf_token %}
                        <!-- Render each field  -->
                        {% for field in trade_form %}
                        <div class="form-group {%if field.errors %}is-invalid{%endif%}">
                            <!-- CHECKBOX in Bootstrap -->
                            {% if 'paper' in field.label|lower %}
                                <div class="form-check">
                                    {{ field }}
                                    <label class="form-check-label">Paper Trade</label>
                                </div>
                            <!-- TEXT BOX FIELD in Bootstrap -->
                            {% else %}
                                {{ field.label_tag }}
                                {{ field }}
                            {% endif %}
                            <!-- FIELD ERROR message -->
                            {% for error in field.errors %}
                                <small class="form-text text-danger">{{ error }}</small>
                            {% endfor %}
                        </div>
                        {% endfor %}
                        <div class="pt-2 px-5">
                            <button name="tradeForm" type="submit" class="btn btn-secondary btn-block shadow">Save Trade</button>
                        </div>
                    </form>
                </p>
            </div>
            <!-- CARD FOOTER - MESSAGE - Success/Error -->
            {% if messages %}
                <!-- check if message is for the TRADE form -->
                {% for message in messages %}
                    {% if 'trade' in message.tags %}
                        <div class="card-footer text-center alert-{{ message.level_tag }}">
                            <small>{{ message }}</small>
                        </div>
                    {% endif %}
                {% endfor %}
            {% endif %}
        </div>
    </div>
</div>
{% endblock %}
```

## Story 3: Index

### Commit
-	Create index page that is linked from home page
-	Add a function that gets all the items from the database and sends them to the template
-	Display a list of items in the database with the fields for that item displayed with labels/headers
-	Link app's home page to the main home page.
-	Add responsive styling to index template.
-	Add link to create new item in either database table
-	Dynamically add anchor tags to fields that are html references

### Interface
![alt text](https://github.com/alex-moffat/Python-Projects/blob/master/Live-Project-Python/Screenshot_index_full_1.jpg "Index_1")
![alt text](https://github.com/alex-moffat/Python-Projects/blob/master/Live-Project-Python/Screenshot_index_full_2.jpg "Index_2")

### Index
```HTML
<!--========== MAIN CONTENT ==========-->
{% block main %}

    <!--===== STOCK TABLE =====-->
    <div class="container mt-5">
        <div id="stock-table" class="card shadow">
            <div class="card-header text-center">
                <h4 class="font-weight-bold">Stock Watchlist</h4>
            </div>
            <div class="card-body">
                <div class="card-text mb-4">
                    <div class="table-responsive">
                        <table class="table table-hover">
                            <thead class="thead-dark">
                                <tr>
                                    <th scope="col">Symbol</th>
                                    <th scope="col">Name</th>
                                    <th scope="col">Category</th>
                                    <th scope="col">Website</th>
                                </tr>
                            </thead>
                            <tbody>
                                {% for object in stocks %}
                                    <tr>
                                        <th class="click-cell" scope="row"><a href="{% url 'StockDetail' pk=object.id %}">{{ object.symbol }}</a></th>
                                        <td class="click-cell"><a href="{% url 'StockDetail' pk=object.id %}">{{ object.name }}</a></td>
                                        <td class="click-cell"><a href="{% url 'StockDetail' pk=object.id %}">{{ object.get_category_display }}</a></td>
                                        <!--===== ANCHOR - create anchor tag only if website link =====-->
                                        {% if object.link is not None %}
                                            <td><a target="_blank" href="{{ object.link }}"><small>{{ object.link }}</small></a></td>
                                        {% else %}
                                            <td class="click-cell"><a href="{% url 'StockDetail' pk=object.id %}"></a>{{ object.link }}</td>
                                        {% endif %}
                                    </tr>
                                {% endfor %}
                            </tbody>
                        </table>
                    </div>
                </div>
                <!--===== BUTTON - link to create new tracker=====-->
                <a name="stockCreate" href="{% url 'InvestCreate' %}" class="btn btn-secondary shadow">Add New Stock Tracker</a>
            </div>
        </div>
    </div>

    <!--===== TRADE TABLE =====-->
    <div class="container my-5">
        <div id="trade-table" class="card shadow">
            <div class="card-header text-center">
                <h4 class="font-weight-bold">Trade List</h4>
            </div>
            <div class="card-body">
                <div class="card-text mb-4">
                    <div class="table-responsive">
                        <table class="table table-hover">
                            <thead class="thead-dark">
                                <tr>
                                    <th scope="col">Stock</th>
                                    <th scope="col">Quantity</th>
                                    <th scope="col">Open</th>
                                    <th scope="col">Open Cost</th>
                                    <th scope="col">Close</th>
                                    <th scope="col">Close Cost</th>
                                </tr>
                            </thead>
                            <tbody>
                                {% for trade in trades %}
                                    <tr>
                                        <th class="click-cell" scope="row"><a href="{% url 'TradeDetail' pk=trade.id %}">{{ trade.stock }}</a></th>
                                        <td class="click-cell"><a href="{% url 'TradeDetail' pk=trade.id %}">{{ trade.quantity }}</a></td>
                                        <td class="click-cell"><a href="{% url 'TradeDetail' pk=trade.id %}">{{ trade.open }}</a></td>
                                        <td class="click-cell"><a href="{% url 'TradeDetail' pk=trade.id %}">{{ trade.open_cost }}</a></td>
                                        <td class="click-cell"><a href="{% url 'TradeDetail' pk=trade.id %}">{{ trade.close }}</a></td>
                                        <td class="click-cell"><a href="{% url 'TradeDetail' pk=trade.id %}">{{ trade.close_cost }}</a></td>
                                    </tr>
                                {% endfor %}
                            </tbody>
                        </table>
                    </div>
                </div>
                <!--===== BUTTON - link to create new tracker=====-->
                <a name="tradeCreate" href="{% url 'InvestCreate' %}" class="btn btn-secondary shadow">Add New Trade Tracker</a>
            </div>
        </div>
    </div>

{% endblock %}
```

## Story 4: Details

### Commit
-	Add two details templates to the template folder, register the url pattern 
-	Create a views function that finds a single desired instance from the database and all related instances from the foreign key.
-	Send details for two tables to a single details template
-	Add in links for each element on the index page that will direct to the details page for that item
-	Add links for each element in the details page that directs to another details page
-	Display all the details of the item on the details page and all related objects from another table
-	Add responsive and dynamic styling based on data in details templates.
-	Add anchor selection and hover styling to entire row of a table 
-	Add calculated properties to model

### Interface
![alt text](https://github.com/alex-moffat/Python-Projects/blob/master/Live-Project-Python/screenshots_details.jpg "Details_Pages")

### Stock Details
```HTML
<!--========== MAIN CONTENT ==========-->
{% block main %}
<!--===== STOCK DETAIL =====-->
<div class="container my-5">
    <div class="card shadow">

        <!--===== CARD HEADER =====-->
        <div class="card-header">
            <h4 class="font-weight-bold py-1">{{ stock.symbol }}</h4>
            <!--=== NAV TABS ===-->
            <ul class="nav nav-tabs card-header-tabs" id="myTab" role="tablist">
                <!--=== DETAILS ===-->
                <li class="nav-item">
                    <a class="nav-link active" id="home-tab" data-toggle="tab" href="#home" role="tab" aria-controls="home" aria-selected="true">Details</a>
                </li>
                <!--=== TRADES - disabled if no trades ===-->
                <li class="nav-item">
                    <a class="nav-link {% if not trades %}disabled{% endif %}" id="trades-tab" data-toggle="tab" href="#trades" role="tab" aria-controls="trades" aria-selected="false">Trades</a>
                </li>
                <!--=== EDIT ===-->
                <li class="nav-item">
                    <a class="nav-link" id="edit-tab" data-toggle="tab" href="#edit" role="tab" aria-controls="edit" aria-selected="false">Edit</a>
                </li>
            </ul>
        </div>

        <!--===== CARD BODY / TAB CONTENT =====-->
        <div class="card-body tab-content" id="myTabContent">

            <!--===== STOCK INFO =====-->
            <div class="tab-pane fade show active" id="home" role="tabpanel" aria-labelledby="home-tab">
                <h5 class="card-title mt-2 mb-4">{{ stock.name }}</h5>
                <div class="card-text">
                    <p>
                        <span class="font-weight-bold">Category:</span><br>
                        {{ stock.get_category_display }}
                    </p>
                    <p>
                        <span class="font-weight-bold">Website:</span><br>
                        <!--=== ANCHOR - create anchor tag only if website link =====-->
                        {% if stock.link is not None %}
                            <a target="_blank" href="{{ object.link }}">{{ stock.link }}</a>
                        {% else %}
                            <span>{{ stock.link }}</span>
                        {% endif %}
                    </p>
                    <p>
                        <span class="font-weight-bold">Notes:</span><br>
                        <span>{{ stock.notes }}</span>
                    </p>
                </div>
                <hr class="my-4 bg-dark">
                <!--===== BUTTON - link to create new tracker =====-->
                <a name="tradeCreate" href="{% url 'InvestCreate' %}" class="btn btn-secondary shadow">Add A Trade Tracker</a>
            </div>

            <!--===== TRADE TABLE - display only if there are trades =====-->
            <div class="tab-pane fade" id="trades" role="tabpanel" aria-labelledby="trades-tab">
                <h5 class="card-title mt-2">{{ stock.symbol }} Trades</h5>
                <h6 class="card-subtitle mb-4 text-muted">Total trackers: {{ trade_count }}</h6>
                <div class="card-text mb-4">
                    <div class="table-responsive">
                        <table class="table table-hover">
                            <thead class="thead-dark">
                                <tr>
                                    <th scope="col">Stock</th>
                                    <th scope="col">Quantity</th>
                                    <th scope="col">Open</th>
                                    <th scope="col">Open Cost</th>
                                    <th scope="col">Close</th>
                                    <th scope="col">Close Cost</th>
                                </tr>
                            </thead>
                            <tbody>
                                {% for object in trades %}
                                    <a href="{% url 'TradeDetail' pk=object.id %}">
                                        <tr>
                                            <th class="click-cell" scope="row"><a href="{% url 'TradeDetail' pk=object.id %}">{{ object.stock }}</a></th>
                                            <td class="click-cell"><a href="{% url 'TradeDetail' pk=object.id %}">{{ object.quantity }}</a></td>
                                            <td class="click-cell"><a href="{% url 'TradeDetail' pk=object.id %}">{{ object.open }}</a></td>
                                            <td class="click-cell"><a href="{% url 'TradeDetail' pk=object.id %}">{{ object.open_cost }}</a></td>
                                            <td class="click-cell"><a href="{% url 'TradeDetail' pk=object.id %}">{{ object.close }}</a></td>
                                            <td class="click-cell"><a href="{% url 'TradeDetail' pk=object.id %}">{{ object.close_cost }}</a></td>
                                        </tr>
                                    </a>
                                {% endfor %}
                            </tbody>
                        </table>
                    </div>
                </div>
                <!--===== BUTTON - link to create new tracker =====-->
                <a name="tradeCreate" href="{% url 'InvestCreate' %}" class="btn btn-secondary shadow">Add A Trade Tracker</a>
            </div>

            <!--===== EDIT FORM =====-->
            <div class="tab-pane fade" id="edit" role="tabpanel" aria-labelledby="edit-tab">
                <h5 class="card-title mt-2 mb-4">{{ stock.symbol }} Edit Details</h5>
                <div class="card-text mb-4">
                    <form name="stockForm" method="POST" action="{% url 'StockUpdate' pk=stock.id %}">
                        <!-- Cross Site Request Forgery (csrf_token) protection -->
                        {% csrf_token %}
                        <!-- Render each field  -->
                        {% for field in stock_form %}
                        <div class="fieldWrapper form-group" aria-required="{% if field.field.required %}true{% else %}false{% endif %}">
                            {{ field.label_tag }}
                            {{ field }}
                            <!-- FIELD ERROR message -->
                            {%if field.errors %}
                                {% for error in field.errors %}
                                    <small class="form-text text-danger">{{ error }}</small>
                                {% endfor %}
                            {% endif %}
                        </div>
                        {% endfor %}
                        <!--===== BUTTONS =====-->
                        <div class="mt-5">
                            <a name="stockDetail" href="{% url 'StockDetail' pk=stock.id %}" class="btn btn-secondary shadow">Cancel</a>
                            <button name="stockForm" type="submit" class="btn btn-success shadow">Save Changes</button>
                            <button type="button" name="deleteConfirm" class="btn btn-danger shadow mx-2" data-toggle="modal" data-target="#deleteConfirm">Delete</button>
                        </div>
                    </form>
                    <!--===== DELETE CONFIRM MODAL =====-->
                    <div class="modal fade" id="deleteConfirm" tabindex="-1" role="dialog" aria-labelledby="deleteConfirmTitle" aria-hidden="true">
                        <div class="modal-dialog modal-dialog-centered" role="document">
                            <!--=== MODAL CONTENT ===-->
                            <div class="modal-content">
                                <!-- HEADER -->
                                <div class="modal-header text-danger">
                                    <h5 class="modal-title" id="modalLongTitle">Confirm Delete</h5>
                                    <button type="button" class="close" data-dismiss="modal" aria-label="Close">
                                      <span aria-hidden="true">&times;</span>
                                    </button>
                                </div>
                                <!-- BODY -->
                                <div class="modal-body">
                                    <p>Please be sure you want to delete this stock tracker. <b>This action can not be undone.</b></p>
                                    <p>When you delete a stock you are tracking you will also delete all trades that are associated.</p>
                                    <p>You currently have <b>{{ trade_count }}</b> trades associated with this stock.</p>
                                </div>
                                <!-- FOOTER -->
                                <div class="modal-footer">
                                    <button type="button" class="btn btn-secondary" data-dismiss="modal">Cancel</button>
                                    <a name="delete" href="{% url 'DeleteStock' pk=stock.id %}" class="btn btn-danger">Delete Data</a>
                                </div>
                            </div>
                        </div>
                    </div>
                </div>
            </div>
        </div>

        <!--===== CARD FOOTER - MESSAGE - Success/Error =====-->
        {% if messages %}
            <!-- check if message is for the STOCK form -->
            {% for message in messages %}
                {% if 'stock' in message.tags %}
                    <div class="card-footer text-center alert-{{ message.level_tag }}">
                        <small>{{ message }}</small>
                    </div>
                {% endif %}
            {% endfor %}
        {% endif %}
    </div>
</div>
{% endblock %}
```


## Webpage Generator

### Commit
- Create a tool that can automatically create a basic HTML web page.
- The page is very simple: Have a title and body text on page.
- Use a Python script that will automatically create the .html file needed.
- Create a GUI with Tkinter that enables users to set title and body text for web page.

### Interface
![alt text](https://github.com/alex-moffat/Python-Projects/blob/master/Webpage%20Generator/Screenshot_webpage_generator.jpg "Webpage_Generator")

### Code
```python
# PYTHON: 3.8.2
# AUTHOR: Alex Moffat
# PURPOSE: The Tech Academy Bootcamp - WEBPAGE GENERATOR
#=============================================================================
description = """
This program was written by Alex Moffat.\n
This is a demonstration of programming based on requirements given from The Tech Academy Python Course. \n
"""
requirements="""
Create a tool that can automatically create a basic HTML web page.
The page is very simple. It will simply have the text "Stay tuned for our amazing summer sale!" on the page.
Use a Python script that will automatically create the .html file needed.
Create a GUI with Tkinter that enables users to set body text for web page.
"""
contact = """
Alex Moffat\n
wamoffat4@gmail.com\n
(917) 674-4820"""

#===== TAGS
"""
 datetime, now, deltatime, total_seconds, open, write, close, tkinter, Text, Button, grid,
 delete, insert, isinstance, destroy, lambda, title, iconbitmap, Tk(), row, column, resizeable,
 config, padx, pady, sticky,columnspan
"""
#=============================================================================

#===== IMPORTED MODULES
import os
from tkinter import *
from datetime import *

#===== VARIABLES
tStart = datetime.now() # script timing
tInc = datetime.now() # script increment timing
webPage = ''
title = "Automated webpage" # webpage title
body = 'Stay tuned for our amazing summer sale!' # webpage body text  

#========== SCRIPT TIMING - gets elapsed time of script execution, reset increment time
def sTime(name):
    global tInc
    if name != None:
        iTime = round(timedelta.total_seconds(datetime.now() - tInc) * 1000)
        tTime = round(timedelta.total_seconds(datetime.now() - tStart) * 1000)
        print("SCRIPT {} completed in {} ms and total time from start is {} ms\n".format(name, iTime , tTime))
    tInc = datetime.now() 

#========== RESET TEXT - set text in text fields to default
def resetText(obj, txt):
    obj.delete("1.0", END)
    obj.insert('1.0', txt)

#=============================================================
#========== TKINTER GUI - CREATE tkinter window with grid
#=============================================================
def createGUI():
    #===== WINDOW =====
    win = Tk()
    #=== title & icon
    win.title('Insert Webpage Content')
    win.iconbitmap('favicon.ico')
    #=== size & position center
    win.resizable(width=False, height=False)
    #===== TEXT =====
    t1 = Text(win, width=50, height=1, wrap=NONE)
    t2 = Text(win, width=50, height=4, wrap=WORD)
    #=== size & position
    t1.grid(row=0, column=1, columnspan=3, padx=(10,20), pady=(40,10), sticky=N+S+W+E)
    t2.grid(row=1, column=1, columnspan=3, padx=(10,20), pady=(0,10), sticky=N+S+W+E)
    #===== BUTTONS =====
    b1 = Button(win, text = "Default Title")
    b2 = Button(win, text = "Default Body")
    b3 = Button(win, text = "Create Webpage")
    b4 = Button(win, text = "Close Program")
    #=== configure
    b1.configure(command=lambda obj=t1, txt=title: resetText(obj, txt))
    b2.configure(command=lambda obj=t2, txt=body: resetText(obj, txt))
    b3.configure(height=2, command=lambda newTitle=t1, newBody=t2: insertContent(newTitle, newBody))
    b4.configure(height=2, command=lambda : win.destroy())
    #=== size & position
    b1.grid(row=0, column=0, padx=(20,10), pady=(40,10), sticky=W+E)
    b2.grid(row=1, column=0, padx=(20,10), pady=(0,10), sticky=W+E)
    b3.grid(row=2, column=0, padx=(20,10), pady=(0,20))
    b4.grid(row=2, column=3, padx=(10,20), pady=(0,20), sticky=E)
    sTime('createGUI') # script timer
    

#=============================================================
#========== WEBPAGE
#=============================================================

#========== CREATE PAGE - create framework with indexed insert wildcards
def createPage():
    global webpage
    webpage = """
        <!DOCTYPE html>
        <html lang='en'>
            <head>
                <title>{0}</title>
                    <meta charset='utf-8'>
            </head>
            <body>
                {1}
            </body>
        </html>    
        """
    print("Webpage framework created:|n",webpage)
    sTime('createPage')

#========== INSERT PAGE CONTENT - insert contents into webpage framework
def insertContent(newTitle, newBody):
    sTime(None)
    global webpage
    if isinstance(newTitle,str) and isinstance(newBody,str): #string format
        newPage = webpage.format(newTitle, newBody)
    else: # text widget object
        newPage = webpage.format(newTitle.get("1.0",END).strip(), newBody.get("1.0",END).strip())
    print(newPage)   
    sTime('insertContent')
    writePage(newPage)    
    
#========== WRITE PAGE 
def writePage(newPage):
    file = open('webpage.html','w') # a = append what exists, w = overwrite
    file.write(newPage)
    file.close()
    print("Webpage created in this path:\n{}".format(os.getcwd()))
    sTime('writePage')
    


#=============================================================
#========== MAIN
#=============================================================        
if __name__ == '__main__':
    createGUI()
    createPage()
```

