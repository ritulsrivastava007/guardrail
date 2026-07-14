import flet as ft

from state import app_state

from screens.splash import splash_screen
from screens.setup import setup_screen
from screens.dashboard import dashboard_screen
from screens.analysis import analysis_screen
from screens.warning import warning_screen
from screens.history import history_screen


async def main(page: ft.Page):
    page.title = "🛡 GuardRail"
    page.window_width = 390
    page.window_height = 844
    page.window_resizable = False
    page.bgcolor = ft.Colors.GREY_100
    page.padding = 0
    page.horizontal_alignment = ft.CrossAxisAlignment.CENTER
    page.vertical_alignment = ft.MainAxisAlignment.CENTER

    async def show(screen):
        page.clean()
        control = await screen(page, show)
        page.add(control)
        page.update()

    app_state["show"] = show

    await show(splash_screen)


ft.run(main)
