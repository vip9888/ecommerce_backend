from django.apps import AppConfig

# this is the config file for the products app
# it is used to tell django that this app is installed and ready to use

class ProductsConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'apps.products'
