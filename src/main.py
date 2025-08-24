import flet as ft
import asyncio
import json

from utils import Message, ChatMessage, ImageMessage

def load_messages_from_jsonl(path="./storage/data/messages.jsonl"):
    messages = []
    with open(path, "r", encoding="utf-8") as f:
        for line in f:
            data = json.loads(line)
            messages.append(
                Message(
                    user_name=data.get("user_name", ""),
                    text=data.get("text", ""),
                    time=data.get("time", ""),
                    message_type=data.get("type", "chat_message"),
                    image_path=data.get("image_path")  # 없으면 None
                )
            )
    return messages


# -----------------------------
# 메인 UI
# -----------------------------
def main(page: ft.Page):

    page.window.width = 600
    page.window.height = 800
    page.window.resizable = False
    page.update()
    
    page.horizontal_alignment = ft.CrossAxisAlignment.STRETCH
    page.title = "Chat UI Example"

    chat = ft.ListView(
        expand=True,
        spacing=10,
        auto_scroll=True,
    )

    new_message = ft.TextField(
        hint_text="Write a message...",
        autofocus=True,
        shift_enter=True,
        min_lines=1,
        max_lines=5,
        filled=True,
        expand=True,
    )

    page.add(
        ft.Container(
            content=chat,
            border=ft.border.all(1, ft.Colors.OUTLINE),
            border_radius=5,
            padding=10,
            expand=True,
        ),
        ft.Row([new_message])
    )

    async def play_fake_chat():
        messages = load_messages_from_jsonl()
        for m in messages:
            if m.message_type == "chat_message":
                chat.controls.append(ChatMessage(m))
            elif m.message_type == "image_message":
                chat.controls.append(ImageMessage(m, m.image_path))
            else:
                continue  # 알 수 없는 타입은 무시

            page.update()
            await asyncio.sleep(1.5)  # 메시지 간 간격

    page.run_task(play_fake_chat)


# 실행
# ft.app(target=main)
ft.app(target=main, view=ft.AppView.FLET_APP)
