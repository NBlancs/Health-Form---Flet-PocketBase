import flet as ft
from views.AppPage import AppPage
from controller.FormController import create_form
from controller.FormController import get_form
from model.form import form
from model.patient import Patient
 
class FormPage (AppPage):

    def __init__(self, root, route):
        super().__init__(root=root, route=route)
        self.page.vertical_alignment = ft.MainAxisAlignment.CENTER
        self.page.horizontal_alignment = ft.CrossAxisAlignment.CENTER
        self.page.did_mount = self.did_mount

    def did_mount(self):
        self.patient = get_form() 
        
    def get_page(self) -> ft.View:
          
        self.height =  ft.TextField(label="Height (M)",bgcolor='Light_Green',suffix_text='cm', on_change=self.calculate,value=1.0)
        self.weight =  ft.TextField(label="Weight (kg)",bgcolor='Light_Green',suffix_text="kg",on_change=self.calculate ,value=1.0)
        self.bmi = ft.TextField(label='BMI',bgcolor='Light_Green', disabled=True, value=float(self.weight.value) / float(self.height.value)**2)

        
        self.name= ft.TextField(label="Full Name",bgcolor='Light_Green')

        
        self.gender = ft.Dropdown(label="Gender",filled=True,options=[
                            ft.dropdown.Option("Male"),
                            ft.dropdown.Option("Female"),
                            ft.dropdown.Option("Non-Binary")
                        ])
        self.blood_type = ft.Dropdown(label="Blood Type",filled=True,options=[
                            ft.dropdown.Option("AB+"),
                            ft.dropdown.Option("AB-"),
                            ft.dropdown.Option("A+"),
                            ft.dropdown.Option("A-"),
                            ft.dropdown.Option("B+"),
                            ft.dropdown.Option("B-"),
                            ft.dropdown.Option("O+"),
                            ft.dropdown.Option("O-")
                        ])
        self.birthdate = ft.TextField(label="Birth Date (MM/DD/YYYY)",bgcolor='Light_Green')
        self.age = ft.TextField(label="Age",bgcolor='Light_Green')
        self.healthproblems = ft.TextField(label="Health Problems",multiline=True,bgcolor='Light_Green')
        self.currentmedicines = ft.TextField(label="Current Medicines",multiline=True,bgcolor='Light_Green')

        self.page.controls = [
            ft.ResponsiveRow(
                controls=[
                    ft.Row([
                        self.name,
                        self.gender,
                        self.blood_type
                    ],alignment=ft.MainAxisAlignment.CENTER)
                ], expand=True
            ),
            ft.ResponsiveRow(
                controls=[
                    ft.Row([
                        self.birthdate 
                    ],alignment=ft.MainAxisAlignment.CENTER)
                ]
            ),
            ft.ResponsiveRow(
                controls=[
                    ft.Row([
                        self.age,
                        self.healthproblems,
                        self.currentmedicines
                    ],alignment=ft.MainAxisAlignment.CENTER)
                ], expand=True
            ),
            ft.ResponsiveRow(
                controls=[
                    ft.Row([                        
                            self.height,
                            self.weight,
                            self.bmi                       
                    ],alignment=ft.MainAxisAlignment.CENTER)
                ], expand=True
            ),
            ft.ResponsiveRow(
                controls=[
                    ft.Row([
                        ft.FilledTonalButton (text="BACK",icon= ft.icons.ARROW_BACK_SHARP, on_click=lambda _: self.root.go('/')),   
                        ft.FilledTonalButton(text="DONE",icon=ft.icons.DONE, on_click=lambda _:create_form
                                             (self.name.value,
                                              self.gender.value,
                                              self.age.value,
                                              self.blood_type.value,
                                              self.birthdate.value,
                                              self.healthproblems.value,
                                              self.currentmedicines.value,
                                              float(self.height.value),
                                              float(self.weight.value),
                                              float(self.bmi.value),
                                              self.root
                                              )),
                    ],alignment=ft.MainAxisAlignment.CENTER)
                ], expand=True
            ),                 
        ] 

        return self.page
    def calculate(self,_):
        try:
            self.bmi.value = float(self.weight.value) / float(self.height.value)**2
            self.page.update()
        except: ValueError




