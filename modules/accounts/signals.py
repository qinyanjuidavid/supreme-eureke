from django.contrib.auth import get_user_model
from django.db.models.signals import post_save, pre_save
from django.dispatch import receiver

from modules.accounts.models import Constants, RoleChoices, SuperUser, TrackingModel

User = get_user_model()


@receiver(post_save, sender=User)
def create_user_profiles(sender, instance, created, **kwargs):
    """
    Signal receiver function to create user profiles
    when a new user is created.
    """
    if created:
        profile_models = {
            RoleChoices.SUPERUSER: SuperUser,
        }

        if instance.is_superuser or instance.is_staff:
            profile_model = SuperUser
        else:
            profile_model = profile_models.get(instance.role)

        # Create the profile
        profile_model.objects.get_or_create(user=instance)
        if profile_model:
            profile_model.objects.get_or_create(user=instance)


@receiver(pre_save)
def set_updated_flag(sender, instance, **kwargs):
    """
    Signal handler to set the updated_flag field before saving the object.

    Args:
        sender (Type): The model class.
        instance: The instance of the model.
        **kwargs: Additional keyword arguments passed to the function.
    """
    if isinstance(instance, TrackingModel) and not instance._state.adding:
        instance.updated_flag = Constants.YES
