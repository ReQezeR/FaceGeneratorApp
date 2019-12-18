from _tkinter import *
from tkintertable import TableCanvas


class CustomCanvas(TableCanvas):
    def adjustColumnWidths(self):
        try:
            fontsize = self.thefont[1]
        except:
            fontsize = self.fontsize
        scale = 8.5 * float(fontsize) / 12
        for col in range(self.cols):
            colname = self.model.getColumnName(col)
            if colname in self.model.columnwidths:
                w = self.model.columnwidths[colname]
            else:
                w = self.cellwidth
            maxlen = self.model.getlongestEntry(col)
            size = maxlen * scale
            if size < w:
                continue
            # if size >= self.maxcellwidth:
            #    size = self.maxcellwidth
            self.model.columnwidths[colname] = size * 1.2  # I changed the calculation to a static float
        return
