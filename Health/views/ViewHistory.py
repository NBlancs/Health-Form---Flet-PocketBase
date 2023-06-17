import flet as ft
import flet as ft
from views.AppPage import AppPage
from controller.HistoryController import get_hist

class History (AppPage):

    def __init__(self, root, route):
        super().__init__(root=root, route=route)

    def get_page(self) -> ft.View:

        self.hist = ft.ListView()

        self.page.controls = [
            ft.AppBar(bgcolor="green",leading=ft.Icon(ft.icons.LOCAL_HOSPITAL),
                      leading_width=40,
                      title=ft.Text('𝖯𝖠𝖳𝖨𝖤𝖭𝖳 𝖥𝖮𝖱𝖬𝖲'),
                      center_title=False,
                      actions=[
                          ft.PopupMenuButton(items=[
                              ft.PopupMenuItem(text="Dashboard",on_click=lambda _: self.root.go('/dash')),                                                         
                              ft.PopupMenuItem(text="Update Forms",on_click=lambda _: self.root.go('/upt')),
                              ft.PopupMenuItem(text="Delete Forms",on_click=lambda _: self.root.go('/del')),
                              ft.PopupMenuItem(text="Logout",on_click=lambda _: self.root.go('/')),  
                          ]
                        )
                      ]
                    ),

            ft.Card(
            content=ft.Container(
                content=ft.Column(
                    [
                        ft.ListTile(
                            leading=ft.Icon(ft.icons.LIST),
                            title=ft.Text("Form List"),
                        ),                            
                        self.history()    
                    ]
                ),
                expand=True,
                padding=10,
            )
        ),
         
        ]
        return self.page

    def history(self):
        for i in get_hist():
            self.hist.controls.append(ft.Container(content=ft.Row([                              
            ft.DataTable(   
                expand=True,            
                bgcolor="green",
                border=ft.border.all(2, "black"),
                border_radius=10,
                vertical_lines=ft.border.BorderSide(3, "blue"),
                horizontal_lines=ft.border.BorderSide(1, "blue"),
                heading_row_color=ft.colors.BLACK12,
                data_row_color={"hovered": "0x30FF0000"},
                divider_thickness=0,
                column_spacing=25,
                columns=[
                    ft.DataColumn(ft.Text('Name')),
                    ft.DataColumn(ft.Text('Blood Type')),
                    ft.DataColumn(ft.Text('Gender')),
                    ft.DataColumn(ft.Text('Birth Date')),
                    ft.DataColumn(ft.Text('Age')),
                    ft.DataColumn(ft.Text('Health Problems')),
                    ft.DataColumn(ft.Text('Current Medicines')),
                    ft.DataColumn(ft.Text('Weight(kg)')),
                    ft.DataColumn(ft.Text('Height(M)')),
                    ft.DataColumn(ft.Text('BMI'))
                ],
                rows=[
                    ft.DataRow(
                cells=[
                    ft.DataCell(ft.Text(i.name)),
                    ft.DataCell(ft.Text(i.blood_type)),
                    ft.DataCell(ft.Text(i.gender)),
                    ft.DataCell(ft.Text(i.birth_date)),
                    ft.DataCell(ft.Text(i.age)),
                    ft.DataCell(ft.Text(i.health_problems)),
                    ft.DataCell(ft.Text(i.current_medicines)),
                    ft.DataCell(ft.Text(i.weight)),
                    ft.DataCell(ft.Text(i.height)),
                    ft.DataCell(ft.Text(i.bmi)),
                 ]
                )
              ]
            )
           ]
          )
         )
        ) 
        return self.hist

    def did_mount(self):
        pass