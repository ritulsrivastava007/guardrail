import flet as ft

from screens.splash import SplashScreen
from screens.onboarding import OnboardingScreen
from screens.dashboard import DashboardScreen
from screens.analysis import AnalysisScreen
from screens.protection import ProtectionScreen
from screens.history import HistoryScreen


async def main(page: ft.Page):

    page.title = "GuardRail - Financial Safety Companion"

    page.theme_mode = ft.ThemeMode.LIGHT

    page.theme = ft.Theme(
        color_scheme=ft.ColorScheme(
            primary=ft.Colors.BLUE_700,
            on_primary=ft.Colors.WHITE,
            surface=ft.Colors.WHITE,
            error=ft.Colors.RED_700,
        )
    )

    # Mobile demo window
    page.window.width = 390
    page.window.height = 844
    page.window.resizable = False


    # Global app state
    page.state = {
        "session_history": [
            {
                "amount": "₹48,000",
                "sender": "Employer Salary",
                "status": "Verified",
                "risk": "2%",
                "color": ft.Colors.GREEN_700
            }
        ],
        "active_sender": "Rajesh Kumar",
        "active_amount": 50000,
        "active_risk": 94
    }


    async def route_change(e):

        page.views.clear()

        if page.route == "/":
            view = await SplashScreen(page)

        elif page.route == "/onboarding":
            view = await OnboardingScreen(page)

        elif page.route == "/dashboard":
            view = await DashboardScreen(page)

        elif page.route == "/analysis":
            view = await AnalysisScreen(page)

        elif page.route == "/protection":
            view = await ProtectionScreen(page)

        elif page.route == "/history":
            view = await HistoryScreen(page)

        else:
            view = ft.View(
                "/",
                [
                    ft.Text("Page Not Found")
                ]
            )


        page.views.append(view)
        await page.update()



    def view_pop(e):

        if len(page.views) > 1:
            page.views.pop()
            page.go(page.views[-1].route)



    page.on_route_change = route_change
    page.on_view_pop = view_pop


    page.go("/")



if __name__ == "__main__":
    ft.run(main)