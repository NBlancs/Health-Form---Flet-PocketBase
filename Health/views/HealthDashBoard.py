import flet as ft
import flet as ft
from views.AppPage import AppPage

class DashBoard (AppPage):

    def __init__(self, root, route):
        super().__init__(root=root, route=route)

    def get_page(self) -> ft.View:

        self.page.controls = [
            ft.AppBar(bgcolor="green",leading=ft.Icon(ft.icons.LOCAL_HOSPITAL),
                      leading_width=40,
                      title=ft.Text('𝖡𝖫𝖠𝖭𝖢𝖮 𝖧𝖮𝖲𝖯𝖨𝖳𝖠𝖫'),
                      center_title=False,
                      actions=[
                          ft.PopupMenuButton(items=[
                              ft.PopupMenuItem(text="Logout",on_click=lambda _: self.root.go('/'))

                          ])
                      ]
                    ),
            ft.Card(
            content=ft.Container(
                content=ft.Column(
                    [
                        ft.ListTile(
                            leading=ft.Icon(ft.icons.LOCAL_HOSPITAL,color='green'),
                            title=ft.Text("COMMANDS"),
                        ),
                        ft.Row(
                            [ft.TextButton("View Forms",icon='remove_red_eye',icon_color="green",on_click=lambda _: self.root.go('/hist'))],
                            alignment=ft.MainAxisAlignment.START,
                        ),
                        ft.Row(
                            [ft.TextButton("Remove Forms",icon='delete',icon_color="green",on_click=lambda _: self.root.go('/del'))],
                            alignment=ft.MainAxisAlignment.START,
                        ),                               
                        ft.Row(
                            [ft.TextButton("Update Forms",icon='edit',icon_color="green",on_click=lambda _: self.root.go('/upt'))],
                            alignment=ft.MainAxisAlignment.START,
                        ),                                           
                    ]
                ),
                width=400,
                padding=10,
            ), 
        ),        
    ]
        
        return self.page

    def did_mount(self):
        pass



