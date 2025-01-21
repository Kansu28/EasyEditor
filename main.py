import os

from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QApplication, QWidget, QPushButton, QListWidget, QLabel, QHBoxLayout, QVBoxLayout, \
    QFileDialog

from image_processor import ImageProcessor

app = QApplication([])
window = QWidget()
window.setWindowTitle("Easy Editor")
window.resize(700, 500)

btn_dir = QPushButton("Папка")
lb_image = QLabel("тут буде картинка")
lw_files = QListWidget()

btn_inv = QPushButton("Инвентировать")
btn_left = QPushButton("Влево")
btn_right = QPushButton("Вправо")
btn_flip = QPushButton("Отзеркалить")
btn_bw = QPushButton("ЧБ")

main_row = QHBoxLayout()
col1 = QVBoxLayout()
col2 = QVBoxLayout()
row_tools = QHBoxLayout()


row_tools.addWidget(btn_left)
row_tools.addWidget(btn_right)
row_tools.addWidget(btn_flip)
row_tools.addWidget(btn_bw)
row_tools.addWidget(btn_inv)

col2.addWidget(lb_image)
col2.addLayout(row_tools)
col1.addWidget(btn_dir)
col1.addWidget(lw_files)

main_row.addLayout(col1, stretch=1)
main_row.addLayout(col2, stretch=3)
window.setLayout(main_row)

workdir = ""


def filter(files, extensions):
    result = []
    for file in files:
        for ex in extensions:
            if file.endswith(ex):
                result.append(file)
    return result


def chooseWorkDir():
    global workdir
    workdir = QFileDialog.getExistingDirectory()


def showFilenameList():
    extensions = [".jpg", ".jpeg", ".png", ".gif", ".bmp"]
    chooseWorkDir()
    filenames = filter(os.listdir(workdir), extensions)
    lw_files.clear()
    lw_files.addItems(filenames)


def showChosenImage():
    file_name = lw_files.currentItem().text()
    workimage.loadImage(workdir, file_name)
    image_path = os.path.join(workimage.dir, workimage.filename)
    workimage.showImage(image_path, lb_image)


workimage = ImageProcessor()

lw_files.currentRowChanged.connect(showChosenImage)

btn_inv.clicked.connect(workimage.do_invert)
btn_dir.clicked.connect(showFilenameList)
btn_bw.clicked.connect(workimage.do_bw)
btn_right.clicked.connect(workimage.do_right)
btn_flip.clicked.connect(workimage.do_flip)
btn_left.clicked.connect(workimage.do_left)

window.setStyleSheet("""
    QWidget{
        background-color:#FFFAFA;
        font-size:20px;
    }
    QPushButton{
        background-color:#04d15d;
        border:3px dashed #038a3d;
        border-radius:5px;
    }
    QPushButton:hover{
        background-color: #038a3d;
        border:3px dashed #04d15d;
        border-radius:5px;
    }
    QListWidget{
        background-color: #808080;

    }
    QListWidget::item:selected{
        background-color: #800000;
        color: white;
    }
     QListWidget::item:hover{
        background-color: #A52A2A;
        color: white;

    }
""")

window.show()

app.exec_()