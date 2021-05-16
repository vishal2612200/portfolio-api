from django.apps import AppConfig


class TradeConfig(AppConfig):
    name = 'trade'
    verbose_name = 'Trade'

    def ready(self):
        import trade.signals
