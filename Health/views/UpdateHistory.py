import flet as ft
import flet as ft
from views.AppPage import AppPage
from controller.FormController import update_form
from controller.HistoryController import get_hist
from controller.HistoryController import update_patient


class UpdateHistory (AppPage):

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
                              ft.PopupMenuItem(text="View Forms",on_click=lambda _: self.root.go('/hist')),
                              ft.PopupMenuItem(text="Delete Forms",on_click=lambda _: self.root.go('/del')),
                              ft.PopupMenuItem(text="Logout",on_click=lambda _: self.root.go('/'))                              
                          ])
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
        # Required
        return self.page

    def history(self):
        for i in get_hist():
            
            name = ft.TextField(value=i.name,expand=True)
            gender =  ft.Dropdown(value=i.gender,expand=True,bgcolor='green',filled=True,options=[ ft.dropdown.Option("AB+"),
                            ft.dropdown.Option("Male"),
                            ft.dropdown.Option("Female"),
                            ft.dropdown.Option("Non-Binary")                        
                    ])
            blood_type = ft.Dropdown(value=i.blood_type,expand=True,bgcolor='green',filled=True,options=[
                            ft.dropdown.Option("AB-"),
                            ft.dropdown.Option("A+"),
                            ft.dropdown.Option("A-"),
                            ft.dropdown.Option("B+"),
                            ft.dropdown.Option("B-"),
                            ft.dropdown.Option("O+"),
                            ft.dropdown.Option("O-")                         
                    ])   
            birth_date = ft.TextField(value=i.birth_date,expand=True)
            age = ft.TextField(value=i.age,expand=True)
            health_problems = ft.TextField(value=i.health_problems,expand=True)
            current_medicines = ft.TextField(value=i.current_medicines,expand=True)
            weight = ft.TextField(value=i.weight,expand=True)
            height = ft.TextField(value=i.height,expand=True)
            bmi = ft.Text(i.bmi,expand=True)





            self.hist.controls.append(ft.Container(content=ft.Row([
            ft.IconButton(ft.icons.DONE,on_click=update_patient(ref_id = i.id,new_data={'Name': name.value, 
                                                                                        'Blood_Type': blood_type.value , 
                                                                                        'Gender': gender.value,
                                                                                        'Birth_Date': birth_date.value,
                                                                                        'Age': age.value,
                                                                                        'Health_Problems': health_problems.value,
                                                                                        'Current_Medicines': current_medicines.value,
                                                                                        'Weight': float(weight.value),
                                                                                        'Height': float(height.value),
                                                                                        'BMI': float(bmi.value)                                                                                    
                                                                                        })),                               
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
                    ft.DataCell(name),
                    ft.DataCell(blood_type),                                         
                    ft.DataCell(gender),
                    ft.DataCell(birth_date),
                    ft.DataCell(age),
                    ft.DataCell(health_problems),
                    ft.DataCell(current_medicines),
                    ft.DataCell(weight),
                    ft.DataCell(height),
                    ft.DataCell(bmi)
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