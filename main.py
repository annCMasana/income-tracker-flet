from flet import *
from components.TrackerForm import TrackerForm

def main(page: Page):
    page.title = "Expense/Income Tracker App"
    page.window_width = 600
    page.window_height = 700
    page.bgcolor = '#D2E7D6'
    page.window_center()


    page.add(
        TrackerForm()
    )
    
    page.update()


app(target=main)