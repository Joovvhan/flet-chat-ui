import flet as ft
from datetime import datetime

def main(page: ft.Page):
    page.horizontal_alignment = ft.CrossAxisAlignment.STRETCH
    page.title = "Flet Fake Chat"

    # Chat messages
    chat = ft.ListView(
        expand=True,
        spacing=10,
        auto_scroll=True,
    )

    # 가상의 메시지 데이터
    fake_messages = [
        {"user_name": "Alice", "text": "안녕! 오늘 기분 어때?", "time": "10:00", "type": "chat_message"},
        {"user_name": "Bob", "text": "좋아! 너는?", "time": "10:01", "type": "chat_message"},
        {"user_name": "Alice", "text": "나도 좋아 😄", "time": "10:02", "type": "chat_message"},
        {"user_name": "Charlie", "text": "다들 점심 뭐 먹었어?", "time": "10:03", "type": "chat_message"},
        {"user_name": "Bob", "text": "피자 먹었어 🍕", "time": "10:04", "type": "chat_message"},
    ]

    # ChatMessage 클래스 재사용
    class Message:
        def __init__(self, user_name: str, text: str, time: str, message_type: str):
            self.user_name = user_name
            self.text = text
            self.time = time
            self.message_type = message_type

    class ChatMessage(ft.Row):
        def __init__(self, message: Message):
            super().__init__()
            self.vertical_alignment = ft.CrossAxisAlignment.START
            self.controls = [
                ft.CircleAvatar(
                    content=ft.Text(self.get_initials(message.user_name)),
                    color=ft.Colors.WHITE,
                    bgcolor=self.get_avatar_color(message.user_name),
                ),
                ft.Column(
                    [
                        ft.Row([
                            ft.Text(message.user_name, weight="bold"),
                            ft.Text(message.time, size=10, color=ft.Colors.BLACK45),
                        ], alignment=ft.MainAxisAlignment.SPACE_BETWEEN),
                        ft.Text(message.text, selectable=True),
                    ],
                    tight=True,
                    spacing=5,
                ),
            ]

        def get_initials(self, user_name: str):
            if user_name:
                return user_name[:1].capitalize()
            else:
                return "?"

        def get_avatar_color(self, user_name: str):
            colors_lookup = [
                ft.Colors.AMBER,
                ft.Colors.BLUE,
                ft.Colors.BROWN,
                ft.Colors.CYAN,
                ft.Colors.GREEN,
                ft.Colors.INDIGO,
                ft.Colors.LIME,
                ft.Colors.ORANGE,
                ft.Colors.PINK,
                ft.Colors.PURPLE,
                ft.Colors.RED,
                ft.Colors.TEAL,
                ft.Colors.YELLOW,
            ]
            return colors_lookup[hash(user_name) % len(colors_lookup)]

    # 가짜 메시지 추가
    for m in fake_messages:
        chat.controls.append(ChatMessage(Message(m["user_name"], m["text"], m["time"], m["type"])))

    # 메시지 입력창
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

ft.app(target=main)