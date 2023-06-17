import flet as ft
import flet as ft
from views.AppPage import AppPage
from controller.AuthController import login
from pocketbase.utils import ClientResponseError

class LoginPage (AppPage):
    username = ft.Ref[ft.TextField]()
    password = ft.Ref[ft.TextField]()

    def __init__(self, root, route):
        super().__init__(root=root, route=route)
        self.page.vertical_alignment = ft.MainAxisAlignment.CENTER
        self.page.horizontal_alignment = ft.CrossAxisAlignment.CENTER
        self.page.did_mount = self.did_mount

    def did_mount(self):
        self.username.current.value = 'admin'
        self.password.current.value = '1234567890'

    def get_page(self,) -> ft.View:
        self.page.controls = [
            ft.Image(src="https://cdn-icons-png.flaticon.com/512/4320/4320350.png", width=100, height=100),
            ft.Text("𝗔𝗨𝗧𝗛𝗘𝗡𝗧𝗜𝗖𝗔𝗧𝗜𝗢𝗡",size=24),
            ft.TextField(
                ref=self.username,
                label="Username",
                width=500,
                prefix_icon=ft.icons.PERSON
            ),
            ft.TextField(
                ref=self.password,
                password=True,
                can_reveal_password=True,
                label="Password",
                width=500,
                prefix_icon=ft.icons.PASSWORD
            ),
            ft.Container(height=32),
            ft.FilledButton(
                text="LOGIN",
                on_click=self.on_login,
                width=500
            )
        ]

        return self.page

    def on_login(self, _):
        try:
            login(username=self.username.current.value,
                  password=self.password.current.value)
            self.root.go(route='/dash')
        except ClientResponseError:
            ok = ft.Ref[ft.TextButton]()
            dialog = ft.AlertDialog(
                modal=True, content=ft.Text('Username or password not found'),
                actions=[
                    ft.TextButton('OK', ref=ok)
                ]
            )

            def on_close(_):
                dialog.open = False
                self.root.update()
            ok.current.on_click = on_close

            self.root.dialog = dialog
            dialog.open = True
            self.root.update()
