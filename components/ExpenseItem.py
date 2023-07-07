from flet import *


class ExpenseItem(UserControl):

    def __init__(self, name,name1, deleteTodo):
        super().__init__()
        self.name = name
        self.name1 = name1
        self.delete = deleteTodo

    def build(self):
        self.text = Text(value=str(self.name), size=15)
        self.text1 = Text(value=("PHP " + str(self.name1)), size=15)
        self.editBtn = IconButton(icon=icons.EDIT, on_click=self.showEdit, icon_color=colors.AMBER)
        self.deleteBtn = IconButton(icon=icons.DELETE, on_click=self.deleteTracker, icon_color=colors.PINK)
        self.editInput = TextField(value=str(self.name), text_size=20, width=350, border_color=colors.BLUE)
        self.savebtn = IconButton(icon=icons.CHECK, on_click=self.updateTracker, icon_color=colors.GREEN, bgcolor=colors.WHITE)
        self.cancelbtn = IconButton(icon=icons.CANCEL, on_click=self.cancel, icon_color=colors.RED, bgcolor=colors.WHITE)


        self.itemrow = Container(
            border = border.all(1.0, colors.BROWN),
            content=Row(controls=[
            self.text,self.text1,
            Row(controls=[
            self.editBtn,
            self.deleteBtn])
        ], alignment=MainAxisAlignment.SPACE_BETWEEN))
    
        self.editrow = Row(controls=[
            self.editInput,
            self.savebtn,
            self.cancelbtn
        ], alignment=MainAxisAlignment.CENTER, visible=False)

        return Column(controls=[
            self.itemrow,
            self.editrow
        ])
    
    def showEdit(self, e):
        self.itemrow.visible = False
        self.editrow.visible = True
        self.update()

    def cancel(self, e):
        self.itemrow.visible = True
        self.editrow.visible = False
        self.update()

    def updateTracker(self, e):
        newName = str(self.editInput.value)
        self.text.value = newName
        self.editrow.visible = False
        self.itemrow.visible = True
        self.update()

    def deleteTracker(self, e):
        self.delete(self)
