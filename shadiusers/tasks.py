from celery import shared_task
from shadiusers.models import Subscribe
from django.utils import timezone

@shared_task
def delete_expired_subscriptions():
    expired_subscriptions = Subscribe.objects.filter(expiry_date__lt=timezone.now())
    for subscription in expired_subscriptions:
        subscription.delete()
    print('Expired subscriptions deleted successfully.')