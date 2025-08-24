import flet as ft

# -----------------------------
# 데이터 구조
# -----------------------------
class Message:
    def __init__(self, user_name: str, text: str, time: str, message_type: str, image_path: str = None):
        self.user_name = user_name
        self.text = text
        self.time = time
        self.message_type = message_type
        self.image_path = image_path  # image_message용 경로

# -----------------------------
# UI 컴포넌트
# -----------------------------
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
        return user_name[:1].capitalize() if user_name else "?"

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

class ImageMessage(ft.Row):
    def __init__(self, message: Message, image_path: str):
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
                    ft.Image(src=image_path, width=200, height=200),
                ],
                tight=True,
                spacing=5,
            ),
        ]

    def get_initials(self, user_name: str):
        return user_name[:1].capitalize() if user_name else "?"

    def get_avatar_color(self, user_name: str):
        colors_lookup = [
            ft.Colors.AMBER, ft.Colors.BLUE, ft.Colors.BROWN, ft.Colors.CYAN,
            ft.Colors.GREEN, ft.Colors.INDIGO, ft.Colors.LIME, ft.Colors.ORANGE,
            ft.Colors.PINK, ft.Colors.PURPLE, ft.Colors.RED, ft.Colors.TEAL,
            ft.Colors.YELLOW,
        ]
        return colors_lookup[hash(user_name) % len(colors_lookup)]