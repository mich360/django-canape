# myapp/my_custom_startup_handler.py

import asyncio

async def my_custom_startup_handler():
    # 開始時のカスタム処理をここに追加
    await asyncio.sleep(1)  # 例: 開始時に1秒待つ
    print("Custom startup handler executed")
