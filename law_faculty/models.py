from django.db import models
from django.utils import timezone

class Department(models.Model):
    name = models.CharField(max_length=255, verbose_name="Назва кафедри")
    head = models.CharField(max_length=255, verbose_name="Завідувач кафедри")

    def __str__(self):
        return self.name

class Program(models.Model):
    name = models.CharField(max_length=255, verbose_name="Назва спеціальності")
    code = models.CharField(max_length=50, verbose_name="Код спеціальності")
    description = models.TextField(verbose_name="Повний опис")
    coordinator_name = models.CharField(max_length=255, verbose_name="Імʼя координатора")
    coordinator_contact = models.CharField(max_length=255, verbose_name="Контакт координатора")
    department = models.ForeignKey(Department, on_delete=models.CASCADE, related_name="programs", verbose_name="Випускова кафедра")
    disciplines = models.TextField(verbose_name="Список дисциплін")

    def __str__(self):
        return f"{self.code} {self.name}"
    
    @property
    def short_description(self):
        words = self.description.split()
        return " ".join(words[:50]) + ("..." if len(words) > 50 else "")

class Teacher(models.Model):
    name = models.CharField(max_length=255, verbose_name="Імʼя викладача")
    position = models.CharField(max_length=255, verbose_name="Посада")
    degree = models.CharField(max_length=255, verbose_name="Науковий ступінь")
    department = models.ForeignKey(Department, on_delete=models.CASCADE, related_name="teachers", verbose_name="Кафедра")

    def __str__(self):
        return f"{self.name} ({self.degree})"

class Specialty(models.Model):
    name = models.CharField(max_length=255, verbose_name="Назва спеціальності")
    code = models.CharField(max_length=50, verbose_name="Код спеціальності")
    description = models.TextField(verbose_name="Повний опис")
    department = models.ForeignKey(Department, on_delete=models.CASCADE, related_name="specialties", verbose_name="Випускова кафедра")
    coordinator_name = models.CharField(max_length=255, verbose_name="Ім'я координатора набору", blank=True, null=True)
    coordinator_contacts = models.CharField(max_length=255, verbose_name="Контакт координатора набору", blank=True, null=True)
    disciplines = models.TextField(verbose_name="Список дисциплін", blank=True, null=True)

    def __str__(self):
        return f"{self.code} {self.name}"
    
    @property
    def short_description(self):
        words = self.description.split()
        return " ".join(words[:50]) + ("..." if len(words) > 50 else "")

class ExchangeProgram(models.Model):
    university = models.CharField(max_length=255, verbose_name="Університет")
    languages = models.CharField(max_length=255, verbose_name="Мови навчання")
    slots = models.PositiveIntegerField(verbose_name="Кількість місць", default=1)
    deadline = models.DateField(verbose_name="Дедлайн подачі")
    description = models.TextField(verbose_name="Опис")
    country = models.CharField(max_length=100, verbose_name="Країна", blank=True, null=True)

    def __str__(self):
        return f"{self.university} ({self.country})"

    @property
    def is_active(self):
        #Повертає True, якщо дедлайн ще не минув (прийом триває)
        return self.deadline >= timezone.now().date()