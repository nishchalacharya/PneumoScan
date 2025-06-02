from django.apps import AppConfig


class LoginappConfig(AppConfig):
    default_auto_field = "django.db.models.BigAutoField"
    name = "loginapp"
    
    
    
class YourAppConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'loginapp'

    def ready(self):
        import loginapp.signals
    
