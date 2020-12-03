#!/usr/bin/env python30
# -*- coding: utf-8 -*-

import os
from django.core.mail import send_mail

os.environ['DJANGO_SETTINGS_MODULE'] = 'mysite.settings'

if __name__ == '__main__':
    send_mail(
        '测试邮件',
        '欢迎使用测试资产管理系统',
        'tianyaqiang1990@sina.com',
        ['505165956@qq.com']
    )