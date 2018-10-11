"""
Django settings for DRF project.

Generated by 'django-admin startproject' using Django 2.1.1.

For more information on this file, see
https://docs.djangoproject.com/en/2.1/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/2.1/ref/settings/
"""

import os
import acm


# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/2.1/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'i!@*c7n&^uyp0pn2ngunkei(hf_*sgww(=#98t!_m3j)!4xy+3'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

ALLOWED_HOSTS = []

# Application definition

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'rest_framework',
    'celery',
    'hqq_user.apps.HqqUsersConfig',
    'topic.apps.TopicConfig',
    'friend.apps.FriendConfig',
    'group.apps.GroupConfig',
    'notice.apps.NoticeConfig',
    'forum.apps.ForumConfig',
    'report.apps.ReportConfig',
    'hqq_tool.apps.HqqToolConfig',

]

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

ROOT_URLCONF = 'DRF.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [os.path.join(BASE_DIR, 'templates')]
        ,
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

WSGI_APPLICATION = 'DRF.wsgi.application'


# Database
# https://docs.djangoproject.com/en/2.1/ref/settings/#databases
# ==============acm==================
# acm proporties
ENDPOINT = "acm.aliyun.com:8080"
NAMESPACE = "520a608f-cf8e-4769-99a4-aa09b4397088"
AK = "LTAIbIchC6epwWTO"
SK = "cpIAKyNPnbwACvuU303gKeqAUXVIFM"

# get config
client = acm.ACMClient(ENDPOINT, NAMESPACE, AK, SK)
data_id = "local_db_2"
group = "DEFAULT_GROUP"
db_info = client.get(data_id, group, timeout=30, no_snapshot=True)
db_info = db_info.replace('\r\n', ':')
db_info = db_info.split(':')
# add watch
# import time
# client.add_watcher(data_id, group, lambda x: print("config change detected: " + x))
# time.sleep(5)  # wait for config changes
# ==============acm==================
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'NAME': db_info[db_info.index('NAME') + 1],
        'USER': db_info[db_info.index('USER') + 1],
        'PASSWORD': db_info[db_info.index('PASSWORD') + 1],
        'HOST': db_info[db_info.index('HOST') + 1],
        'PORT': db_info[db_info.index('PORT') + 1],
    }
}


# Password validation
# https://docs.djangoproject.com/en/2.1/ref/settings/#auth-password-validators

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
# https://docs.djangoproject.com/en/2.1/topics/i18n/

LANGUAGE_CODE = 'zh-hans'   # 使用中文

TIME_ZONE = 'Asia/Shanghai'

USE_I18N = True

USE_L10N = True

USE_TZ = False



# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/2.1/howto/static-files/

STATIC_URL = '/static/'


REST_FRAMEWORK = {
    'DEFAULT_PERMISSION_CLASSES': [
        # 'rest_framework.permissions.IsAdminUser',
    ],
    'DEFAULT_AUTHENTICATION_CLASSES': [
        # 'rest_framework.authentication.BasicAuthentication',
        # 'rest_framework.authentication.TokenAuthentication', # 系统已有的
    ],
    # 'DEFAULT_RENDERER_CLASSES': [
    #     'rest_framework.renderers.JSONRenderer',
    # ],
    # 'DEFAULT_PARSER_CLASSES': [
    #     'rest_framework.parsers.JSONParser',
    # ],
    'PAGE_SIZE': 10
}

LOGGING = {
    'version': 1,
    'disable_existing_loggers': False,
    'handlers': {
        'console': {
            'level': 'INFO',
            'class': 'logging.StreamHandler',
        },
    },
    'loggers': {
        'django.db.backends': {
            'handlers': ['console'],
            'propagate': True,
            'level': 'DEBUG',
        },
    }
}


# CELERY_FORCE_EXECV = True  # 避免某些死锁

# CELERY_ACKS_LATE = True  # 出错之后允许重试

# CELERY_MAX_TASKS_PER_CHILD = 100  # 每个worker最多执行100个任务之后就会被销毁

# CELERY_TASK_TIME_LIMIT = 每个任务最多运行多少秒




# CELERY_BROKER = 'redis'

# redis://:password@hostname:port/db_number
CELERY_BROKER_URL = 'redis://39.105.97.242:6379/1'

# 可见性超时时间定义了等待职程在消息分派到其他职程之前确认收到任务的秒数
# CELERY_BROKER_TRANSPORT_OPTIONS = {'visibility_timeout': 3600}  # 1 hour.

# 在 Redis 中存储任务的状态和返回值
CELERY_RESULT_BACKEND = 'redis://39.105.97.242:6379/2'
#
# CELERY_TASK_ROUTES = {
#     'hqq_user.tasks.*': {
#         'queue': 'user_queue'
#     }
# }

# CELERY_TASK_DEFAULT_QUEUE = 'work_queue'
#
task_serializer = 'pickle'
