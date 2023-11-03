"""
ASGI config for main project.

It exposes the ASGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/4.2/howto/deployment/asgi/
"""

import os

from django.core.asgi import get_asgi_application

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'main.settings')

application = get_asgi_application()
# 追加

from myapp import my_custom_startup_handler, my_custom_shutdown_handler

# ASGIアプリケーションを取得
django_asgi_app = get_asgi_application()

# ライフサイクルハンドラを追加
async def application(scope, receive, send):
    if scope['type'] == 'lifespan':
        if scope['asgi']['type'] == 'startup':
            await my_custom_startup_handler()  # 開始時の処理
        elif scope['asgi']['type'] == 'shutdown':
            await my_custom_shutdown_handler()  # 終了時の処理
    else:
        await django_asgi_app(scope, receive, send)

# UvicornでASGIアプリケーションを起動
