# Python-Projects
Python modules and solutions. Most projects were completed in about 2 hours except two: The "Live-Project" was a two-week project to create a Python/Django dynamic and fully reactive investment portfolio traker website from scratch. The "Phonebook Demo" was a four-day project to create a tKinter contact list interface with database with export features.   

### Video Hightlight: Django Project
<a href="http://www.youtube.com/watch?feature=player_embedded&v=3Dia9XkRW04" target="_blank"><img src="https://github.com/alex-moffat/Python-Projects/blob/master/Live-Project-Python/Screenshot_home_full.jpg" alt="Django_Project_Demo" border="10" /></a>

### Video Hightlight: Tkinter Phonebook Demo
<a href="http://www.youtube.com/watch?feature=player_embedded&v=d3SrnxGAbEs" target="_blank"><img src="https://github.com/alex-moffat/Python-Projects/blob/master/Tkinter%20Phonebook/Screenshot_Phonebook.jpg" alt="Tkinter_Phonebook_Demo" border="10" /></a>

## CONTENTS
- [Django Project: Investment Portfolio Tracker](#django-project)  
  1. [Story 1: Base/Home](#story-1-base)
  2. [Story 2: Create](#story-2-create)
  3. [Story 3: Index Page](#story-3-index)
  4. [Story 4: Detail Pages](#story-4-details)
  5. [Story 5: Edit Pages](#story-5-edits)
- [File Transfer Demo](#file-transfer-demo)
- [Icon Converter](#icon-converter)
- [Naughty or Nice Game](#naughty-or-nice-game)
- [Tkinter Phonebook Demo](#tkinter-phonebook-demo)
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
4. [Story 4: Detail Pages](#story-4-details)
5. [Story 5: Edit Pages](#story-5-edits)

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

### Stock Details/Edit
```HTML
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

## Story 5: Edits

### Commit
-	Add an edit page to the detail templates for two models
-	Add tab submenus for detail templates to view relate data from other tables and allow edit
-	Use model forms and instances to display the content of a single item from the database
-	Have the views function send the information for the single item and save any changes.
-	Include the option to delete an item with a confirmation that the user wants to delete.
-	Use a modal for the delete confirmation message
-	Add responsive and dynamic styling with image selection based on data from model instance

### Interface
![alt text](https://github.com/alex-moffat/Python-Projects/blob/master/Live-Project-Python/Screenshot_stock_edit.jpg "Stock_Edit")
![alt text](https://github.com/alex-moffat/Python-Projects/blob/master/Live-Project-Python/Screenshot_trade_edit.jpg "Trade_Edit")

### Trade Details/Edit
```HTML
{% block main %}

<!--===== TRADE DETAIL =====-->
<div class="container my-5">
    <div class="card shadow">

        <!--=== CARD HEADER ===-->
        <div class="card-header">
            <h4 class="font-weight-bold py-1">{{ trade }}</h4>
            <!--=== NAV TABS ===-->
            <ul class="nav nav-tabs card-header-tabs" id="myTab" role="tablist">
                <!--=== DETAILS ===-->
                <li class="nav-item">
                    <a class="nav-link active" id="home-tab" data-toggle="tab" href="#home" role="tab" aria-controls="home" aria-selected="true">Details</a>
                </li>
                <!--=== SUMMARY ===-->
                <li class="nav-item">
                    <a class="nav-link" id="summary-tab" data-toggle="tab" href="#summary" role="tab" aria-controls="summary" aria-selected="false">Summary</a>
                </li>
                <!--=== STOCK ===-->
                <li class="nav-item">
                    <a class="nav-link" id="stock-tab" data-toggle="tab" href="#stock" role="tab" aria-controls="stock" aria-selected="false">Stock</a>
                </li>
                <!--=== EDIT ===-->
                <li class="nav-item">
                    <a class="nav-link" id="edit-tab" data-toggle="tab" href="#edit" role="tab" aria-controls="edit" aria-selected="false">Edit</a>
                </li>
            </ul>
        </div>

        <!--===== CARD BODY / TAB CONTENT =====-->
        <div class="card-body tab-content" id="myTabContent">

            <!--===== DETAILS TAB =====-->
            <div class="tab-pane fade show active" id="home" role="tabpanel" aria-labelledby="home-tab">
                <div class="media mt-2">
                    <img class="thumb mr-3" src="{% if trade.paper %}{% static 'InvestmentApp/img/paper-trade.jpg' %}{% else %}{% static 'InvestmentApp/img/currency.jpg' %}{% endif %}" alt="trade-type">
                    <div class="media-body">
                        <h5 class="card-title mb-4">{{ stock.name }}</h5>
                        <div class="card-text">
                            <p><span class="font-weight-bold">Open Date:</span><br>{{ trade.open }}</p>
                            <p><span class="font-weight-bold">Quantity:</span><br>{{ trade.quantity }}</p>
                            <p><span class="font-weight-bold">Open Cost:</span><br>{{ trade.open_cost }}</p>
                            <p><span class="font-weight-bold">Close Date:</span><br>{{ trade.close }}</p>
                            <p><span class="font-weight-bold">Close Cost:</span><br>{{ trade.close_cost }}</p>
                        </div>
                    </div>
                </div>
            </div>

            <!--===== SUMMARY TAB =====-->
            <div class="tab-pane fade" id="summary" role="tabpanel" aria-labelledby="summary-tab">
                <h5 class="card-title mt-2 mb-4">{{ stock.name }}</h5>
                <div class="card-text">
                    <p><span class="font-weight-bold">Total Open Cost:</span><br>{{ trade.total_open }}</p>
                    <p><span class="font-weight-bold">Total Close Cost:</span><br>{{ trade.total_close }}</p>
                    <!--=== Styling for gain or lose ===-->
                    {% if trade.win == True %}
                    <p><span class="font-weight-bold">Total Gain:</span><br><span class="text-success">{{ trade.gain }}</span></p>
                    <p><span class="font-weight-bold">Percentage Gain:</span><br><span class="text-success">{{ trade.percent_gain }}</span></p>
                    {% elif trade.win == False  %}
                    <p><span class="font-weight-bold">Total Gain:</span><br><span class="text-danger">{{ trade.gain }}</span></p>
                    <p><span class="font-weight-bold">Percentage Gain:</span><br><span class="text-danger">{{ trade.percent_gain }}</span></p>
                    {% else %}
                        <p><span class="font-weight-bold">Total Gain:</span><br>{{ trade.gain }}</p>
                        <p><span class="font-weight-bold">Percentage Gain:</span><br>{{ trade.percent_gain }}</p>
                    {% endif %}
                </div>
                <hr class="my-4 bg-dark">
                <!--===== BUTTON - link to create new tracker =====-->
                <a name="tradeCreate" href="{% url 'InvestCreate' %}" class="btn btn-secondary shadow">Add A Trade Tracker</a>
            </div>

            <!--===== STOCK TAB =====-->
            <div class="tab-pane fade" id="stock" role="tabpanel" aria-labelledby="stock-tab">
                <h5 class="card-title mt-2 mb-4">{{ stock.name }}</h5>
                <div class="card-text">
                    <p>
                        <span class="font-weight-bold">Symbol:</span><br>{{ stock.symbol }}
                    </p>
                    <p>
                        <span class="font-weight-bold">Category:</span><br>{{ stock.get_category_display }}
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
                        <span class="font-weight-bold">Notes:</span><br>{{ stock.notes }}
                    </p>
                </div>
                <hr class="my-4 bg-dark">
                <!--===== BUTTON - link to create new tracker=====-->
                <a name="tradeCreate" href="{% url 'StockDetail' pk=stock.id %}" class="btn btn-secondary shadow">View {{ stock.symbol }} Details and Trades</a>
            </div>

            <!--===== EDIT TAB =====-->
            <div class="tab-pane fade" id="edit" role="tabpanel" aria-labelledby="edit-tab">
                <h5 class="card-title mt-2 mb-4">{{ stock.name }}</h5>

                <form name="tradeForm" method="POST" action="{% url 'TradeUpdate' pk=trade.id %}">
                    <!-- Cross Site Request Forgery (csrf_token) protection -->
                    {% csrf_token %}
                    <!-- Render each field  -->
                    {% for field in trade_form %}
                    <div class="fieldWrapper form-group" aria-required="{% if field.field.required %}true{% else %}false{% endif %}">
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
                        {% if field.errors %}
                            {% for error in field.errors %}
                                <small class="form-text text-danger">{{ error }}</small>
                            {% endfor %}
                        {% endif %}
                    </div>
                    {% endfor %}
                    <!--===== BUTTONS =====-->
                    <div class="mt-5">
                        <a name="tradeDetail" href="{% url 'TradeDetail' pk=trade.id %}" class="btn btn-secondary shadow">Cancel</a>
                        <button name="tradeForm" type="submit" class="btn btn-success shadow">Save Changes</button>
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
                                <p>Please be sure you want to delete this trade tracker.</p>
                                <p><b>This action can not be undone.</b></p>
                            </div>
                            <!-- FOOTER -->
                            <div class="modal-footer">
                                <button type="button" class="btn btn-secondary" data-dismiss="modal">Cancel</button>
                                <a name="delete" href="{% url 'DeleteTrade' pk=trade.id %}" class="btn btn-danger">Delete Data</a>
                            </div>
                        </div>
                    </div>
                </div>
            </div>
        </div>

        <!--===== CARD FOOTER - MESSAGE - Success/Error =====-->
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

{% endblock %}
```
## File Transfer Demo

### Commit
- A program to identify & move all .txt files from one folder to another with the click of a button.
- Find all .txt files in source folder modified in the last 24 hours and copy to destination folder.
- GUI allowing user to browse and choose a specific folder that will contain the files to copied/moved from.
- GUI allowing user to browse and choose a specific folder that will receive the copied files.
- GUI allowing user to manually initiate the 'file check' process that is performed by the script.

### Interface
![alt text](https://github.com/alex-moffat/Python-Projects/blob/master/File%20Transfer%20Program/Screenshot_file_transfer.jpg "File_Transfer")

### Code
```python
# PYTHON: 3.8.2
# AUTHOR: Alex Moffat
# PURPOSE: File Transfer Demo
#=============================================================================
description = """
This program was written by Alex Moffat.\n
This is a demonstration of programming based on requirements given from The Tech Academy Python Course. \n
"""
requirements="""
A program to identify & move all .txt files from one folder to another with the click of a button.
Find all .txt files in source folder modified in the last 24 hours and copy to destination folder.
GUI allowing user to browse and choose a specific folder that will contain the files to copied/moved from.
GUI allowing user to browse and choose a specific folder that will receive the copied files.
GUI allowing user to manually initiate the 'file check' process that is performed by the script.
"""
contact = """
Alex Moffat\n
wamoffat4@gmail.com\n
(917) 674-4820"""

#===== TAGS
"""
 datetime, now, deltatime, total_seconds, open, write, close, os, getmtime, listdir, join,
 shutil, move, filedialog, messagebox, path error checking
"""
#=============================================================================

#===== IMPORTED MODULES
import os
import shutil
from tkinter import *
from tkinter import messagebox
from tkinter import filedialog
from datetime import *

#===== VARIABLES
tStart = datetime.now() # script timing
tInc = datetime.now() # script increment timing
source = "" # folder where the source files are
destination = "" # folder where files should be transfered to

#========== SCRIPT TIMING - gets elapsed time of script execution, reset increment time
def sTime(name):
    global tInc
    if name != None:
        iTime = round(timedelta.total_seconds(datetime.now() - tInc) * 1000)
        tTime = round(timedelta.total_seconds(datetime.now() - tStart) * 1000)
        print("SCRIPT {} completed in {} ms and total time from start is {} ms\n".format(name, iTime , tTime))
    tInc = datetime.now() 


#=============================================================
#========== TKINTER GUI - CREATE tkinter window with grid
#=============================================================
def createGUI():
    #===== WINDOW =====
    win = Tk()
    #=== title & icon
    win.title('Extract & Transfer txt Files')
    win.iconbitmap('favicon.ico')
    #=== size & position center
    win.resizable(width=False, height=False)
    #===== ENTRIES =====
    v1 = StringVar()
    v2 = StringVar()
    e1 = Entry(win, width=100, textvariable = v1)
    e2 = Entry(win, width=100, textvariable = v2)
    #=== size & position
    e1.grid(row=0, column=1, columnspan=3, padx=(10,20), pady=(40,10), sticky=N+S+W+E)
    e2.grid(row=1, column=1, columnspan=3, padx=(10,20), pady=(0,10), sticky=N+S+W+E)
    #===== BUTTONS =====
    b1 = Button(win, text = "Source")
    b2 = Button(win, text = "Destination")
    b3 = Button(win, text = "Transfer All txt Files")
    b4 = Button(win, text = "Copy Recently Modified Files")
    b5 = Button(win, text = "Close Program")
    #=== configure
    b1.configure(command=lambda obj=v1: getDir(obj))
    b2.configure(command=lambda obj=v2: getDir(obj))
    b3.configure(height=2, command=lambda sPath=v1, dPath=v2: extractTextFiles(sPath, dPath))
    b4.configure(height=2, command=lambda sPath=v1, dPath=v2: copyRecent(sPath, dPath))
    b5.configure(height=2, command=win.destroy)
    #=== size & position
    b1.grid(row=0, column=0, padx=(20,10), pady=(40,10), sticky=W+E)
    b2.grid(row=1, column=0, padx=(20,10), pady=(0,10), sticky=W+E)
    b3.grid(row=2, column=0, padx=(20,10), pady=(0,20))
    b4.grid(row=2, column=1, padx=(10,10), pady=(0,20), sticky=W)
    b5.grid(row=2, column=3, padx=(10,20), pady=(0,20), sticky=E)
    sTime('createGUI') # script timer
    win.mainloop()
    
#========== GET DIR - tkinter askdirectory, invoke dialog modal, get folder path from user, place folderpath into Entry widget
def getDir(obj):
    sPath = filedialog.askdirectory()
    obj.set(sPath)

#========== CHECK PATHS - make sure both paths are valid
def checkPaths(sPath, dPath):
    global source, destination
    source = sPath.get().strip()
    destination = dPath.get().strip()
    if source == "" or destination == "":
        #===== make sure both paths are selected
        messagebox.showwarning("INVALID PATH", "Make sure both the source and destination folders are selected.")
        return False
    elif source == destination:
        #===== make sure both paths different from each other
        messagebox.showwarning("INVALID PATH", "Make sure the source and destination folders are different.")
        return False
    else:
        #===== make sure source path is valid
        try:
            files = os.listdir(source)            
        except:
            messagebox.showwarning("INVALID PATH", "Source path is not valid. Please select another source folder.")
            return False
        try:
            files = os.listdir(destination)            
        except:
            messagebox.showwarning("INVALID PATH", "Destination path is not valid. Please select another destination folder.")
            return False
    return True

#========== EXTRACT TEXT FILES - find all .txt files in source folder
def extractTextFiles(sPath, dPath):
    sTime(None)
    if checkPaths(sPath, dPath): # check if both paths are valid
        rString = ""
        fCount = 0
        #===== search all files in source folder for .txt files
        files = os.listdir(source)
        for f in files:
            fPath = os.path.join(source, f)
            #=== get txt files, count, get last modified date, transfer to destination 
            if fPath.endswith('.txt'):
                fCount += 1
                mTime = date.fromtimestamp(os.path.getmtime(fPath))
                rString = rString + '\n' + f + ' --> Last modified: ' + str(mTime)
                shutil.move(fPath, destination)
        print('There where {} txt files moved from the source folder to the destination folder: {}'.format(fCount, rString))
    sTime('extractTextFiles') # script timer

#========== COPY RECENT - find all .txt files in source folder modified in the last 24 hours and copy to destination folder
def copyRecent(sPath, dPath):
    sTime(None)
    if checkPaths(sPath, dPath): # check if both paths are valid 
        rString = ""
        fCount = 0
        #===== search all files in source folder for .txt files
        files = os.listdir(source)
        for f in files:
            fPath = os.path.join(source, f)
            #=== get txt files, count, get last modified date, copy to destination 
            if fPath.endswith('.txt'):
                mTime = datetime.fromtimestamp(os.path.getmtime(fPath))
                #=== Files modified in the last 24 hours (86400 seconds)
                if timedelta.total_seconds(tStart - mTime) <= 86400: 
                    fCount += 1
                    rString = rString + '\n' + f + ' --> Last modified: ' + str(mTime)
                    shutil.copy(fPath, destination)
        print('There where {} recently modified txt files copied to the destination folder: {}'.format(fCount, rString))
    sTime('copyRecent') # script timer
    
#=============================================================
#========== MAIN
#=============================================================        
if __name__ == '__main__':
    createGUI()    
```

## Icon Converter

### Commit
This module designed to convert an image to a base64 string and a base64 string to image:
- Convert Image to String and return result.
- Convert String to Image and return result.
- Take image path - reads 'image' and writes base64 string to txt file with same name in same path.

### Code
```python
# Python: 3.8.2
# Author: Alex Moffat
# Purpose: Convert Image to String, Convert String to Image 
#=============================================================
"""TAGS:
base64, b64encode, b64decode
"""
#=============================================================
description = """
This program was written by Alex Moffat.\n
This module designed to convert an image to a base64 string and a base64 string to image.\n
This module has 3 methods:\r
1. image2String(i) - takes image path (i) - reads 'image' and returns base64 string.\r
2. image2Text(i) - takes image name in same folder (i) - reads 'image' and writes base64 string to txt file with same name.\r
3. string2Image(s, f) - takes base64 string (s) & 'fileName.png' (f) - writes 'image' file"""

contact = """
Alex Moffat\n
wamoffat4@gmail.com\n
(917) 674-4820"""
#=============================================================

#========== IMPORTED MODULES
import base64

#========== IMAGE 2 STRING - takes image path (i) - uses "rb" read binary switch, reads "image" and returns base64 string
def image2String(i):
    with open(i, "rb") as imageFile:
        rStr = base64.b64encode(imageFile.read())
        print(rStr)
        return rStr

#========== IMAGE 2 Text - takes image name in same folder (i) - uses "rb" read binary switch, reads "image" and writes base64 string to txt file with same name
def image2Text(i):
    bStr=image2String(i)
    fileName = i.split('.')[0] + '.txt'
    newFile = open(fileName, "wb")
    newFile.write(bStr)
    newFile.close()

#========== STING 2 IMAGE - takes base64 string (s) & "fileName.png" (f) - uses "wb" write binary switch, writes "image"
def string2Image(s, f):
    newFile = open(f, "wb")
    newFile.write(base64.b64decode(s))
    newFile.close()


#=============================================================
#========== MAIN
#=============================================================
if __name__ == '__main__':
    pass
```

## Naughty or Nice Game

### Description
GA console word game that presents the user with random scenarios and asks which option they will choose. At the end the user is told if they win or lose and given the option to play again. This complete project was a simple example of loops and if/then statements that was completed in about 2 hours. 

### Code
```python
# Python: 3.8.2
# Author: Alex Moffat
# Purpose: A game that shows off basic programming skills

#===== IMPORTED MODULES
import random

#===== GLOBAL VARIABLES 
scenes, name, yes, nope = [], "", 0, 0
print(name)

#===== SET SCENES : creates a list of 5 scenarios (tuples) of stranger interactions  - Sets messages for scenario, question, nope response, yes response
def setScenes():
    global scenes
    scenes = [ 
    ('A smelly stranger approaches you and says hello.', 'Do you say hello?', 'The stranger glares at you and storms off...', 'The stranger smiles and says you made his day...'), 
    ('You are in a hurry and an old man approaches and asks for directions.', 'Do you stop to give him directions?', 'The old man seems confused as you walk away...', 'The old man thanks you for your time...'),
    ('An old woman with a walker is crossing very slowly across a busy street.', 'Do you help her across the street?', 'The old women falls down at the curb on the other side...', 'The old women says you are very kind...'),
    ('A stranger wants to have a conversation about the weather.', 'Do you have a conversation about the weather?', 'The stranger mutters something about having no friends and walks away...', 'You find out the stranger lives in your home town and knows your mother...'),
    ('You are in a rush to get to work and a stranger asks for the time.', 'Do you stop to give the time?', 'The stranger yells that you are mean as you are running away...', 'The stranger says have a great day and enjoy the sunshine...')]

#===== START GAME : Check if played before --> start game
def startGame():
    print("\nThank you for playing again {}!".format(name)) if name != "" else getName()
    setScenes()
    naughtyNice()

#===== GET NAME : Get players name for global variable 'name', reset yes and nope scores to zero
def getName():
    global name, yes, nope
    go = True
    while go:
        name = input('What is your name? \n>>> ').capitalize()
        if name == "":
            print('You need to provide a name!')
        else:
            print("\nWelcome {}".format(name))
            print('\nIn this game you will be greeted by several different people.')
            print('You can choose to be naughty or nice, but at the end of the game your fate will be sealed by your actions.')
            yes, nope, go = 0, 0, False

#===== NAUGHTYNICE - Check if valid answer then score 1 yes/nope
def naughtyNice():
    global scenes, yes, nope
    go = True
    rStranger = random.sample(scenes,1)[0] #pull a random scene tuple from strangers list
    scenes.remove(rStranger) # remove current scene so we don't repeat
    while go:
        pick = input('\n{scene} \n{question} (Y/N): \n>>> '.format(scene = rStranger[0], question = rStranger[1])).upper()
        if pick == "": # check if left blank
            print('You need to provide an answer\n>>> ')
        elif pick != "Y" and pick != "N": # check if valid answer
            print('You need to answer with \"Y\" (be nice) or \"N\" (be naughty)')            
        else: # valid answer - give message and score
            go = False
            if pick == 'N':
                print("\n{N}".format(N = rStranger[2]))
                nope += 1
            else:
                print("\n{Y}".format(Y = rStranger[3]))
                yes += 1
    print("\n{player}, your current total: \n({naughty} Naughty) and ({nice} Nice)".format(player = name, naughty = nope, nice = yes))
    checkScore()

#===== SCORE - when player has answered YES or nope 3 times - win/lose condition is met - otherwise continue game
def checkScore(): 
    if yes > 2: # WIN - Nice condition
        print("\nNice job {}, you win! \nYou are nice and Santa will bring you lots of presents this year. \nEveryone loves you and you've made lots of friends along the way!".format(name))
    elif nope > 2: # LOSE - Naughty condition
        print("\nToo bad {}, game over! \nYou are naughty and Santa is not bringing you any presents this year. \nKeep it up and you will live alone with no friends to call your own!".format(name))
    else:
        naughtyNice()
    again()

#===== AGAIN - ask if play again - terminate game or reset variables and start again 
def again():
     go = True
     while go:
         choice = input('\nDo you want to play again? (Y/N): \n>>> ').upper()
         if choice == 'Y':
             go = False
             startGame()
         elif choice == 'N':
             go = False            
             print("\nOh, so sad, sorry to see you go!")
             quit()
         else:
             print("\nEnter (Y) for 'Yes' or (N) for 'No':\n>>> ")


if __name__ == '__main__':
    startGame()
```

## Tkinter Phonebook Demo

### Description
This is a demonstration of OOP using the Python Tkinter GUI module with parent and child relationships. This app uses a custom module 'SQL_functions.py' that wraps the SQLite3 module with error handling and reporting. This demo was built in about 4 days.

### Commit
- Build tKinter GUI. 
-	Create a SQL module to handle all SQL transactions with error handling.
- This demo creates and populates a database on first start. 
- Users can ADD, UPDATE or DELETE users.
- Use code to combine first and second name for display in Listbox
- Use varchar datatype to reduce size in database
-	Add data validation to phone that enforces 10-digit numbers only
- Add validation to email that enforces email formatting
- Add validation to check if changes are made before update
- Add verification of delete a record
-	Remove unneeded variable assignments for variables that are not referenced
-	Display names in the Listbox in alphabetical order (lastname, firstname).
- Add working dropdown menu  
-	Add copy to clipboard functionality
-	Add export database functionality using os module
-	Add help menu functionality
-	Customize GUI colors
-	Add rolodex icon to menu bar
- Embed icon into executable with base64 string 
- Create full executable with all modules encapsulated

### Interface
![alt text](https://github.com/alex-moffat/Python-Projects/blob/master/Tkinter%20Phonebook/Screenshot_Phonebook.jpg "Phonebook_Demo")

### Main Program
```python
# Python: 3.8.2
# Author: Alex Moffat
# Purpose: Tkinter Demo Phonebook. Demonstrating OOP, Tkinter GUI module using Tkinter Parent and Child relationships. 
#=============================================================
"""TAGS:
tkinter, Tk(), master, Frame, grid, row, column, label, entry, button,
iconbitmap, title, resizeable, config, padx, pady, sticky, WM_DELETE_WINDOW
columnspan, font, fg, bg, format, mainloop, destroy, SQL, sqlite3.version
error handling, connect, cursor, execute, CREATE, INSERT, SELECT,
slice, upper, fetchall, lambda, command, Listbox, Scrollbar, bind, set,
ListboxSelect, yview, yscrollcommand, exportselection, winfo_screenwidth,
winfo_screenheight, messgaebox, event, widget, withdraw, clipboard_clear,
clipboard_append, clipboard_get, update, open, write, read, close
"""
#=============================================================
description = """
This program was written by Alex Moffat.\n
This is a demonstration of OOP using the Python Tkinter GUI module with parent and child relationships.\n
This app uses a custom module 'SQL_functions.py' that wraps the SQLite3 module with error handling and reporting."""

use = """
This demo creates and populates a database on first start. You can ADD, UPDATE or DELETE users.\n
ADD: Fill in first name, last name, 10 digit phone number, and email address, then press 'Add'. Entries with the same first and last name are not permitted.\n
UPDATE: Select an entry from the list box and edit the phone number and/or email address in the entry fields, then press 'Update'. Name changes are not permitted.\n
DELETE: Select an entry from the list box, then press 'Delete'.\n
COPY & EXPORT: From the 'File' menu, copy individual selected records to the clipboard or export the entire database to a .txt file."""

contact = """
Alex Moffat\n
wamoffat4@gmail.com\n
(917) 674-4820"""
#=============================================================

#========== IMPORTED MODULES
import os
import tkinter as tk
from tkinter import * # this is required to make all widgets in tkinter available
from tkinter import messagebox
import SQL_functions
import icon_converter

#========== VARIABLES
w = 500 # App Window width
h = 330 # App Window height
DB = 'demo_phonebook.db' # demo phonebook database
phoneInsert = 'INSERT INTO phonebook (fName, lName, phone, email) VALUES (?, ?, ?, ?)' # standard SQL INSERT statement
phoneSelect = "SELECT fName, lName, phone, email FROM phonebook WHERE phoneID = '{}'" # standard SQL SELECT statement 
selectRecordCount = 'SELECT COUNT(phoneID) FROM phonebook' # count db records
icon = ""

#=============================================================
#========== TKINTER PARENT WINDOW
#=============================================================
class ParentWindow(Frame):
    def __init__ (self, master, *args, **kwargs):
        Frame.__init__(self, *args, **kwargs)
        #===== master window
        self.master = master
        M = self.master # Assign self.master to single digit variable "M" for cleaner code        
        #===== protocol - built-in tkinter method to catch user click the corner "X" on Windows OS, calls function in '_func' module
        M.protocol("WM_DELETE_WINDOW", lambda: askQuit(self))
        
        #========== MENU ==========
        #===== title bar & icon
        icon_converter.string2Image(icon, 'temp.ico') # create icon from base64 string
        M.iconbitmap('temp.ico')
        os.remove('temp.ico')
        M.title('Tkinter Phonebook Demo')
        #===== dropdown menus - Instantiate the Tkinter menu dropdown object - this menu will appear at the top of our window
        menubar = Menu(M)
        #=== file menu
        filemenu = Menu(menubar, tearoff=0)
        filemenu.add_command(label="Copy", underline=1,command=lambda: onCopy(self))
        filemenu.add_command(label="Export", underline=1,command=lambda: onExport(self))
        filemenu.add_separator()
        filemenu.add_command(label="Exit", underline=1,command=lambda: askQuit(self))
        menubar.add_cascade(label="File", underline=0, menu=filemenu)
        #=== help menu
        helpmenu = Menu(menubar, tearoff=0) # defines the particular drop down colum and tearoff=0 means do not separate from menubar
        helpmenu.add_command(label="How to use this program", command=lambda: helpMenu('use'))
        helpmenu.add_command(label="About Phonebook Demo", command=lambda: helpMenu('about')) # add_command is a child menubar item of the add_cascade parent item
        helpmenu.add_separator()
        helpmenu.add_command(label="Contact Author", command=lambda: helpMenu('contact')) # add_command is a child menubar item of the add_cascade parent item
        menubar.add_cascade(label="Help", menu=helpmenu) # add_cascade is a parent menubar item (visible heading)
        M.config(menu=menubar, borderwidth='1')        

        #========== WINDOW ==========
        #===== color
        M.config(bg='#F0F8FF')
        #===== size & position
        M.resizable(width=False, height=False)
        x = int((M.winfo_screenwidth()/2) - (w/2)) # calling built-in tkinter function to get display width
        y = int((M.winfo_screenheight()/2) - (h/2)) # calling built-in tkinter function to get display height
        M.geometry('{}x{}+{}+{}'.format(w, h, x, y))
        
        #========== GUI ==========
        #===== labels
        Label(M, text='First Name ', bg='#F0F8FF').grid(row=0, column=0, padx=(27,0), pady=(10,0), sticky=N+W)
        Label(M, text='Last Name ', bg='#F0F8FF').grid(row=2, column=0, padx=(27,0), pady=(10,0), sticky=N+W)
        Label(M, text='Phone Number ', bg='#F0F8FF').grid(row=4, column=0, padx=(27,0), pady=(10,0), sticky=N+W)
        Label(M, text='Email Address ', bg='#F0F8FF').grid(row=6, column=0, padx=(27,0), pady=(10,0), sticky=N+W)
        Label(M, text='Database: ', bg='#F0F8FF').grid(row=0, column=2, padx=(0,0), pady=(10,0), sticky=N+W)
        #===== entries
        self.E_fName = Entry(M, text='First') # VAR E_fName 
        self.E_fName.grid(row=1, column=0, rowspan=1, columnspan=2, padx=(30,40), pady=(0,0), sticky=N+E+W)
        self.E_lName = Entry(M, text='Last') # VAR E_lName
        self.E_lName.grid(row=3, column=0, rowspan=1, columnspan=2, padx=(30,40), pady=(0,0), sticky=N+E+W)
        self.E_phone = Entry(M, text='Phone') # VAR E_phone
        self.E_phone.grid(row=5, column=0, rowspan=1, columnspan=2, padx=(30,40), pady=(0,0), sticky=N+E+W)
        self.E_email = Entry(M, text='Email') # VAR E_email
        self.E_email.grid(row=7, column=0, rowspan=1, columnspan=2, padx=(30,40), pady=(0,0), sticky=N+E+W)
        #===== scrollbar & listbox
        self.phoneIDs = [] # stores unique phoneID for each person in the list
        self.sBar = Scrollbar(M, orient=VERTICAL) # VAR sBar
        self.sBar.grid(row=1, column=5, rowspan=7, columnspan=1, padx=(0,0), pady=(0,0), sticky=N+S+E)
        self.lBox = Listbox(M, exportselection=0, yscrollcommand=self.sBar.set) # VAR lBox
        self.lBox.grid(row=1, column=2, rowspan=7, columnspan=3, padx=(0,0), pady=(0,0), sticky=N+S+E+W)
        #===== cross-reference: scrollbar & listbox
        self.sBar.config(command=self.lBox.yview) 
        self.lBox.bind('<<ListboxSelect>>', lambda event: onSelect(self,event)) # the "event' object is passed to this function with the class object "self"
        #===== buttons
        self.B_add =  Button(M, width=12, height=2, text='Add', bg='#A8D7FF', command= lambda: onAdd(self))
        self.B_add.grid(row=8, column=0, padx=(25,0), pady=(45,10), sticky=W)
        self.B_update = Button(M, width=12, height=2, text='Update', bg='#A8D7FF', command= lambda: onUpdate(self))
        self.B_update.grid(row=8, column=1, padx=(15,0), pady=(45,10), sticky=W)
        self.B_delete = Button(M, width=12, height=2, text='Delete', bg='#A8D7FF', command= lambda: onDelete(self))
        self.B_delete.grid(row=8, column=2, padx=(15,0), pady=(45,10), sticky=W)
        self.B_close = Button(M, width=12, height=2, text='Close', bg='#A8D7FF', command= lambda: askQuit(self))
        self.B_close.grid(row=8, column=4, padx=(15,0), pady=(45,10), sticky=E)
        #===== functions
        createDB()
        onRefresh(self)        

#=============================================================
#========== TKINTER FUNCTIONS
#=============================================================

#========== ON COPY - copy a selected database person to the clipboard
def onCopy(self):
    if not checkSelect(self): return # Determine if a selection from listbox is made
    index = self.lBox.curselection()[0] # Returns the line number of variable lBox (tkinter listbox) - used [0] to get first item from curselection() tuple return
    dataSet = SQL_functions.sqlExecute(DB, phoneSelect.format(self.phoneIDs[index]))
    info = "{}, {}, {}, {}".format(dataSet[0][0], dataSet[0][1], dataSet[0][2], dataSet[0][3])
    r = Tk()
    r.withdraw() # keep window from popping up
    r.clipboard_clear()
    r.clipboard_append(info)
    r.update()
    print("{} copied to clipboard".format(r.clipboard_get()))

#========== ON EXPORT - export entire database to a .txt using the os module
def onExport(self):
    fileName = 'phonebook_data.txt'
    filePath = os.getcwd()
    abPath = os.path.join(filePath, fileName)
    dataSet = SQL_functions.sqlExecute(DB, "SELECT lName, fName, phone, email FROM phonebook ORDER BY lName, fName")
    f = open(fileName, 'w') # w = overwrite
    f.write('Last Name\tFirst Name\tPhone Number\tEmail Address\r')
    f.close()
    f = open(fileName, 'a') # a = append what exists
    records = 0
    for d in dataSet:
        records += 1
        f.write('{}\t{}\t{}\t{}\r'.format(d[0], d[1], d[2], d[3]))
    f.close()    
    messagebox.showinfo("EXPORT COMPLETE", '{} records saved to {}'.format(records, abPath))
    
#========== ASK QUIT - make sure user wants to exit App - use tkinter method messagebox
def askQuit(self):
    if messagebox.askokcancel("Exit Program", "Are you sure you want to exit the program?"): # returns True if user selects "OK"
        self.master.destroy()
        os._exit(0) # prevents memory leaks by purging variables and widgets associated with the application

#========== HELP MENU - tell about this program
def helpMenu(m):
    if m == 'use':
        messagebox.showinfo("How to use Phonebook Demo", use)
    elif m == 'about':
        messagebox.showinfo("About Phonebook Demo", description)
    elif m == 'contact':
        messagebox.showinfo("Contact Developer", contact)

#========== CHECK FORMAT - make sure all data is formatted correctly
def checkFormat(fName, lName, phone, email):
    msg = ""
    if len(fName) == 0 or len(lName) == 0 or len(phone) == 0 or len(email) == 0: #===== all fields are filled out
        msg = "Make sure you have filled out all four fields"
    elif not "@" or not "." in email: #===== email format
        msg = "Incorrect email format"
    elif len(phone) != 10: #===== phone 10 digits
        msg = "Phone number must have exactly 10 digits"
    else: #===== phone numbers only
        try: 
            int(phone)
        except ValueError:
            msg = "Phone number must contain numbers only"
    return msg

#========== ON CLEAR - clear all Entry widgets
def onClear(self):
    self.E_fName.delete(0, END) # deletes data (text) from the beginning (Position 0) of text box to the end
    self.E_lName.delete(0, END)
    self.E_phone.delete(0, END)
    self.E_email.delete(0, END)    

#=============================================================
#========== SQL related
#=============================================================

#========== CREATE DB - create database and table
def createDB():
    #===== Create database
    SQL_functions.dbConnect(DB)
    #===== Create table
    sCreateTable = "CREATE TABLE IF NOT EXISTS phonebook(\
        phoneID INTEGER PRIMARY KEY AUTOINCREMENT,\
        fName VARCHAR(30),\
        lName VARCHAR(30),\
        phone VARCHAR(10),\
        email VARCHAR(255))"
    SQL_functions.sqlExecute(DB, sCreateTable)
    #===== populate DB - check if first time through, if so add an entry
    dbCount = SQL_functions.sqlExecute(DB, selectRecordCount) # dataset return is a list
    if not bool(dbCount[0][0]):
        data = [
            ('John', 'Doe', '1111111111', 'jdoe@email.com'),
            ('Alex', 'Moffat', '9176744820', 'wamoffat4@gmail.com'),
            ('Zuli', 'Kitty', '2223334444', 'zuli@kitty.com'),
            ('Albert', 'Einstein', '2062321010', 'albert@einstein.com'),
            ('Nikola', 'Tesla', '2123331010', 'nikola@tesla.com'),
            ('Thomas', 'Edison', '1847001931', 'thomas@edison.com'),
            ('Benjamin', 'Franklin', '1706001790', 'ben@franklin.com'),
            ('Henry', 'Ford', '1863001947', 'henry@ford.com'),
            ('Alexander', 'Graham Bell', '1847001922', 'alex@bell.com'),
            ('Steve', 'Jobs', '1955002011', 'steve@jobs.com'),
            ('Bill', 'Gates', '1955000000', 'bill@gates.com')]
        SQL_functions.sqlInsert(DB, phoneInsert, data)
    else:
        print("Database already exists")

#========== ON SELECT
def onSelect(self, event):
    listBox = event.widget # REDUNDANT: event.widget is the widget element (.!listbox) that triggered the event - in this case the tkinter Listbox 
    select = listBox.curselection()[0] # REDUNDANT: Returns the line number of selected event widget (tkinter listbox) 
    index = self.lBox.curselection()[0] # Returns the line number of variable lBox (tkinter listbox) - used [0] to get first item from curselection() tuple return
    fullName = listBox.get(index) # returns the text (fullName) of the line selected
    print(fullName)
    dataSet = SQL_functions.sqlExecute(DB, phoneSelect.format(self.phoneIDs[index]))
    onClear(self)
    for d in dataSet:
        self.E_fName.insert(0, d[0]) # inserts data (text) starting from the beginning of the text box (0) 
        self.E_lName.insert(0, d[1])
        self.E_phone.insert(0, d[2])
        self.E_email.insert(0, d[3])

#========== ON ADD - get text in 'Entry' widgets, normalize data, data format check, write data to database     
def onAdd(self):
    #===== variables
    fName = self.E_fName.get()
    lName = self.E_lName.get()
    phone = self.E_phone.get()
    email = (self.E_email.get()).strip()
    #===== normalize & concatenate name
    fName = (fName.strip()).title() 
    lName = (lName.strip()).title()
    phone = phone.strip(' ,().-') #removing all other characters accept numbers
    #===== data format checking
    msg = checkFormat(fName, lName, phone, email)
    if msg !="": #===== message - only if data format error
        messagebox.showerror("Invalid Data Entered", msg)
    else: #===== check for duplicate name
        dbCount = SQL_functions.sqlExecute(DB, "SELECT COUNT(phoneID) FROM phonebook WHERE fName = '{}' and lName = '{}'".format(fName, lName)) # dataset return is a list
        if not bool(dbCount[0][0]):
            SQL_functions.sqlInsert(DB, phoneInsert, (fName, lName, phone, email))
            onRefresh(self) # refresh Listbox with new fullName            
        else:
            messagebox.showerror("Invalid Data Entered","{} {} already exists in the database".format(fName, lName))
        onClear(self)
    
#========== ON DELETE - checks if last entry in database, ask for confirmation of delete, execute SQL delete
def onDelete(self):
    if not checkSelect(self): return # Determine if a selection from listbox is made
    index = self.lBox.curselection()[0] # index of the listbox selection
    fullName = self.lBox.get(index) # the selected fullName value in the Listbox
    #===== check DB record count - cannot delete the last record or error will occur
    dbCount = SQL_functions.sqlExecute(DB, selectRecordCount) # dataset return is a list
    if dbCount[0][0] > 1:
         #===== delete - check if want to delete first, if OK is select execute SQL delete 
        if messagebox.askokcancel("Delete Confirmation", "All information associated with {} \nwill be permenantly deleted. Ok to continue?".format(fullName)): # returns True if user selects "OK"
            SQL_functions.sqlExecute(DB, "DELETE FROM phonebook WHERE phoneID = '{}' ".format(self.phoneIDs[index]))             
            onClear(self)
            onRefresh(self)
    else:
        messagebox.showerror("Last Record Error", "{} is the last record in the database and cannot be deleted.".format(fullName))
    
#========== ON REFRESH - clear Listbox, SQL select all 'fullName' records, populate Listbox will all records
def onRefresh(self):
    self.phoneIDs = []
    self.lBox.delete(0, END)
    dataSet = SQL_functions.sqlExecute(DB, "SELECT phoneID, fName, lName FROM phonebook ORDER BY lName, fName")
    for d in dataSet:
        self.phoneIDs.append(d[0]) #put unique phoneID at the end of the phoneIDs list variable
        self.lBox.insert(END,"{} {}".format(d[1],d[2])) #put "full name" at the end of the listbox

#========== CHECK SELECT - Determine if a selection from listbox is made 
def checkSelect(self):
    try:
        index = self.lBox.curselection()[0] # index of the listbox selection
        return True
    except:
        messagebox.showinfo("Missing Selection","Please select a name from the list.")
        return False

#========== ON UPDATE - determine selection made, normalize data, check data formated correctly, update email and/or phone record
def onUpdate(self):
    if not checkSelect(self): return # Determine if a selection from listbox is made
    index = self.lBox.curselection()[0]
    fullName = self.lBox.get(self.lBox.curselection()) # the selected fullName value in the Listbox
    nameParse = fullName.split() # dividing the full name into a list [fName, lName]
    #===== normalize data
    phone = (self.E_phone.get()).strip(' ,().-') #removing all other characters accept numbers
    email = (self.E_email.get()).strip()
    #===== check if data changed
    dataSet = SQL_functions.sqlExecute(DB, phoneSelect.format(self.phoneIDs[index]))
    if dataSet[0][2] == phone and dataSet[0][3] == email:
        messagebox.showinfo('Cancelled Request', 'No changes to email or phone number have been detected.')
        return
    #===== data format checking
    msg = checkFormat(nameParse[0], nameParse[1], phone, email)
    if msg != "": #===== message - only if data format error
        messagebox.showwarning("Invalid Data Entered", msg)
    else: #===== update - confirm first
        if messagebox.askokcancel('Update Request', '{} will be updated: \nPhone: {} \nEmail: {}'.format(fullName, phone, email)): # returns 'True' if OK is clicked
            SQL_functions.sqlExecute(DB, "UPDATE phonebook SET phone = '{}', email = '{}' WHERE phoneID = '{}'".format(phone, email, self.phoneIDs[index]))
            onRefresh(self)
        else:
            messagebox.showinfo('Cancelled Request', 'No changes have been made to {} {}.'.format(nameParse[0], nameParse[1]))
        onClear(self)    
    
#=============================================================
#========== MAIN
#=============================================================
if __name__ == '__main__':
    master = Tk() # Tkinter call
    App = ParentWindow(master) #calls function with customiztion and provides Tk object as argument 
    master.mainloop() # keeps window open
```

### SQL Functions
```python
# PYTHON: 3.8.2
# AUTHOR: Alex Moffat
# PURPOSE: General use SQLite3 functions
"""
TAGS:
 SQL, sqlite3.version, error handling, connect, cursor, execute, CREATE, INSERT, SELECT
 slice, upper, fetchall, isinstance, ValueError as 
"""
# ============================================================================

#===== IMPORTED MODULES
import sqlite3

#========== CONNECT - establish connection to DB and print sqlite3 version
def dbConnect(db):
    conn = None
    try:
        conn = sqlite3.connect(db) # creates a db if one does not exist
        print(sqlite3.version)
    except ValueError as e:
        print("DB Connection Error: {}".format(e))
    finally:
        if conn: conn.close() # close db connection if open

#========== USE CONNECTION - establish connetion to DB and return open connection
def dbUse(db):
    conn = None
    try:
        conn = sqlite3.connect(db) # creates a db if one does not exist        
    except ValueError as e:
        print("DB Connection Error: {}".format(e))        
    return conn

#========== EXECUTE - pass database and a non-parameterized SQL statement
def sqlExecute(db, statement):
    conn = dbUse(db)
    if conn != None: #===== EXECUTE 
        try:
            cur = conn.cursor() # creates cursor object 'cur'
            cur.execute(statement)
            switch = statement[slice(0,6)].upper()
            if switch == 'SELECT': #===== SELECT
                dataset = cur.fetchall()
                if conn: conn.close()
                return dataset
            else:
                conn.commit()
                r = "record"
                if cur.rowcount > 1: r = "records"
                if switch == 'UPDATE': #===== UPDATE
                    printStr = "{} {} updated in database {}".format(cur.rowcount, r, db)
                elif switch == 'DELETE': #===== DELETE
                    printStr = "{} {} deleted in database {}".format(cur.rowcount, r, db)                    
                elif switch == 'INSERT': #===== INSERT
                    printStr = "{} {} inserted in database {}".format(cur.rowcount, r, db)
                else:
                    printStr = "Execute complete in database {}".format(db)
                print(printStr)
        except ValueError as e:
            print("DB Execute Error: {}".format(e))
        finally:
            if conn: conn.close()            
    else:
        print("DB Connection Error...cannot execute SQL statement")

#========== INSERT - can pass SQL db, table statement, values statement (can be single tuple or list of tuples)
def sqlInsert(db, statement, iValue):
    conn = dbUse(db)
    if conn != None: #===== INSERT 
        try:
            cur = conn.cursor() # creates cursor object
            if isinstance(iValue, list): #===== MULTIPLE ROW INSERT
                cur.executemany(statement, iValue)
                conn.commit()
                print(cur.rowcount, " records inserted.")
            elif isinstance(iValue, tuple): #===== SINGLE ROW INSERT
                cur.execute(statement, iValue)
                conn.commit()
                print(cur.rowcount, " record inserted.")
            else:
                print("DB INSERT Error: Values are not formatted correctly - need list or tuple")
        except ValueError as e:
            print("DB INSERT Error: {}".format(e))
        finally:
            if conn: conn.close()            
    else:
        print("DB Connection Error...cannot execute SQL statement")
     
if __name__ == '__main__':
    pass
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

