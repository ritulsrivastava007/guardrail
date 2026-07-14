import flet as ft

from screens.setup import setup_screen


async def splash_screen(page: ft.Page, show):

    async def start(e):
        await show(setup_screen)

    return ft.Container(
        expand=True,
        bgcolor=ft.Colors.WHITE,
        alignment=ft.Alignment.CENTER,

        content=ft.Column(
            alignment=ft.MainAxisAlignment.CENTER,
            horizontal_alignment=ft.CrossAxisAlignment.CENTER,
            spacing=18,

            controls=[

                ft.Icon(
                    icon=ft.Icons.SHIELD_ROUNDED,
                    size=120,
                    color=ft.Colors.BLUE_700,
                ),

                ft.Text(
                    "GuardRail",
                    size=36,
                    weight=ft.FontWeight.BOLD,
                    color=ft.Colors.BLUE_900,
                ),

                ft.Text(
                    "AI Financial Safety Companion",
                    size=18,
                    color=ft.Colors.GREY_700,
                    text_align=ft.TextAlign.CENTER,
                ),

                ft.Container(height=35),

                ft.ElevatedButton(
                    content=ft.Text(
                        "Get Started",
                        size=20,
                        weight=ft.FontWeight.BOLD,
                    ),
                    width=320,
                    height=58,
                    style=ft.ButtonStyle(
                        bgcolor=ft.Colors.BLUE_700,
                        color=ft.Colors.WHITE,
                        shape=ft.RoundedRectangleBorder(radius=14),
                    ),
                    on_click=start,
                ),

                ft.Container(height=20),

                ft.Text(
                    "Built for protecting senior citizens\nagainst modern banking scams.",
                    size=14,
                    color=ft.Colors.GREY_600,
                    text_align=ft.TextAlign.CENTER,
                ),
            ],
        ),
    )