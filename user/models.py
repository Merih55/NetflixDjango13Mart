from django.db import models
from django.contrib.auth.models import User
# rastgele id için
import uuid

from django.utils.text import slugify
#pillow pip install Pillow
class Profile(models.Model):
    id = models.UUIDField(primary_key=True, db_index=True, default=uuid.uuid4, editable=False)
    user = models.ForeignKey(User, on_delete=models.CASCADE, verbose_name='Kullanıcı')
    isim = models.CharField(max_length=100)
    resim = models.ImageField(upload_to= 'profiller/')
    olusturulma_tarihi = models.DateField(auto_now_add=True, null=True)
    slug = models.SlugField(null=True, editable=False)

    def __str__(self):
        return self.isim
    
    def save(self, *args, **kwargs):
        self.slug = slugify(self.isim)# + '-' + str(self.id)[:10])
        super().save(*args,**kwargs)