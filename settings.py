import flet as ft


async def settings_screen(page: ft.Page, show):

    auto_protection = ft.Switch(
        label="Auto Protection",
        value=True,
    )

    otp_shield = ft.Switch(
        label="OTP Shield",
        value=True,
    )

    screen_detection = ft.Switch(
        label="Screen Sharing Detection",
        value=True,
    )

    ai_monitor = ft.Switch(
        label="AI Continuous Monitoring",
        value=True,
    )

    biometric = ft.Switch(
        label="Biometric Confirmation",
        value=False,
    )

    async def back(e):
        from screens.dashboard import dashboard_screen
        await show(dashboard_screen)

    return ft.Container(
        expand=True,
        bgcolor=ft.Colors.GREY_100,
        padding=20,

        content=ft.Column(
            expand=True,
            scroll=ft.ScrollMode.AUTO,
            spacing=20,

            controls=[

                ft.Row(
                    controls=[
                        ft.Icon(
                            ft.Icons.SETTINGS,
                            size=35,
                            color=ft.Colors.BLUE,
                        ),

                        ft.Text(
                            "Settings",
                            size=30,
                            weight=ft.FontWeight.BOLD,
                        ),
                    ],
                ),

                ft.Card(
                    content=ft.Container(
                        padding=15,

                        content=ft.Column(

                            controls=[

                                auto_protection,

                                otp_shield,

                                screen_detection,

                                ai_monitor,

                                biometric,

                            ],
                        ),
                    ),
                ),

                ft.Card(
                    content=ft.Container(
                        padding=20,

                        content=ft.Column(

                            spacing=10,

                            controls=[

                                ft.Text(
                                    "About GuardRail",
                                    size=22,
                                    weight=ft.FontWeight.BOLD,
                                ),

                                ft.Divider(),

                                ft.Text(
                                    "Version 1.0.0"
                                ),

                                ft.Text(
                                    "Enterprise AI Fraud Protection"
                                ),

                                ft.Text(
                                    "Designed for Smart India Hackathon Demo"
                                ),

                            ],
                        ),
                    ),
                ),

                ft.ElevatedButton(
                    width=340,
                    height=55,

                    style=ft.ButtonStyle(
                        bgcolor=ft.Colors.BLUE_700,
                        color=ft.Colors.WHITE,
                    ),

                    content=ft.Text(
                        "Back",
                        size=18,
                        weight=ft.FontWeight.BOLD,
                    ),

                    on_click=back,
                ),

            ],
        ),
    )