from PIL import Image
from django.db import models
from django.db.transaction import atomic

from users.choices import GENDER_CHOICES, EDUCATION_CHOICES
# import CustomUser instead of get_user_model because CustomUser
# is not initialized yet and get_user_model cannot return CustomUser
from users.models.custom_user import CustomUser
from users.validators import PValidationError

__all__ = ['Profile', 'Role']


class Role(models.Model):
    name = models.CharField(max_length=20)

    def __str__(self):
        return f'{self.name}'

    class Meta:
        db_table = "roles"


class Profile(models.Model):
    """
    date_of_birth, experience, gender and education are nullable
    in case we will use oauth2 and cannot automatically take this data

    user can change the data in profile page

    Django forms and serializer do not allow you to leave data empty.
    """
    user = models.OneToOneField(CustomUser, on_delete=models.CASCADE,
                                db_column='user_id')
    role = models.ForeignKey(Role, on_delete=models.PROTECT,
                             db_column='role_id')
    image = models.ImageField(upload_to='profile_pics',
                              blank=True, null=True)
    date_of_birth = models.DateField(null=True)
    experience = models.IntegerField(null=True)
    gender = models.CharField(choices=GENDER_CHOICES, max_length=20, null=True)
    education = models.CharField(choices=EDUCATION_CHOICES, max_length=50,
                                 null=True)

    @atomic
    def save(self, **kwargs):
        """
        if img is too big we decrease img
        because the less image is the less memory it takes
        """
        try:
            super(Profile, self).save(**kwargs)
            if self.image:
                img = Image.open(self.image.path)
                if img.height > 300 or img.width > 300:
                    output_size = (300, 300)
                    img.thumbnail(output_size)
                    img.save(self.image.path)
        except (OSError, IOError):
            self.image = None
            super(Profile, self).save(update_fields=['image'])
            raise PValidationError('Image can`t be saved')

    def __str__(self):
        return f'{self.user.username} => {self.role.name}'

    class Meta:
        db_table = "profiles"