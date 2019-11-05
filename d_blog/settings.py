"""
Django settings for d_blog project.

Generated by 'django-admin startproject' using Django 1.11.18.

For more information on this file, see
https://docs.djangoproject.com/en/1.11/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/1.11/ref/settings/
"""

import os

# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/1.11/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'hj9mdcbr^zg8m)(bz%)0no_g-9w9dbj8idym$@fhl)jvrsswfh'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True
# DEBUG = False

ALLOWED_HOSTS = ['*']
INTERNAL_IPS = ('127.0.0.1',)

# Application definition

INSTALLED_APPS = [
    'simpleui',
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    
    'debug_toolbar',
    'corsheaders',
    'mdeditor',
    'import_export',
    'stdimage',

    'xmy',
    'blog',
    'account',
]

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',

    'debug_toolbar.middleware.DebugToolbarMiddleware',
    'corsheaders.middleware.CorsMiddleware'
]

ROOT_URLCONF = 'd_blog.urls'
AUTH_USER_MODEL = 'account.UserModel'
TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [os.path.join(BASE_DIR, 'templates')],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
            ],
        },
    },
]

WSGI_APPLICATION = 'd_blog.wsgi.application'

# Database
# https://docs.djangoproject.com/en/1.11/ref/settings/#databases

DATABASES = {
    'default': {
        # 'ENGINE': 'django.db.backends.sqlite3',
        # 'NAME': os.path.join(BASE_DIR, 'db.sqlite3'),
        'ENGINE': 'django.db.backends.mysql',
        'NAME': 'blog',
        'HOST': 'localhost',
        'USER': 'root',
        'PASSWORD': '123456',
        'PORT': 3306,
    }
}


# Password validation
# https://docs.djangoproject.com/en/1.11/ref/settings/#auth-password-validators

AUTH_PASSWORD_VALIDATORS = [
    {
        'NAME': 'django.contrib.auth.password_validation.UserAttributeSimilarityValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.MinimumLengthValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.CommonPasswordValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.NumericPasswordValidator',
    },
]


# Internationalization
# https://docs.djangoproject.com/en/1.11/topics/i18n/

LANGUAGE_CODE = 'zh-hans'

TIME_ZONE = 'Asia/Shanghai'

USE_I18N = True

USE_L10N = True

USE_TZ = False

# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/1.11/howto/static-files/


# 静态文件迁移目录
# STATIC_ROOT = os.path.join(BASE_DIR, 'static')
# django访问静态文件目录
STATICFILES_DIRS = [
    os.path.join(BASE_DIR, 'static'),
]
STATIC_URL = '/static/'

MEDIA_ROOT = os.path.join(BASE_DIR, 'media/upload')
MEDIA_URL = '/media/upload/'


CACHES = {
    'default': {
        'BACKEND': 'django_redis.cache.RedisCache',
        'LOCATION': 'redis://{}:{}/{}'.format('127.0.0.1', '6379', '1'),
        'OPTIONS': {
            'CLIENT_CLASS': 'django_redis.client.DefaultClient',
            'CONNECTION_POOL_KWARGS': {'max_connections': 100},
            # 'PASSWORD': '123456'
        }
    }
}

# 浏览器关闭,session失效
# SESSION_EXPIRE_AT_BROWSER_CLOSE = True
# session存储时间
SESSION_COOKIE_AGE = 60 * 60

DATA_UPLOAD_MAX_NUMBER_FIELDS = 5000

