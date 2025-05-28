from django.db.models.signals import pre_save, post_save
from django.dispatch import receiver
from .models import Blog
from django.core.mail import send_mail

@receiver(pre_save,sender = Blog)
def before_save(sender,instance,**kwargs):
    print("Bazaga malumot qoshilishidan oldin:",instance)

@receiver(post_save,sender = Blog)
def after_save(sender,instance,created,**kwargs):
    if created:
        send_mail(
            subject="Hello from Django",
            message="This is a test email",
            from_email="abdullokh.akromov@gmail.com",
            recipient_list=['abdullokh.akromov@gmail.com','abdullokh.it@gmail.com'],
            fail_silently=False,
        )
    #     print("Bazaga malumot qoshildi:",instance)
    # else:
    #     print("Bor malumot yangilandi:",instance)