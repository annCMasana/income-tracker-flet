from flet import *
from components.TrackerForm import TrackerForm

def main(page: Page):
    page.title="Income Tracker"
    page.window_width = 500
    page.window_height = 600
    page.bgcolor = '#8DA399'
    page.window_center()


    page.add(
        TrackerForm()
    )
    page.update()

app(target=main)