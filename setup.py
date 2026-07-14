import flet as ft

from state import app_state


async def setup_screen(page: ft.Page, show):

    async def enable_protection(e):

        app_state["registered"] = True
        app_state["device_protected"] = True
        app_state["protection_active"] = True

        from screens.dashboard import dashboard_screen

        await show(dashboard_screen)


    return ft.Container(

        expand=True,

        bgcolor=ft.Colors.WHITE,

        alignment=ft.Alignment.CENTER,


        content=ft.Column(

            horizontal_alignment=ft.CrossAxisAlignment.CENTER,

            alignment=ft.MainAxisAlignment.CENTER,

            spacing=22,


            controls=[


                ft.Icon(

                    icon=ft.Icons.SHIELD_ROUNDED,

                    size=120,

                    color=ft.Colors.BLUE_700,

                ),



                ft.Text(

                    "Secure Your Device",

                    size=32,

                    weight=ft.FontWeight.BOLD,

                    color=ft.Colors.BLUE_900,

                ),



                ft.Text(

                    "GuardRail becomes your AI security layer",

                    size=17,

                    color=ft.Colors.GREY_700,

                    text_align=ft.TextAlign.CENTER,

                ),



                ft.Container(

                    width=330,

                    padding=20,

                    bgcolor=ft.Colors.BLUE_50,

                    border_radius=15,


                    content=ft.Column(

                        controls=[


                            ft.Text(

                                "GuardRail will monitor:",

                                size=18,

                                weight=ft.FontWeight.BOLD,

                            ),



                            ft.Text(
                                "✓ Suspicious transactions"
                            ),


                            ft.Text(
                                "✓ Scam messages"
                            ),


                            ft.Text(
                                "✓ Remote access attempts"
                            ),


                            ft.Text(
                                "✓ Financial safety risks"
                            ),

                        ],

                    ),

                ),



                ft.ElevatedButton(

                    content=ft.Text(

                        "Enable Protection",

                        size=20,

                        weight=ft.FontWeight.BOLD,

                    ),


                    width=320,

                    height=55,


                    style=ft.ButtonStyle(

                        bgcolor=ft.Colors.BLUE_700,

                        color=ft.Colors.WHITE,


                        shape=ft.RoundedRectangleBorder(

                            radius=12

                        ),

                    ),


                    on_click=enable_protection,

                ),


            ],

        ),

    )