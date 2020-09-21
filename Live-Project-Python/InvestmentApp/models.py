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
