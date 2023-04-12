from django.db import models
from datetime import date, datetime


class Language(models.Model):
    name = models.CharField(max_length=20)
    month_to_learn = models.IntegerField()

    def save(self, *args, **kwargs):
        super().save(*args, **kwargs)
        return self.name.title()
        print('Успешно')

    def __str__(self):
        return f'{self.name} -- {self.month_to_learn}'


class AbstractPerson(models.Model):
    name = models.CharField(max_length=20)
    email = models.EmailField()
    phone_number = models.CharField(max_length=14)

    class Meta:
        abstract = True
        ordering = ['name', ]

    def save(self, *args, **kwargs):
        if self.phone_number.startswith('0704110406'):
            self.phone_number = '+996704110406'
        super().save(*args, **kwargs)
        print('Успешно')

    def __str__(self):
        return self.save()


class Student(AbstractPerson):
    work_study_place = models.CharField(max_length=20, null=True, blank=True)
    has_own_notebook = models.BooleanField()
    preffered_os = models.IntegerField(verbose_name='Выборка', choices=(
        (1, "Windows"),
        (2, "MacOS"),
        (3, "Linux"),
    ))

    class Meta(AbstractPerson.Meta):
        pass

    def __str__(self):
        return f' {self.name} - {self.work_study_place} - {self.has_own_notebook} - {self.phone_number}'


class Mentor(AbstractPerson):
    main_work = models.CharField(max_length=50, null=True, blank=True)
    experience = models.DateField()
    students = models.ManyToManyField(Student, related_name='students', through='Course')

    def __str__(self):
        return f'{self.name} - {self.email} - {self.phone_number} -{self.main_work} - {self.experience} '


class Course(models.Model):
    name = models.CharField(max_length=20)
    language = models.ForeignKey(Language, on_delete=models.CASCADE)
    date_started = models.DateField()
    mentor = models.ForeignKey(Mentor, on_delete=models.CASCADE)
    student = models.ForeignKey(Student, on_delete=models.CASCADE)

    def get_end_date(self):
        days_completed = date.today() - self.date_started
        days_left = int(days_completed.days / 30) - self.language.month_to_learn
        return f'{days_left} months is left'

    def __str__(self):
        return f'Имя курса:{self.name} / Язык:{self.language} / Студент: {self.student}/ Начало курса: {self.date_started}/ Осталось: {self.get_end_date()} '
