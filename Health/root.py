import flet as ft

from views.AppPage import AppPage
from views.mainpage import MainPage
from views.formpage import FormPage
from views.ThankYou import ThankYou
from views.loginpage import LoginPage
from views.ViewHistory import History
from views.HealthDashBoard import DashBoard
from views.DeleteHistory import DeleteHistory
from views.UpdateHistory import UpdateHistory

def main(page: ft.Page):

    pages: list[AppPage] = [
        MainPage(root=page, route='/'),
        LoginPage(root=page, route='/login'),
        FormPage(root=page, route='/form'),
        ThankYou(root=page, route='/thanks'),
        DashBoard(root=page, route='/dash'),
        History(root=page, route='/hist'),
        DeleteHistory (root=page, route='/del'),
        UpdateHistory(root=page, route='/upt'),
    ]

    page.title = "HEALTH RECORD FORM"

    theme = ft.Theme(
        color_scheme_seed=ft.colors.GREEN,
        use_material3=True
    )

    page.theme = theme
    page.dark_theme = theme
    page.theme_mode = ft.ThemeMode.LIGHT
    page.window_bgcolor = ft.colors.LIGHT_GREEN_800

    page.vertical_alignment = ft.MainAxisAlignment.CENTER
    page.horizontal_alignment = ft.CrossAxisAlignment.CENTER

    def route_change(_):
        page.views.clear()
        print(pages[0].page.route)

        sel = tuple(filter(lambda x: x.page.route == page.route, pages))
        page.views.append(sel[0].get_page())
        page.go(sel[0].page.route)


    page.on_route_change = route_change
    page.go(page.route)