from django.db import models

# Create your models here.

class Category (models.Model):
    name = models.CharField(max_length=255, verbose_name="Nomi")

    class Meta:
        verbose_name = "Kategoriya"
        verbose_name_plural = "Kategoriyalar"

    def __str__(self):
        return self.name

class Todo (models.Model):
    category = models.ForeignKey(Category, on_delete=models.CASCADE, verbose_name = "Kategoriya")
    task_name = models.CharField(max_length=255, verbose_name = "Vazifa nomi")
    completed = models.BooleanField(default=False, verbose_name ="Bajarilganmi")
    description = models.TextField(null=True, verbose_name="Tavsifi")
    notify_text = models.TextField(null=True, blank=True, verbose_name="Eslatma matn")

    class Meta:
        verbose_name = "Vazifa"
        verbose_name_plural = "Vazifalar"

    def __str__(self):
        return self.task_name
   
