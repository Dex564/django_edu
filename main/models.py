from django.db import models

class Category(models.Model):

    name = models.CharField(max_length=100, db_index=True)
    slug = models.SlugField(max_length=100, unique=True)

    class Meta:
        ordering = ('name',) # в бд будет отсртированно по имени
        verbose_name = 'Категория' # если делаем сайт на русском
        verbose_name_plural = 'Категории' # параметр отображения во множ числе

    def __str__(self): # метод, который определяет как будет отображаться обьект в адмике
        
        return self.name
    

class Product(models.Model):
    category = models.ForeignKey(Category, related_name='find_where_this_written', on_delete=models.CASCADE) # related_name - имя, которое будет использоваться в админке
    name = models.CharField(max_length=50, db_index=True)
    slug = models.SlugField(max_length=100, unique=True)
    image = models.ImageField(upload_to='products/%Y/%m/%d', blank=True) # blank=true для того, чтобы в админке image мог быть пустым
    description = models.TextField(blank=True)
    price = models.DecimalField(max_digits=10, decimal_places=2) # DecimalField - 10.07 , числа с плавающей точкой, нужно для высчитывания скидки, IntegerField тут не прокатит, decimal_places - кол-во знаков после точки
    available = models.BooleanField(default=True)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ('name',)
    
    def __str__(self):
        return self.name
    
