from django.db import models
from django.utils import timezone
from django.conf import settings
from django.core.validators import MinValueValidator

# Create your models here.

TICKER_CHOICES = (
    ("TCS", "Tata Consultancy Services Limited"),
    ("WIPRO", "Wipro Limited"),
    ("GODREJIND", "Godrej Industries Ltd")
)

class Trade(models.Model):
    class Category(models.TextChoices):
        BUY = 'BUY'
        SELL = 'SELL'
    
    shareholder = models.ForeignKey(settings.AUTH_USER_MODEL, 
                                on_delete=models.CASCADE, default=1)
    unit_price = models.FloatField(validators=[MinValueValidator(0)])
    trd_share_quantity = models.PositiveIntegerField(editable=True)
    created = models.DateTimeField(default=timezone.now, editable=False)
    ticker = models.CharField(max_length=100,
                             choices=TICKER_CHOICES)
    category = models.CharField(
        max_length=20, choices=Category.choices)

    def __str__(self):
        return '{} was {} by ({})'.format(self.ticker, self.category, self.shareholder)

    class Meta:
        ordering = ['-created']


class Portfolio(models.Model):
    shareholder = models.ForeignKey(settings.AUTH_USER_MODEL, 
                                on_delete=models.CASCADE, default=1)
    ticker = models.CharField(max_length=100,
                             choices=TICKER_CHOICES,
                             )
    created = models.DateTimeField(default=timezone.now, editable=False)                      
    avg_buy_price = models.FloatField(default=0, validators=[MinValueValidator(0)])
    share_quantity = models.PositiveIntegerField(editable=True)

    def __str__(self):
        return '{}: average buy price {} with  {} quantity'\
            .format(self.shareholder, self.avg_buy_price, self.share_quantity)

    class Meta:
        ordering = ['-created']
