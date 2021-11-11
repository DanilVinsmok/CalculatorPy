from PyQt5 import QtCore, QtGui, QtWidgets
import sys
from form import Ui_MyWindow

app = QtWidgets.QApplication(sys.argv)

MyWindow = QtWidgets.QWidget()
ui = Ui_MyWindow()
ui.setupUi(MyWindow)
MyWindow.show()


def Bt0():
    dano = ui.LineEd.text()
    ui.LineEd.setText(dano+"0")


def Bt1():
    dano = ui.LineEd.text()
    ui.LineEd.setText(dano+"1")


def Bt2():
    dano = ui.LineEd.text()
    ui.LineEd.setText(dano+"2")


def Bt3():
    dano = ui.LineEd.text()
    ui.LineEd.setText(dano+"3")


def Bt4():
    dano = ui.LineEd.text()
    ui.LineEd.setText(dano+"4")


def Bt5():
    dano = ui.LineEd.text()
    ui.LineEd.setText(dano+"5")


def Bt6():
    dano = ui.LineEd.text()
    ui.LineEd.setText(dano+"6")


def Bt7():
    dano = ui.LineEd.text()
    ui.LineEd.setText(dano+"7")


def Bt8():
    dano = ui.LineEd.text()
    ui.LineEd.setText(dano+"8")


def Bt9():
    dano = ui.LineEd.text()
    ui.LineEd.setText(dano+"9")


def Separator():
    dano = ui.LineEd.text()
    ui.LineEd.setText(dano + ".")


mas = ["+", "-", "/", "*"]


def Calculations():
    dano = ui.LineEd.text()
    for i in mas:
        leng = dano.split(i)
        if len(leng) > 1:
            for i in dano:
                if i == "+":
                    ui.LineEd.setText(str(float(leng[0])+float(leng[1])))
                if i == "-":
                    ui.LineEd.setText(str(float(leng[0])-float(leng[1])))
                if i == "*":
                    ui.LineEd.setText(str(float(leng[0])*float(leng[1])))
                if i == "/":
                    ui.LineEd.setText(str(float(leng[0])/float(leng[1])))


def IfTwoNums():
    dano = ui.LineEd.text()
    for i in dano:
        for j in mas:
            if i == j:
                return True


def Minus():
    if IfTwoNums():
        Calculations()
    ui.LineEd.setText(ui.LineEd.text()+"-")
    ui.lb1.setText(ui.lb1.text() + "\n-")


def Plus():
    if IfTwoNums():
        Calculations()
    ui.LineEd.setText(ui.LineEd.text()+"+")
    ui.lb1.setText(ui.lb1.text() + "\n+")


def Multiply():
    if IfTwoNums():
        Calculations()
    ui.LineEd.setText(ui.LineEd.text()+"*")
    ui.lb1.setText(ui.lb1.text() + "\n*")


def Division():
    if IfTwoNums():
        Calculations()
    ui.LineEd.setText(ui.LineEd.text()+"/")
    ui.lb1.setText(ui.lb1.text() + "\n/")


def Cube():
    if IfTwoNums():
        Calculations()
    ui.LineEd.setText(str(pow(float(ui.LineEd.text()), 2)))
    ui.lb1.setText(ui.lb1.text() + "\n^2")

def Equally():
    if IfTwoNums():
        Calculations()


def Reset():
    ui.LineEd.setText("")
    ui.lb1.setText("")


ui.Button0.pressed.connect(Bt0)
ui.Button1.pressed.connect(Bt1)
ui.Button2.pressed.connect(Bt2)
ui.Button3.pressed.connect(Bt3)
ui.Button4.pressed.connect(Bt4)
ui.Button5.pressed.connect(Bt5)
ui.Button6.pressed.connect(Bt6)
ui.Button7.pressed.connect(Bt7)
ui.Button8.pressed.connect(Bt8)
ui.Button9.pressed.connect(Bt9)
ui.ButtonSeparator.pressed.connect(Separator)
ui.ButtonMinus.clicked.connect(Minus)
ui.ButtonPlus.clicked.connect(Plus)
ui.ButtonMultiply.clicked.connect(Multiply)
ui.ButtonDivision.clicked.connect(Division)
ui.ButtonCube.clicked.connect(Cube)
ui.ButtonEqually.clicked.connect(Equally)
ui.ButtonReset.clicked.connect(Reset)

sys.exit(app.exec_())