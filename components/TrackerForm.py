from flet import *
from .ExpenseItem import ExpenseItem
from .IncomeItem import IncomeItem

import firebase_admin
from firebase_admin import credentials
from firebase_admin import firestore
cred = credentials.Certificate("./trackerservicekey.json")
firebase_admin.initialize_app(cred)
db = firestore.client()

class TrackerForm(UserControl):
    def build(self):
        
        self.title = Text(value="Expense/Income Tracker",weight=FontWeight.BOLD, size=20)
        self.track = Dropdown(expand=True,bgcolor='#E0FFFF',on_change=self.showTrack,
            options=[
                dropdown.Option('Income'),
                dropdown.Option('Expense'),
            ]
        )

        self.descplbl = Text(value="Description:",weight=FontWeight.BOLD)
        self.amntlbl = Text(value="Amount:",weight=FontWeight.BOLD)
        self.descp = TextField(expand=True,bgcolor='#E0FFFF',height=30)
        self.amnt = TextField(expand=True,bgcolor='#E0FFFF',height=30)
        self.addBtn = ElevatedButton(text="+", on_click=self.addTrack)

        row = Row(
            controls=[
                self.track,
            ],width=500,alignment=MainAxisAlignment.CENTER
        )

        row1 = Row(
            controls=[
                self.descplbl,
                self.descp
            ]
        )

        row2 = Row(
            controls=[
                self.amntlbl,
                self.amnt,
                self.addBtn
            ]
        )


        self.incomelist = Column()
        self.expenselist = Column()

        return Column(
            controls=[
                self.title,
                row,
                row1,
                row2,
                self.incomelist,
                self.expenselist
            ]
        )
    
    def showTrack(self,e):
        if self.track.value == "Income":
            self.incomelist.visible = True
        else:
            self.expenselist.visible = True
    
    def addTrack(self,e):

        if self.track.value == "Income":
            self.incomelist.controls.append(IncomeItem(self.descp.value,self.amnt.value,self.deleteTrack))
            doc_ref = db.collection("income").document(self.descp.value)
            doc_ref.set({
                u'descp' : str(self.descp.value),
                u'amnt' : str(self.amnt.value),
            })
            self.descp.value = ""
            self.amnt.value = ""
        else:
            self.incomelist.visible = False
            self.expenselist.visible = True
            self.expenselist.controls.append(ExpenseItem(self.descp.value,self.amnt.value,self.deleteTrack))
            doc_ref = db.collection("expense").document(self.descp.value)
            doc_ref.set({
                u'descp' : str(self.descp.value),
                u'amnt' : str(self.amnt.value),
            })
        self.update()
    
    def deleteTrack(self,track):
        self.incomelist.controls.remove(track)
        self.expenselist.controls.remove(track)
        self.update()
    