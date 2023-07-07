from flet import *

class IncomeItem(UserControl):

    def __init__(self,track,track1,deleteTodo):
        super().__init__()
        self.track = track
        self.track1 = track1
        self.delete = deleteTodo

    def build(self):
        self.txt = Text(value=str(self.track),size=15,expand=True,color=colors.BLACK)
        self.txt1 = Text(value=str(self.track1),size=15,expand=True,color=colors.BLACK)
        self.editBtn = IconButton(icon=icons.EDIT,on_click=self.showEdit)
        self.deleteBtn = IconButton(icon=icons.DELETE,on_click=self.deleteTrack)
        self.editTrack = TextField(value=str(self.track),bgcolor=colors.WHITE,color=colors.BLACK)
        self.saveBtn = IconButton(icon=icons.CHECK,on_click=self.updateTrack,icon_color="WHITE")
        self.cancelBtn = IconButton(icon=icons.CANCEL,on_click=self.cancel,icon_color="WHITE")

        self.itemRow = Container(
            border=border.only(left=border.BorderSide(2.0, "AMBER")),
            bgcolor=colors.WHITE,
            border_radius=10,
            padding=6,
            content=Row(
            controls=[
                self.txt,
                self.txt1,
                self.editBtn,
                self.deleteBtn
            ],width=500,alignment=MainAxisAlignment.CENTER,
        )
        )

        self.editrow = Row(
            controls=[
                self.editTrack,
                self.saveBtn,
                self.cancelBtn
            ],width=500,alignment=MainAxisAlignment.CENTER,visible=False
        )

        return Column(
            controls=[
                self.itemRow,
                self.editrow
            ]
        )
    
    def showEdit(self,e):
        self.itemRow.visible = False
        self.editrow.visible = True
        self.update()

    def cancel(self,e):
        self.itemRow.visible = True
        self.editrow.visible = False
        self.update()

    def updateTrack(self,e):
        newTrack = str(self.editTrack.value)
        self.txt.value = newTrack
        self.editrow.visible = False
        self.itemRow.visible = True
        self.update()

    def deleteTrack(self,e):
        self.delete(self)
        