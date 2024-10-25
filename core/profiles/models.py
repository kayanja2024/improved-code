# from django.db import models
# from django.contrib.auth.models import User
# # Create your models here.

# class profile(models.Model):
#     user = models.OneToOneField(User, on_delete=models.CASCADE)
#     photos = models.ImageField(upload_to='photos', blank=True, null=True)
#     bio = models.TextField()
#     created = models.DateTimeField(auto_now_add=True)

#     def __str__(self):
#         return f"profile of {self.user.username}"

