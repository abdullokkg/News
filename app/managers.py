from django.db.models import Manager
from parler.managers import TranslatableManager

class CategoryManager(TranslatableManager):
    
    def get_category(self,category_name):

        try:
            return self.get(name__icontains = category_name)
        except Exception as e:
            return None
