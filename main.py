from database.models import create_tables
from gui.views.main_window import MainWindow

create_tables()

app = MainWindow()
app.run()