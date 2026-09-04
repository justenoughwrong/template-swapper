'''Template Swapper main script.'''

from pathlib import Path

import pyperclip
from PySide6.QtWidgets import QApplication, QMainWindow

from mainwindow import Ui_MainWindow

HTML = Path().cwd() / 'html'
HTML_GUNBROKER = Path(HTML / 'gunbroker')
HTML_WEBSITE = Path(HTML / 'website')


class MainWindow(QMainWindow, Ui_MainWindow):
    '''GUI's main window widget.'''

    def __init__(self) -> None:  # noqa: D107
        super().__init__()
        self.setupUi(self)

        for template in HTML_WEBSITE.iterdir():
            self.templateSelect.addItem(template.stem.title())

        # Signal Connections
        self.templateSelectionButtonGroup.buttonToggled.connect(
            self.set_template_choices)
        self.templateSelect.currentIndexChanged.connect(self.set_display_text)

    def set_template_choices(self) -> None:
        '''Changes available template choices in selection widget.'''
        self.templateSelect.clear()
        match self.templateSelectionButtonGroup.checkedButton():
            case self.websiteRadioButton:
                for template in HTML_WEBSITE.iterdir():
                    self.templateSelect.addItem(template.stem.title())
            case self.gunbrokerRadioButton:
                for template in HTML_GUNBROKER.iterdir():
                    self.templateSelect.addItem(template.stem.title())

    def set_display_text(self) -> None:
        '''Changes display text to reflect html in file.

        Checks html file using self.comboBox's current item text.
        Changes textDisplay's placeholder text to html file's content.
        '''
        filename = self.templateSelect.currentText().lower() + '.html'
        match self.templateSelectionButtonGroup.checkedButton():
            case self.websiteRadioButton:
                file = Path(HTML_WEBSITE / filename)
            case self.gunbrokerRadioButton:
                file = Path(HTML_GUNBROKER / filename)
        self.textBrowser.setText(file.read_text())
        pyperclip.copy(file.read_text())


app = QApplication()
window = MainWindow()
window.show()
app.exec()
