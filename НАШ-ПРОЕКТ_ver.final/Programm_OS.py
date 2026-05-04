import flet as ft
import random

def main(page: ft.Page):
    page.title = "НАШ ПРОЕКТ"
    page.vertical_alignment = ft.MainAxisAlignment.CENTER
    page.horizontal_alignment = ft.CrossAxisAlignment.CENTER
    page.theme_mode = ft.ThemeMode.DARK


    user_id = ft.Text(value="0", size=20)
    auth_status = ft.Text(value="Авторизованный", size=20)
    counter = 0  

    text_number = ft.TextField(
        label="Пользователь",
        label_style=ft.TextStyle(color=ft.Colors.YELLOW),
        text_align=ft.TextAlign.RIGHT,
        width=200,
        color=ft.Colors.WHITE,
        bgcolor=ft.Colors.PURPLE_500,
        focused_border_color=ft.Colors.YELLOW,
    )
    password = ft.TextField(
        label="Пароль",
        label_style=ft.TextStyle(color=ft.Colors.YELLOW),
        text_align=ft.TextAlign.RIGHT,
        width=200,
        password=True,
        helper="Минимум 8 символов",
        color=ft.Colors.WHITE,
        bgcolor=ft.Colors.PURPLE_500,
        focused_border_color=ft.Colors.YELLOW,
    )
    check = ft.Checkbox(label="YES OF COURSE", value=False)
    info_text = ft.Text(
        value="Добро пожаловать на регистрацию. Введите данные для входа в систему.",
        color="grey",
        size=15
    )
    error_text = ft.Text(value="", color="red", size=12)
    WIN_text = ft.Text(value="", color="green", size=12)

    submit_button = ft.FilledButton(
        content=ft.Text("Подтвердить"),
        color=ft.Colors.YELLOW,
        bgcolor=ft.Colors.RED_900,
        width=200,
        disabled=True
    )

    back_button = ft.FilledButton(
        content=ft.Text("В ГЛАВНОЕ МЕНЮ"),
        color=ft.Colors.YELLOW,
        bgcolor=ft.Colors.RED_900,
        width=200,
    )
    site_button = ft.FilledButton(
        content=ft.Text("Ссылка на сайт"),
        width=200,
        color=ft.Colors.YELLOW,
        bgcolor=ft.Colors.RED_900,
    )
    profile_button = ft.FilledButton(
        content=ft.Text("Профиль"),
        color=ft.Colors.YELLOW,
        bgcolor=ft.Colors.RED_900,
        width=200,
    )
    description_button = ft.FilledButton(
        content=ft.Text("Описание сайта"),
        color=ft.Colors.YELLOW,
        bgcolor=ft.Colors.RED_900,
        width=200,
    )
    counter_button = ft.FilledButton(
        content=ft.Text(value="0"),
        color=ft.Colors.YELLOW,
        bgcolor=ft.Colors.RED_900,
        width=200,
    )

    IMAGE = ft.Image(
        src="https://i.postimg.cc/WbxfVSJH/1679482137-1s2.jpg",
        width=150,
        height=150,
    )

    TEXT_1 = ft.Text(
        value="Приветствуем вас на нашем проекте по операционным системам.\nЗдесь мы приглашаем самых любопытных и заинтересованных людей.\nВ нём вы узнаете, насколько тяжело проектировать и ощущать на себе\nвсю сложность нашего проекта. Далее нас ждёт много всего интересн-\nого. Проект будет состоять из нескольких этапов. Первым станет уник-\nальная идея. Затем следует сама разработка. Третий этап — бета-тест-\nирование, и в конце мы объявляем о завершении данного проекта.\nПосетите сайт и узнайте о нас подробнее.",
        size=14
    )


    def validate(e):
        if text_number.value and password.value and len(password.value) >= 8 and check.value:
            submit_button.disabled = False
            error_text.value = ""
        else:
            submit_button.disabled = True
            if password.value and len(password.value) < 8:
                error_text.value = "Пароль должен содержать минимум 8 символов"
            else:
                error_text.value = ""
        page.update()

    def on_submit(e):
        print("Пользователь:", text_number.value)
        print("Пароль:", password.value)
        page.controls.clear()
        page.add(
    ft.Column(
            alignment=ft.MainAxisAlignment.CENTER,
            horizontal_alignment=ft.CrossAxisAlignment.CENTER,
            controls=[
                ft.Text(value="Добро пожаловать", size=24, weight=ft.FontWeight.BOLD),
                ft.Container(),
                ft.Row(
                    alignment=ft.MainAxisAlignment.CENTER,
                    controls=[
                        counter_button,
                        site_button,
                        profile_button,
                        description_button
                    ]
                ),
            ]
        )
    )
    page.title = "ОПЕРАЦИОННЫЕ СИСТЕМЫ"    
    page.update()

    async def open_url(e):
        await page.launch_url("https://flet.dev/docs/types/alignment/")

    def show_main_menu(e):
        page.controls.clear()
        page.add(
            ft.Column(
            alignment=ft.MainAxisAlignment.START,
            horizontal_alignment=ft.CrossAxisAlignment.CENTER,
            controls=[
                ft.Text(value="Добро пожаловать", size=24, weight=ft.FontWeight.BOLD),
                ft.Row(
                    alignment=ft.MainAxisAlignment.CENTER,
                    controls=[
                        counter_button,
                        site_button,
                        profile_button,
                        description_button
                    ]
                ),
            ]
        )
    )
    page.update()


    def show_profile(e):
        user_id.value = f"ID: {random.randint(1000, 999999)}"
        page.controls.clear()
        page.add(
            ft.Stack(
                [
                    ft.Container(
                        content=ft.Text(value=f"Имя: {text_number.value}", size=20),
                        right=155,
                        top=25,
                    ),
                    ft.Container(
                        content=IMAGE,
                        right=10,
                        top=10,
                    ),
                    ft.Container(
                        content=user_id,
                        right=155,
                        top=60,
                    ),
                    ft.Container(
                        content=auth_status,
                        right=155,
                        top=95,
                    ),
                    ft.Container(
                        content=back_button,
                        bottom=10,
                        right=0,
                        left=0,
                    ),
                ],
                expand=True,
            )
        )
        page.update()

    def show_description(e):
        page.controls.clear()
        page.add(
            ft.Column(
                alignment=ft.MainAxisAlignment.CENTER,
                controls=[
                    TEXT_1,
                    back_button
                ],
            )
        )
        page.update()

    def increase_counter(e):
        nonlocal counter
        counter += 1
        counter_button.content.value = str(counter)
        counter_button.bgcolor = ft.Colors.RED_900  
        counter_button.update()
        if(counter == 100):
            WIN_text.value = ft.Text(value="Ты победил", color="green", size=12)
            counter_button.disabled = True

    text_number.on_change = validate
    password.on_change = validate
    check.on_change = validate
    submit_button.on_click = on_submit
    site_button.on_click = open_url
    profile_button.on_click = show_profile
    back_button.on_click = show_main_menu
    description_button.on_click = show_description
    counter_button.on_click = increase_counter

    page.add(
        ft.Row(
            alignment=ft.MainAxisAlignment.CENTER,
            controls=[
                ft.Column(
                    controls=[
                        text_number,
                        password,
                        error_text,
                        check,
                        submit_button,
                        info_text
                    ],
                    alignment=ft.MainAxisAlignment.CENTER,
                    horizontal_alignment=ft.CrossAxisAlignment.CENTER,
                    spacing=10
                )
            ]
        )
    )

ft.app(target=main)