# myapp/my_custom_shutdown_handler.py

import asyncio

async def my_custom_shutdown_handler():
    # 終了時のカスタム処理をここに追加
    await asyncio.sleep(1)  # 例: 終了時に1秒待つ
    print("Custom shutdown handler executed")
