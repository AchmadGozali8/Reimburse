# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models
from django.contrib.auth.models import User

from managers.custom_managers import StatusDeletedModel, DateTimeHandlerModel


DELETED = 1
NOT_DELETED = 0


class Reimbursement(StatusDeletedModel, DateTimeHandlerModel):
    image = models.FileField(upload_to="img/%Y/%m/%d")
    description = models.CharField(max_length=200)
    transaction_date = models.DateTimeField(null=False)
    transaction_amount = models.CharField(max_length=40, null=False)
    deleted = models.IntegerField(default=NOT_DELETED, null=False)
    user_id = models.ForeignKey(User, on_delete = models.CASCADE,
                                db_column="user_id")
    def save(self, *args, **kwargs):
        if self.created_at is None:
            self.created_at = timezone.now()
        if self.updated_at is not None:
            self.updated_at = timezone.now()
        super(Reimbursement, self).save(*args, **kwargs)

    def __str__(self):
        return "{}".format(description)

    class Meta:
        db_table = 'reimbursement'
        ordering = ('-created_at',)
