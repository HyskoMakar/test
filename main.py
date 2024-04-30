from PySide6.QtWidgets import QApplication, QPushButton

app = QApplication([])
button = QPushButton("Привіт, світ!")
button.resize(300, 200)

button.show()
app.exec()