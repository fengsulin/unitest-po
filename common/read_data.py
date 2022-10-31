import xlrd
import os


class Helper():
    ''' 从excel表中读取数据 '''

    def readData(self, rowx):
        filepath = os.path.dirname(os.path.abspath('.')) + '/data/' + 'login_info.xls'
        book = xlrd.open_workbook(filepath, 'r')
        table = book.sheet_by_index(0)
        # for datavalue in range(1,table.nrows):
        #     datalist.append(table.row_values(datavalue,0,table.ncols))
        return table.row_values(rowx)

    def read_user(self, rowx):
        return self.readData(rowx)[0]

    def read_pwd(self, rowx):
        return self.readData(rowx)[1]

    def read_text(self, rowx):
        return self.readData(rowx)[2]


