import flet as ft
import asyncio

from screens.lock import lock_screen


async def alert_screen(page: ft.Page, show):

    async def secure_now(e=None):
        await show(lock_screen)


    async def auto_secure():

        await asyncio.sleep(4)

        await show(lock_screen)


    page.run_task(auto_secure)


    return ft.Container(

        expand=True,

        bgcolor=ft.Colors.GREY_100,

        alignment=ft.Alignment.CENTER,


        content=ft.Column(

            alignment=ft.MainAxisAlignment.CENTER,

            horizontal_alignment=ft.CrossAxisAlignment.CENTER,

            spacing=25,


            controls=[


                ft.Container(

                    width=350,

                    padding=20,

                    bgcolor=ft.Colors.WHITE,

                    border_radius=20,


                    shadow=ft.BoxShadow(

                        blur_radius=15,

                        spread_radius=2,

                    ),


                    content=ft.Column(

                        horizontal_alignment=ft.CrossAxisAlignment.CENTER,


                        controls=[


                            ft.Icon(

                                icon=ft.Icons.SHIELD_ROUNDED,

                                size=80,

                                color=ft.Colors.BLUE_700,

                            ),



                            ft.Text(

                                "GuardRail On Duty",

                                size=30,

                                weight=ft.FontWeight.BOLD,

                                color=ft.Colors.BLUE_900,

                            ),



                            ft.Divider(),



                            ft.Text(

                                "⚠ Suspicious Activity Detected",

                                size=18,

                                weight=ft.FontWeight.BOLD,

                                color=ft.Colors.RED,

                                text_align=ft.TextAlign.CENTER,

                            ),



                            ft.Container(height=10),



                            ft.Text(

                                "Incoming financial activity\n"
                                "requires immediate protection.",

                                size=16,

                                text_align=ft.TextAlign.CENTER,

                            ),



                            ft.Container(height=10),



                            ft.Text(

                                "Sender: Unknown User\n"
                                "Risk Level: HIGH\n"
                                "Risk Score: 94%",

                                size=17,

                                text_align=ft.TextAlign.CENTER,

                            ),



                            ft.Container(height=20),



                            ft.ElevatedButton(

                                content=ft.Text(

                                    "Secure Device Now"

                                ),

                                width=260,

                                height=50,


                                on_click=secure_now,

                            ),

                        ],

                    ),

                ),



                ft.Text(

                    "Automatic protection starts in 4 seconds",

                    size=15,

                    color=ft.Colors.GREY_700,

                ),

            ],

        ),

    )