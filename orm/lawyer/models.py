from django.db import models


class CasesType(models.Model):
    type = models.CharField(max_length=255, unique=True, verbose_name='Тип дела')

    def __str__(self):
        return self.type

    class Meta:
        verbose_name = 'Тип дела'
        verbose_name_plural = 'Тип дела'
        ordering = ['id']


class Scope(models.Model):
    type = models.CharField(max_length=255, unique=True, verbose_name='Cпециализация')

    def __str__(self):
        return self.type

    class Meta:
        verbose_name = 'Специализация'
        verbose_name_plural = 'Специализации'
        ordering = ['id']


class Clients(models.Model):
    f_name = models.CharField(max_length=20, verbose_name='Имя')
    m_name = models.CharField(max_length=20, null=True, verbose_name='Отчество')
    l_name = models.CharField(max_length=20, verbose_name='Фамилия')
    passport = models.CharField(max_length=50, unique=True, verbose_name='Серия и номер паспорта')
    tel = models.IntegerField(verbose_name='Номер телефона')

    def __str__(self):
        return f'{str(self.f_name)} {str(self.m_name)}'

    class Meta:
        verbose_name = 'Клиент'
        verbose_name_plural = 'Клиенты'
        ordering = ['l_name']


class Lawyers(models.Model):
    f_name = models.CharField(max_length=20, verbose_name='Имя')
    m_name = models.CharField(max_length=20, null=True, verbose_name='Отчество')
    l_name = models.CharField(max_length=20, verbose_name='Фамилия')
    id_scope = models.ForeignKey(Scope, on_delete=models.PROTECT, verbose_name='Специализация')
    free = models.BooleanField(default=False, verbose_name='Занятость')

    def __str__(self):
        return f'{str(self.f_name)} {str(self.m_name)}'

    class Meta:
        verbose_name = 'Адвокат'
        verbose_name_plural = 'Адвокаты'
        ordering = ['l_name']


class Services(models.Model):
    type = models.CharField(max_length=255, verbose_name='Услуга')
    cost = models.IntegerField(verbose_name='Цена')

    def __str__(self):
        return self.type

    class Meta:
        verbose_name = 'Услуга'
        verbose_name_plural = 'Услуги'
        ordering = ['id']


class Cases(models.Model):
    name = models.CharField(max_length=30, verbose_name='Название')
    content = models.TextField(blank=True, verbose_name='Материалы дела')
    date = models.DateTimeField(auto_now_add=True, verbose_name='Дата создания')
    id_client = models.ForeignKey(Clients, on_delete=models.PROTECT, verbose_name='Клиент')
    id_lawyer = models.ForeignKey(Lawyers, on_delete=models.PROTECT, verbose_name='Адвокат')
    id_service = models.ForeignKey(Services, on_delete=models.PROTECT, verbose_name='Услуга')
    id_case_type = models.ForeignKey(CasesType, on_delete=models.PROTECT, verbose_name='Тип дела')

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Дело'
        verbose_name_plural = 'Дела'
        ordering = ['name']


class Registration(models.Model):
    id_client = models.ForeignKey(Clients, on_delete=models.PROTECT, verbose_name='Клиент')
    id_lawyer = models.ForeignKey(Lawyers, on_delete=models.PROTECT, verbose_name='Адвокат')
    id_service = models.ForeignKey(Services, on_delete=models.PROTECT, verbose_name='Услуга')
    id_case_type = models.ForeignKey(CasesType, on_delete=models.PROTECT, verbose_name='Тип дела')
    date = models.DateTimeField(verbose_name='Дата записи')

    def __str__(self):
        return self.id_client

    class Meta:
        verbose_name = 'Регистрация'
        verbose_name_plural = 'Регистрация'
        ordering = ['date']
