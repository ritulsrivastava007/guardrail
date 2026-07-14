import flet as ft

from datetime import datetime
from state import app_state
from screens.analysis import analysis_screen
from screens.history import history_screen
from screens.settings import settings_screen


async def dashboard_screen(page: ft.Page, show):

    current_time = datetime.now().strftime("%I:%M %p")

    async def simulate(e):
        await show(analysis_screen)

    async def history(e):
        await show(history_screen)

    async def settings(e):
        await show(settings_screen)

    status_color = (
        ft.Colors.GREEN
        if app_state["device_status"] == "Protected"
        else ft.Colors.RED
    )

    return ft.Container(
        expand=True,
        bgcolor=ft.Colors.GREY_100,
        padding=20,

        content=ft.Column(
            expand=True,
            scroll=ft.ScrollMode.AUTO,
            spacing=18,

            controls=[

                # Header
                ft.Row(
                    alignment=ft.MainAxisAlignment.SPACE_BETWEEN,
                    controls=[

                        ft.Column(
                            spacing=2,
                            controls=[
                                ft.Text(
                                    "GuardRail",
                                    size=30,
                                    weight=ft.FontWeight.BOLD,
                                ),
                                ft.Text(
                                    "Enterprise AI Fraud Protection",
                                    color=ft.Colors.GREY_700,
                                ),

                                ft.Text(
                                    f"Last opened: {current_time}",
                                    color=ft.Colors.GREY_600,
                                    size=12,
                                ),
                                
                            ],
                        ),

                        ft.Container(
                            bgcolor=ft.Colors.GREEN_100,
                            padding=10,
                            border_radius=50,
                            content=ft.Icon(
                                ft.Icons.SHIELD,
                                color=ft.Colors.GREEN,
                                size=38,
                            ),
                        ),

                    ],
                ),

                # Main Status Card
                ft.Card(
                    elevation=3,
                    content=ft.Container(
                        padding=20,

                        content=ft.Column(

                            spacing=12,

                            controls=[

                                ft.Row(
                                    controls=[
                                        ft.Icon(
                                            ft.Icons.VERIFIED_USER,
                                            color=status_color,
                                            size=34,
                                        ),

                                        ft.Text(
                                            app_state["device_status"],
                                            size=26,
                                            weight=ft.FontWeight.BOLD,
                                        ),
                                    ],
                                ),

                                ft.Text(
                                    "Your device is continuously protected against online banking fraud.",
                                    color=ft.Colors.GREY_700,
                                ),

                                ft.Divider(),

                                ft.Row(
                                    alignment=ft.MainAxisAlignment.SPACE_BETWEEN,
                                    controls=[
                                        ft.Text("AI Monitoring"),
                                        ft.Text(
                                            "● ONLINE",
                                            color=ft.Colors.GREEN,
                                            weight=ft.FontWeight.BOLD,
                                        ),
                                    ],
                                ),

                                ft.Row(
                                    alignment=ft.MainAxisAlignment.SPACE_BETWEEN,
                                    controls=[
                                        ft.Text("Risk Level"),
                                        ft.Text(
                                            "LOW",
                                            color=ft.Colors.GREEN,
                                            weight=ft.FontWeight.BOLD,
                                        ),
                                    ],
                                ),

                                ft.Row(
                                    alignment=ft.MainAxisAlignment.SPACE_BETWEEN,
                                    controls=[
                                        ft.Text("Last Scan"),
                                        ft.Text(app_state["last_scan"]),
                                    ],
                                ),

                            ],
                        ),
                    ),
                ),

                # Statistics
                ft.Text(
                    "Today's Protection",
                    size=22,
                    weight=ft.FontWeight.BOLD,
                ),

                ft.Row(

                    spacing=12,

                    controls=[

                        ft.Card(
                            expand=True,

                            content=ft.Container(
                                padding=15,

                                content=ft.Column(

                                    horizontal_alignment=ft.CrossAxisAlignment.CENTER,

                                    controls=[
                                        ft.Icon(
                                            ft.Icons.GPP_BAD,
                                            color=ft.Colors.RED,
                                        ),

                                        ft.Text(
                                            "Blocked",
                                            weight=ft.FontWeight.BOLD,
                                        ),

                                        ft.Text(
                                            str(app_state["blocked_today"]),
                                            size=26,
                                            weight=ft.FontWeight.BOLD,
                                            color=ft.Colors.RED,
                                        ),

                                    ],
                                ),
                            ),
                        ),

                        ft.Card(
                            expand=True,

                            content=ft.Container(
                                padding=15,

                                content=ft.Column(

                                    horizontal_alignment=ft.CrossAxisAlignment.CENTER,

                                    controls=[
                                        ft.Icon(
                                            ft.Icons.CHECK_CIRCLE,
                                            color=ft.Colors.GREEN,
                                        ),

                                        ft.Text(
                                            "Safe",
                                            weight=ft.FontWeight.BOLD,
                                        ),

                                        ft.Text(
                                            str(app_state["safe_today"]),
                                            size=26,
                                            weight=ft.FontWeight.BOLD,
                                            color=ft.Colors.GREEN,
                                        ),

                                    ],
                                ),
                            ),
                        ),

                    ],
                ),

                # AI Status
                ft.Card(
                    content=ft.Container(
                        padding=18,

                        content=ft.Column(

                            controls=[

                                ft.Text(
                                    "Live Protection",
                                    size=20,
                                    weight=ft.FontWeight.BOLD,
                                ),

                                ft.Divider(),

                                ft.Row(
                                    controls=[
                                        ft.Icon(ft.Icons.CHECK_CIRCLE,
                                                color=ft.Colors.GREEN),
                                        ft.Text("Banking Apps Protected"),
                                    ],
                                ),

                                ft.Row(
                                    controls=[
                                        ft.Icon(ft.Icons.CHECK_CIRCLE,
                                                color=ft.Colors.GREEN),
                                        ft.Text("OTP Shield Enabled"),
                                    ],
                                ),

                                ft.Row(
                                    controls=[
                                        ft.Icon(ft.Icons.CHECK_CIRCLE,
                                                color=ft.Colors.GREEN),
                                        ft.Text("Screen Sharing Detection"),
                                    ],
                                ),

                                ft.Row(
                                    controls=[
                                        ft.Icon(ft.Icons.CHECK_CIRCLE,
                                                color=ft.Colors.GREEN),
                                        ft.Text("Real-Time AI Monitoring"),
                                    ],
                                ),

                            ],
                        ),
                    ),
                ),

                # Buttons
                ft.ElevatedButton(
                    content=ft.Text(
                        "Simulate Scam Detection",
                        size=18,
                        weight=ft.FontWeight.BOLD,
                    ),
                    width=340,
                    height=55,

                    style=ft.ButtonStyle(
                        bgcolor=ft.Colors.RED_700,
                        color=ft.Colors.WHITE,
                    ),

                    on_click=simulate,
                ),

                ft.OutlinedButton(
                    content=ft.Text(
                        "Protection History",
                        size=18,
                    ),
                    width=340,
                    height=55,
                    on_click=history,
                ),

                ft.OutlinedButton(
                    content=ft.Text(
                        "Settings",
                        size=18,
                    ),
                    width=340,
                    height=55,
                    on_click=settings,
                ),

                ft.Container(height=25),

            ],
        ),
    )