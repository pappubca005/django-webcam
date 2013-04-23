# -*- coding: utf-8 -*-
import random
from django.db import models
from webcam.fields import CameraPictureField
from webcam.tests import temp_storage


class FSDemoModel(models.Model):
    photo = CameraPictureField('CameraPictureField', format='jpeg', null=True, blank=True,
                               storage=temp_storage, upload_to='tests')

    class Meta:
        app_label = 'webcam'
