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
