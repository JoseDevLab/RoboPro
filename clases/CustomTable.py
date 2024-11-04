from PySide6.QtCore import QSize, QTimer, Qt
from PySide6.QtWidgets import QTableWidget, QTableWidgetItem, QSizePolicy
def create_centered_item(text):
    item = QTableWidgetItem(text)
    item.setTextAlignment(Qt.AlignCenter)
    return item
class CustomTable(QTableWidget):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.tiempoAjustar = 100
        self.setSizePolicy(QSizePolicy.Fixed, QSizePolicy.Fixed)
        self.prefijoColumn = ''
        self.prefijoRow = ''
        self.columns = 0
        self.rows = 0
        self.isEditable = True
        self.verticalHeader().setVisible(False)
        self.horizontalHeader().setVisible(False)
        self.vLabelVisible = False
        self.hLabelVisible = False
        
        self.timer = QTimer(self)
        self.timer.timeout.connect(self.ajustar)
        
        self.itemChanged.connect(lambda item: self.adjustSizeToContent())
        self.clicked.connect(lambda item: self.adjustSizeToContent())
        
    def showEvent(self, event):
        super().showEvent(event)
        self.adjustSizeToContent()

    def setTable(self, table):
        self.rows = len(table)
        self.columns  = len(table[0]) if table else 0
        self.setRowCount(self.rows)
        self.setColumnCount(self.columns)
        for row_index, row in enumerate(table):
            for col_index, item in enumerate(row):
                self.setItem(row_index, col_index, self.create_centered_item(str(item)))
        self.timer.start(self.tiempoAjustar)

    def create_centered_item(self,text):
        item = QTableWidgetItem(text)
        item.setTextAlignment(Qt.AlignCenter)
        if not self.isEditable:
            item.setFlags(item.flags() & ~Qt.ItemIsEditable)
        return item

    def getTable(self):
        rows, cols = self.rowCount(), self.columnCount()
        return [[self.item(row, col).text() if self.item(row, col) else "" for col in range(cols)] for row in range(rows)]

    def setSize(self, row, column):
        self.setRowCount(row)
        self.setColumnCount(column)
        self.add_size(row, column)
        self.rows = row
        self.columns = column
        self.adjustSizeToContent()
        
    def setRowS(self,row):
        self.setRowCount(row)
        self.add_row(row)
        self.rows = row
        self.adjustSizeToContent()
        
    def setColumnS(self,column):
        self.setColumnCount(column)
        self.add_column(column)
        self.columns = column
        self.adjustSizeToContent()

    def adjustSizeToContent(self):
        self.resizeColumnsToContents()
        self.resizeRowsToContents()
        total_width = self.calculateTotalWidth()
        total_height = self.calculateTotalHeight()
        self.setMinimumWidth(total_width + 2)
        self.setMinimumHeight(total_height + 2)

    def sizeHint(self):
        width = self.calculateTotalWidth()
        height = self.calculateTotalHeight()
        return QSize(width, height)

    def calculateTotalWidth(self):
        width = sum([self.columnWidth(col) for col in range(self.columnCount())])
        if self.vLabelVisible:
            width += self.verticalHeader().width()
        return width

    def calculateTotalHeight(self):
        height = sum([self.rowHeight(row) for row in range(self.rowCount())])
        if self.hLabelVisible:
            height += self.horizontalHeader().height()
        return height

    def setAxisLabelsVisible(self, visible:bool):
        self.horizontalHeader().setVisible(visible)
        self.verticalHeader().setVisible(visible)
        self.hLabelVisible = visible
        self.vLabelVisible = visible
        self.timer.start(self.tiempoAjustar)  # Intervalo de verificación en milisegundos
        
    def setHLabelsVisible(self, visible:bool):
        self.horizontalHeader().setVisible(visible)
        self.hLabelVisible = visible
        self.timer.start(self.tiempoAjustar)
        
    def setVLabelsVisible(self, visible:bool):
        self.verticalHeader().setVisible(visible)
        self.vLabelVisible = visible
        self.timer.start(self.tiempoAjustar)
        
    def ajustar(self):
        self.adjustSizeToContent()
        self.timer.stop()
    
    def set_column_prefix(self, prefix:str):
        self.prefijoColumn = prefix
        column_count = self.columnCount()
        for i in range(column_count):
            self.setHorizontalHeaderItem(i, QTableWidgetItem(f"{self.prefijoColumn}{i+1}"))
    
    def set_row_prefix(self, prefix:str):
        self.prefijoRow = prefix
        row_count = self.rowCount()
        for i in range(row_count):
            self.setVerticalHeaderItem(i, QTableWidgetItem(f"{self.prefijoRow}{i+1}"))
    
    def add_column(self, column:int):
        for i in range(self.columns,column,1):
            self.setHorizontalHeaderItem(i, QTableWidgetItem(f"{self.prefijoColumn}{i+1}"))
        for j in range(self.columns,column,1):
            for i in range(self.rows):
                self.setItem(i, j, self.create_centered_item('0'))
    
    def add_row(self, row:int):
        for i in range(self.rows,row,1):
            self.setVerticalHeaderItem(i, QTableWidgetItem(f"{self.prefijoRow}{i+1}"))
        for i in range(self.rows,row,1):
            for j in range(self.columns):
                self.setItem(i, j, self.create_centered_item('0'))
    
    def add_size(self,row,column):
        for i in range(self.rows,row,1):
            self.setVerticalHeaderItem(i, QTableWidgetItem(f"{self.prefijoRow}{i+1}"))
            
        for i in range(self.columns,column,1):
            self.setHorizontalHeaderItem(i, QTableWidgetItem(f"{self.prefijoColumn}{i+1}"))
        
        for i in range(self.rows,row,1):
            for j in range(column):
                self.setItem(i, j, self.create_centered_item('0'))
                
        for j in range(self.columns,column,1):
            for i in range(row):
                self.setItem(i, j, self.create_centered_item('0'))
    
    def setEditable(self, editable:bool):
        self.isEditable = editable
        for i in range(self.rows):
            for j in range(self.columns):
                item = self.item(i, j)
                if item:  # Verificar si el ítem existe
                    item.setFlags(item.flags() & ~Qt.ItemIsEditable)