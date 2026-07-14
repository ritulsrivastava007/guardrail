import flet as ft
import asyncio
from datetime import datetime

from state import app_state
from screens.warning import warning_screen


async def analysis_screen(page: ft.Page, show):

    progress = ft.ProgressBar(width=340, value=0)

    percent = ft.Text(
        "0%",
        size=24,
        weight=ft.FontWeight.BOLD,
        color=ft.Colors.BLUE,
    )

    status = ft.Text(
        "Initializing GuardRail AI...",
        size=18,
        weight=ft.FontWeight.BOLD,
        text_align=ft.TextAlign.CENTER,
    )

    checks = ft.Column(
        spacing=12,
        scroll=ft.ScrollMode.AUTO,
        expand=True,
    )

    async def run_scan():

        steps = [
            "Checking sender reputation...",
            "Analyzing transaction behaviour...",
            "Inspecting device integrity...",
            "Protecting banking applications...",
            "Scanning SMS & OTP activity...",
            "Verifying network reputation...",
            "Running AI fraud prediction...",
            "Calculating threat score...",
        ]

        total = len(steps)

        for i, step in enumerate(steps):

            status.value = step

            checks.controls.append(
                ft.Row(
                    controls=[
                        ft.ProgressRing(width=18, height=18),
                        ft.Text(step),
                    ]
                )
            )

            page.update()

            await asyncio.sleep(0.8)

            checks.controls[-1] = ft.Row(
                controls=[
                    ft.Icon(
                        ft.Icons.CHECK_CIRCLE,
                        color=ft.Colors.GREEN,
                    ),
                    ft.Text(step),
                ]
            )

            value = (i + 1) / total

            progress.value = value
            percent.value = f"{int(value*100)}%"

            page.update()

        status.value = "🚨 Threat Detected"

        app_state["last_scan"] = "Just Now"
        app_state["blocked_today"] += 1

        app_state["history"].insert(
            0,
            {
                "sender": app_state["sender"],
                "amount": app_state["amount"],
                "status": "Blocked",
                "color": "red",
                "time": datetime.now().strftime("%I:%M %p"),
            },
        )

        page.update()

        await asyncio.sleep(2)

        await show(warning_screen)

    page.run_task(run_scan)

    return ft.Container(
        expand=True,
        bgcolor=ft.Colors.WHITE,
        padding=20,

        content=ft.Column(
            expand=True,
            horizontal_alignment=ft.CrossAxisAlignment.CENTER,
            spacing=20,

            controls=[

                ft.Container(height=20),

                ft.Icon(
                    ft.Icons.SECURITY,
                    size=90,
                    color=ft.Colors.BLUE,
                ),

                ft.Text(
                    "GuardRail AI Engine",
                    size=30,
                    weight=ft.FontWeight.BOLD,
                ),

                ft.Text(
                    "Enterprise Fraud Detection System",
                    color=ft.Colors.GREY_700,
                ),

                percent,

                progress,

                status,

                ft.Divider(),

                ft.Text(
                    "Live Analysis",
                    size=20,
                    weight=ft.FontWeight.BOLD,
                ),

                checks,

                ft.Container(height=20),

            ],
        ),
    )