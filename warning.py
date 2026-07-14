import flet as ft
import asyncio

from screens.history import history_screen


async def warning_screen(page: ft.Page, show):

    timer_text = ft.Text(
        "30:00",
        size=32,
        weight=ft.FontWeight.BOLD,
        color=ft.Colors.RED_700,
    )

    progress = ft.ProgressBar(
        width=330,
        value=1,
        color=ft.Colors.RED,
    )

    protection_status = ft.Text(
        "Maximum Protection Enabled",
        color=ft.Colors.GREEN,
        weight=ft.FontWeight.BOLD,
        size=18,
    )

    async def countdown():

        total = 30 * 60
        remaining = total

        while remaining >= 0:

            try:

                minutes = remaining // 60
                seconds = remaining % 60

                timer_text.value = f"{minutes:02}:{seconds:02}"
                progress.value = remaining / total

                page.update()

                await asyncio.sleep(1)

                remaining -= 1

            except RuntimeError:
                break

    page.run_task(countdown)

    async def continue_app(e):
        await show(history_screen)

    return ft.Container(

        expand=True,

        bgcolor=ft.Colors.RED_50,

        padding=20,

        content=ft.Column(

            expand=True,

            scroll=ft.ScrollMode.AUTO,

            horizontal_alignment=ft.CrossAxisAlignment.CENTER,

            spacing=20,

            controls=[

                ft.Container(height=10),

                ft.Icon(
                    ft.Icons.GPP_BAD,
                    size=110,
                    color=ft.Colors.RED,
                ),

                ft.Text(
                    "Threat Successfully Blocked",
                    size=30,
                    weight=ft.FontWeight.BOLD,
                    text_align=ft.TextAlign.CENTER,
                ),

                ft.Text(
                    "GuardRail prevented a possible banking fraud before any sensitive information was exposed.",
                    text_align=ft.TextAlign.CENTER,
                    color=ft.Colors.GREY_700,
                ),

                ft.Card(

                    content=ft.Container(

                        width=340,

                        padding=20,

                        content=ft.Column(

                            spacing=10,

                            controls=[

                                ft.Text(
                                    "Threat Report",
                                    size=22,
                                    weight=ft.FontWeight.BOLD,
                                ),

                                ft.Divider(),

                                ft.Row(
                                    alignment=ft.MainAxisAlignment.SPACE_BETWEEN,
                                    controls=[
                                        ft.Text("Sender"),
                                        ft.Text("Unknown Sender"),
                                    ],
                                ),

                                ft.Row(
                                    alignment=ft.MainAxisAlignment.SPACE_BETWEEN,
                                    controls=[
                                        ft.Text("Transaction"),
                                        ft.Text("₹50,000"),
                                    ],
                                ),

                                ft.Row(
                                    alignment=ft.MainAxisAlignment.SPACE_BETWEEN,
                                    controls=[
                                        ft.Text("Risk Score"),
                                        ft.Text(
                                            "94%",
                                            color=ft.Colors.RED,
                                            weight=ft.FontWeight.BOLD,
                                        ),
                                    ],
                                ),

                                ft.Row(
                                    alignment=ft.MainAxisAlignment.SPACE_BETWEEN,
                                    controls=[
                                        ft.Text("Action"),
                                        ft.Text(
                                            "BLOCKED",
                                            color=ft.Colors.GREEN,
                                            weight=ft.FontWeight.BOLD,
                                        ),
                                    ],
                                ),

                            ],

                        ),

                    ),

                ),

                ft.Card(

                    content=ft.Container(

                        width=340,

                        padding=20,

                        content=ft.Column(

                            controls=[

                                ft.Text(
                                    "Protection Status",
                                    size=22,
                                    weight=ft.FontWeight.BOLD,
                                ),

                                ft.Divider(),

                                protection_status,

                                ft.Text("✔ Banking apps locked"),

                                ft.Text("✔ OTP shield active"),

                                ft.Text("✔ Screen sharing blocked"),

                                ft.Text("✔ Accessibility attack blocked"),

                                ft.Text("✔ Suspicious notifications filtered"),

                            ],

                        ),

                    ),

                ),

                ft.Text(
                    "Protection ends in",
                    size=18,
                    weight=ft.FontWeight.BOLD,
                ),

                timer_text,

                progress,

                ft.ElevatedButton(

                    width=340,

                    height=55,

                    style=ft.ButtonStyle(
                        bgcolor=ft.Colors.BLUE_700,
                        color=ft.Colors.WHITE,
                    ),

                    content=ft.Text(
                        "View Security Report",
                        size=18,
                        weight=ft.FontWeight.BOLD,
                    ),

                    on_click=continue_app,

                ),

                ft.Container(height=20),

            ],

        ),

    )