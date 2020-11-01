from django.apps import AppConfig

class HoodappConfig(AppConfig):
    name = 'hoodapp'

    def ready(self):
        import hoodapp.signals