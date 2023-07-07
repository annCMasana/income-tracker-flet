from flet import *
from .IncomeItem import IncomeItem
from .ExpenseItem import ExpenseItem

import firebase_admin
from firebase_admin import credentials
from firebase_admin import firestore
cred = credentials.Certificate("./midtermappservicekey.json")
firebase_admin.initialize_app(cred)
db = firestore.client()

class TrackerForm(UserControl):

    def build(self):
        self.title = Text(value="Expense/Income Tracker",weight=FontWeight.BOLD, size=35, color='Brown')
        self.tracker = Dropdown(
        width=100,
        options=[
            dropdown.Option("Income"),
            dropdown.Option("Expense"),
            ],value="Income" ,border_color=colors.BLACK, on_change=self.showTracker
        )
        self.descriptionlbl = Text(value="DESCRIPTION:", width=100,weight=FontWeight.BOLD,)
        self.amountlbl = Text(value="AMOUNT:", width=100,weight=FontWeight.BOLD,)
        self.description = TextField(label="", width=300,height=30,text_size=15, border_color=colors.BLACK,)
        self.amount = TextField(label="", width=300,height=30,text_size=15, border_color=colors.BLACK,)
        self.addBtn = ElevatedButton(text="+", bgcolor=colors.BROWN, color=colors.WHITE, on_click=self.addTracker)

        row1 = Row(controls=[
            self.title
        ], alignment=MainAxisAlignment.CENTER)
        
        row2 = Row(controls=[
            self.tracker
        ], alignment=MainAxisAlignment.CENTER)

        row3 = Row(controls=[
            self.descriptionlbl,
            self.description,
        ], alignment=MainAxisAlignment.CENTER)

        row4 = Row(controls=[
            self.amountlbl,
            self.amount,
        ], alignment=MainAxisAlignment.CENTER)

        col2 = Column(controls=[
            self.addBtn
        ], alignment=MainAxisAlignment.CENTER)
        
        col1 = Column(controls=[
            row3,
            row4,
        ])

        row5 = Row(controls=[
            col1,
            col2
        ], alignment=MainAxisAlignment.CENTER)

        self.incomeList = Column()
        self.expenseList = Column()

        return Column(controls=[
            row1,
            row2,
            row5,
            self.incomeList,
            self.expenseList
        ], alignment=MainAxisAlignment.CENTER)
    

    def showTracker(self, e):
        if str(self.tracker.value) == "Income":
            self.incomeList.visible = True
            self.expenseList.visible = False
        else:
            self.incomeList.visible = False
            self.expenseList.visible = True
        self.update()

    def addTracker(self,e):
        if str(self.tracker.value) == "Income":
            self.incomeList.controls.append(IncomeItem(self.description.value, self.amount.value, self.deleteList))
            doc_ref = db.collection("income").document( self.description.value)
            doc_ref.set({
            u'description' : str(self.description.value),
            u'amount' : str(self.amount.value),
        })
        else:
            self.expenseList.controls.append(ExpenseItem(self.description.value,self.amount.value, self.deleteList))
            doc_ref = db.collection("expense").document( self.description.value)
            doc_ref.set({
            u'description' : str(self.description.value),
            u'amount' : str(self.amount.value),
        })
        self.description.value = ""
        self.amount.value = ""
        self.update()

    def deleteList(self,List):
        if str(self.tracker.value) == "Income":
            self.incomeList.controls.remove(List)
        else:
            self.expenseList.controls.remove(List)
        self.update()
    