# -*- coding: utf-8 -*-
# @Author  : SamSa
from django.conf import settings

RANK_ARTICLE = '%s%s' % (settings.SECRET_KEY, 'rank_article')

# 登陆url
LOGIN_URL = '/admin/login'
SERVER_ERROR = 500
