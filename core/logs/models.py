# from django.db import models
# from profiles.models import profile
# # Create your models here.

# class log(models.Model):
#     profile = models.ForeignKey(profile, on_delete=models.CASCADE, blank=True, null=True)
#     photo = models.ImageField(upload_to='logs')
#     is_correct = models.BooleanField(default=False)
#     created = models.DateTimeField(auto_now_add=True)

#     # def __str__(self):
#     #     return f"log of {self.profile.id}"
#     def __str__(self):
#         return str(self.id)
