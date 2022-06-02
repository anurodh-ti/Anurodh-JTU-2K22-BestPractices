# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models

# Create your models here.
from django.contrib.auth.models import User
from restapi.constants import *


class Category(models.Model):
    name = models.CharField(max_length=CATEGORY_NAME_MAX_LENGTH, null=False)


class Groups(models.Model):
    name = models.CharField(max_length=GROUP_NAME_MAX_LENGTH, null=False)
    members = models.ManyToManyField(User, related_name='members', blank=True)


class Expenses(models.Model):
    description = models.CharField(max_length=EXPENSE_DESC_MAX_LENGTH)
    total_amount = models.DecimalField(max_digits=EXPENSE_MAX_DIGITS, decimal_places=EXPENSE_DECIMAL_PLACES)
    group = models.ForeignKey(Groups, null=True, on_delete=models.CASCADE)
    category = models.ForeignKey(Category, default=EXPENSES_CATEGORY_DEFAULT, on_delete=models.CASCADE)


class UserExpense(models.Model):
    expense = models.ForeignKey(Expenses, default=1, on_delete=models.CASCADE, related_name="users")
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name="expenses")
    amount_owed = models.DecimalField(max_digits=USER_EXPENSE_MAX_DIGITS, decimal_places=USER_EXPENSE_DECIMAL_PLACES)
    amount_lent = models.DecimalField(max_digits=USER_EXPENSE_MAX_DIGITS, decimal_places=USER_EXPENSE_DECIMAL_PLACES)

    def __str__(self):
        return f"user: {self.user}, amount_owed: {self.amount_owed} amount_lent: {self.amount_lent}"