LOGGING = {
    'version': 1,
    'disable_existing_loggers': True,

    # 格式配置
    'formatters': {
        'simple': {
            'format': '%(asctime)s %(module)s.%(funcName)s: %(message)s',
            'datefmt': '%Y-%m-%d %H:%M:%S',
        },
        'verbose': {
            'format': ('%(asctime)s %(levelname)s [%(process)d-%(threadName)s]'
                       '%(module)s.%(funcName)s line %(lineno)d: %(message)s'),
            'datefmt': '%Y-%m-%d %H:%M:%S',
        },
    },
    # Handler 配置
    'handlers': {
        'console': {
            'class': 'logging.StreamHandler',
            'level': 'DEBUG' if DEBUG else 'ERROR'
        },
        'info': {
            'class': 'logging.handlers.TimedRotatingFileHandler',
            'filename': f'log/info.log',
            'when': 'D',  # 每天切割日志
            'backupCount': 5,  # 日志保留5天
            'formatter': 'simple',
            'level': 'INFO',
        },
        'error': {
            'class': 'logging.handlers.TimedRotatingFileHandler',
            'filename': f'log/error.log',
            'when': 'W0',
            'backupCount': 4,
            'formatter': 'verbose',
            'level': 'ERROR',
        },
        'warning': {
            'class': 'logging.handlers.TimedRotatingFileHandler',
            'filename': f'log/warning.log',
            'when': 'D',
            'backupCount': 15,
            'formatter': 'verbose',
            'level': 'WARNING',
        }

    },

    # LOGGER 配置
    'loggers': {
        'django': {
            'handlers': ['console'],
        },

        'inf': {
            'handlers': ['info'],
            'propagate': True,
            'level': 'INFO',
        },
        'err': {
            'handlers': ['error'],
            'propagate': True,
            'level': 'ERROR',
        },
        'war': {
            'handlers': ['warning'],
            'propagate': True,
            'level': 'WARNING'
        }
    }
}

# 跨域
CORS_ALLOW_CREDENTIALS = True
CORS_ORIGIN_ALLOW_ALL = True
CORS_ORIGIN_WHITELIST = ('https://*',)

CORS_ALLOW_METHODS = (
    'DELETE',
    'GET',
    'OPTIONS',
    'PATCH',
    'POST',
    'PUT',
    'VIEW',
)
CORS_ALLOW_HEADERS = (
    'XMLHttpRequest',
    'X_FILENAME',
    'accept-encoding',
    'authorization',
    'content-type',
    'dnt',
    'origin',
    'user-agent',
    'x-csrftoken',
    'x-requested-with',
)

# simpleui 配置
# simpleui隐藏服务器信息    
SIMPLEUI_HOME_INFO = False
# 关闭默认图标
SIMPLEUI_DEFAULT_ICON = False
# 自定义图标
# name	模块名字，请注意不是model的命名，而是菜单栏上显示的文本，因为model是可以重复的，会导致无法区分
# icon	图标
SIMPLEUI_ICON = {
    '相册': 'fa fa-list-ol',
    '博客管理': 'fas fa-user-tie',
    '博客': 'fas fa-book-open',
    '相册管理': 'fa fa-archive',
    '管理': 'fa fa-align-justify'
}
# 首页配置
# SIMPLEUI_HOME_PAGE = 'https://www.baidu.com'
# 首页标题
SIMPLE_HOME_TITLE = 'SamSa'
# # 首页图标,支持element-ui的图标和fontawesome的图标
SIMPLEUI_HOME_ICON = 'el-icon-date'

# 首页显示最近动作
# SIMPLEUI_HOME_ACTION = False
# 首页显示快速操作
# SIMPLEUI_HOME_QUICK = False
# 自定义SIMPLEUI的Logo
# SIMPLEUI_LOGO = 'https://avatars2.githubusercontent.com/u/13655483?s=60&v=4'
# SIMPLEUI_LOGO = ''
# 登录页粒子动画，默认开启，False关闭
# SIMPLEUI_LOGIN_PARTICLES = False
# 让simpleui 不要收集相关信息
SIMPLEUI_ANALYSIS = True
# simpleui 自定义菜单
# SIMPLEUI_CONFIG = {
# 
# }
# 评论 far fa-comments
# 指定simpleui 是否以脱机模式加载静态资源，为True的时候将默认从本地读取所有资源，即使没有联网一样可以。适合内网项目
# 不填该项或者为False的时候，默认从第三方的cdn获取
SIMPLEUI_STATIC_OFFLINE = True

# redis
REDIS = {
    'host': '127.0.0.1',
    'port': 3306,
    'db': 0
}