import calendar
import flet as ft
from datetime import date


class D:
    d = str(date.today()).split('-')
    year = int(d[0])
    month = int(d[1])
    day = int(d[2])


def change_month(value):
    D.month = value


def show_calendar(ly):
    try:
        D.year = int(ly)
    except:
        D.year = int(D.d[0])
        print("Введите число")

    ft.app(target=my_calendar)


def create_months_grid():
    months_matrix = (
        ('Январь', 'Февраль', 'Март', 'Апрель'),
        ('Май', 'Июнь', 'Июль', 'Август'),
        ('Сентябрь', 'Октябрь', 'Ноябрь', 'Декабрь')
    )
    months = (
        'Январь', 'Февраль', 'Март', 'Апрель',
        'Май', 'Июнь', 'Июль', 'Август',
        'Сентябрь', 'Октябрь', 'Ноябрь', 'Декабрь'
    )
    rows = []
    for r in months_matrix:
        row = []
        for m in r:
            row.append(
                ft.Container(
                    content=ft.Text(m, color=ft.colors.BLACK),
                    bgcolor='#4c4a48',
                    width=100,
                    height=75,
                    border_radius=20,
                    alignment=ft.alignment.center,
                    on_click=lambda e: change_month(value=e.control.data),
                    ink=True,
                    data=months.index(m) + 1
                )
            )
        rows.append(row)
    return rows


def create_week(items):
    row = []
    bgcolor = '#616161'
    for e in items:
        if e != 0:
            if D.year == int(D.d[0]) and D.month == int(D.d[1]) and e == D.day:
                bgcolor = '#4c4a48'
            else:
                bgcolor = '#616161'
            c = ft.Container(
                content=ft.Text(e, color=ft.colors.BLACK),
                bgcolor=bgcolor,
                border_radius=20,
                width=50,
                height=50,
                alignment=ft.alignment.center,
                on_click=lambda a: print(f'{a.control.data}.{D.month}.{D.year}'),
                ink=True,
                data=e
            )
        else:
            c = ft.Container(
                width=50,
                height=50
            )

        row.append(c)
    return row


def create_weekdays(items):
    row = []
    for e in items:
        row.append(
            ft.Container(
                content=ft.Text(e, color=ft.colors.BLACK),
                bgcolor='#4c4a48',
                border_radius=20,
                width=50,
                height=50,
                alignment=ft.alignment.center
            )
        )
    return row


def my_calendar(page: ft.Page):
    page.title = f"{D.year}/{D.month}"
    page.window_width = 450
    page.window_height = 425 + 50 * (len(calendar.monthcalendar(D.year, D.month)) == 6)
    page.window_resizable = False

    weekdays = ('пн', 'вт', 'ср', 'чт', 'пт', 'сб', 'вс')
    weekdays_row = ft.Row(spacing=10, controls=create_weekdays(weekdays))
    page.add(weekdays_row)

    for w in calendar.monthcalendar(D.year, D.month):
        week = ft.Row(spacing=10, controls=create_week(w))
        page.add(week)


def hub(page: ft.Page):
    page.window_width = 475
    page.window_height = 475
    page.window_resizable = False
    page.title = 'Hub'
    year_in = ft.TextField(label='Год')
    for r in create_months_grid():
        row = ft.Row(r)
        page.add(row)

    data_in = ft.Container(
        content=ft.Text(value='Показать', color=ft.colors.BLACK),
        width=435,
        height=75,
        alignment=ft.alignment.center,
        ink=True,
        on_click=lambda a: show_calendar(year_in.value),
        border_radius=10,
        bgcolor='#616161'
    )
    page.add(year_in, data_in)


if __name__ == '__main__':
    ft.app(target=hub)
