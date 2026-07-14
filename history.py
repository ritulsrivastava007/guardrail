import flet as ft

from state import app_state


async def history_screen(page: ft.Page, show):

    history_cards = []

    for item in app_state["history"]:

        if item["color"] == "green":
            icon = ft.Icons.CHECK_CIRCLE
            color = ft.Colors.GREEN
        else:
            icon = ft.Icons.GPP_BAD
            color = ft.Colors.RED

        history_cards.append(

            ft.Card(

                elevation=2,

                content=ft.Container(

                    padding=15,

                    content=ft.Column(

                        spacing=8,

                        controls=[

                            ft.Row(

                                alignment=ft.MainAxisAlignment.SPACE_BETWEEN,

                                controls=[

                                    ft.Row(

                                        controls=[

                                            ft.Icon(
                                                icon,
                                                color=color,
                                            ),

                                            ft.Text(
                                                item["status"],
                                                weight=ft.FontWeight.BOLD,
                                                color=color,
                                            ),

                                        ],

                                    ),

                                    ft.Text(
                                        item["time"],
                                        color=ft.Colors.GREY_700,
                                        size=12,
                                    ),

                                ],

                            ),

                            ft.Divider(),

                            ft.Row(

                                alignment=ft.MainAxisAlignment.SPACE_BETWEEN,

                                controls=[

                                    ft.Column(

                                        spacing=3,

                                        controls=[

                                            ft.Text(
                                                item["sender"],
                                                size=18,
                                                weight=ft.FontWeight.BOLD,
                                            ),

                                            ft.Text(
                                                "Protected by GuardRail AI",
                                                color=ft.Colors.GREY_700,
                                            ),

                                        ],

                                    ),

                                    ft.Text(
                                        item["amount"],
                                        size=18,
                                        weight=ft.FontWeight.BOLD,
                                    ),

                                ],

                            ),

                        ],

                    ),

                ),

            )

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

                    alignment=ft.MainAxisAlignment.SPACE_BETWEEN,

                    controls=[

                        ft.Text(
                            "Protection History",
                            size=30,
                            weight=ft.FontWeight.BOLD,
                        ),

                        ft.Icon(
                            ft.Icons.HISTORY,
                            color=ft.Colors.BLUE,
                            size=35,
                        ),

                    ],

                ),

                ft.Text(
                    "Every detected transaction is stored securely.",
                    color=ft.Colors.GREY_700,
                ),

                *history_cards,

                ft.ElevatedButton(

                    width=340,

                    height=55,

                    style=ft.ButtonStyle(

                        bgcolor=ft.Colors.BLUE_700,

                        color=ft.Colors.WHITE,

                    ),

                    content=ft.Text(
                        "Back to Dashboard",
                        size=18,
                        weight=ft.FontWeight.BOLD,
                    ),

                    on_click=back,

                ),

                ft.Container(height=20),

            ],

        ),

    )