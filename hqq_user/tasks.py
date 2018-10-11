# -*- coding: utf-8 -*-
# __author__= "Ruda"
# Data: 2018/10/3

from __future__ import absolute_import, unicode_literals
from celery import shared_task
from celery.task import Task
import time

from hqq_user import models


@shared_task
def save_verify_code(verify_code, phone):
    return_info = models.VerifyCode.objects.update_or_create(defaults={"code": verify_code, "phone": phone})
    return str(return_info)


@shared_task
class CourseTask(Task):
    name = 'course-task'

    def run(self, *args, **kwargs):
        print('Start Task!')
        time.sleep(4)
        print('End Task!')


@shared_task
def add(x, y):
    print('Start Task!')
    time.sleep(4)
    print('End Task!')
    return x + y, 'aaa'


@shared_task
def mul(x, y):
    return x * y


@shared_task
def xsum(numbers):
    return sum(numbers)
