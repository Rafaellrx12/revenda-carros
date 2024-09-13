from django.db.models import Sum
from django.dispatch import receiver
from django.db.models.signals import pre_save,pre_delete,post_save,post_delete
from cars.models import Car,CarInventory




def car_inventory_update():
    car_count = Car.objects.all().count()
    car_value = Car.objects.aggregate(
        total_valor = Sum('value')
    )['total_valor']
    
    CarInventory.objects.create(
        cars_count = car_count,
        cars_value = car_value
    )


@receiver(pre_save, sender=Car)
def car_pre_save(sender,instance, **kwargs):
    if not instance.bio:
        instance.bio = 'Bio gerada automaticamente'
    
@receiver(post_save,sender=Car)
def car_post_save(sender,instance, **kwargs):
   car_inventory_update()
    
@receiver(post_delete,sender=Car)
def car_post_delete(sender,instance, **kwargs):
    car_inventory_update()