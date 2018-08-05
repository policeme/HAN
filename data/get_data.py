
import os
import re
import xlrd
import xlwt

file_path = os.path.dirname(os.path.realpath(__file__))

class DataProcess(object):
    def read_data(self, file_path):
        """
        this function is able to read news from excel
        :return: data list
        """
        excel_file = xlrd.open_workbook(file_path)
        sheet = excel_file.sheet_by_index(0)
        data_list = []
        for i in range(0, sheet.nrows):
            sub_list = []
            title = sheet.cell_value(i, 0)
            content = sheet.cell_value(i, 1)
            label = sheet.cell_value(i, 2)
            if title == '' or len(content) < 100:
                continue
            title = self.regular_content(title)
            content = self.regular_content(content)
            sub_list.append(title)
            sub_list.append(content)
            sub_list.append(label)
            data_list.append(sub_list)

        return data_list

    def regular_content(self, title):
        """
        this function is able to regular content
        :param title: news title
        :return: regular title
        """
        title = ''.join(re.findall(u'[\u4e00-\u9fff]+', title))
        title = re.sub('|', '', title)

        return title

    def write_excel(self, file_name, data):
        """
        this function is able to save data to excel
        :param data: data list
        :return:
        """
        book = xlwt.Workbook()
        sheet = book.add_sheet('sheet1')
        c = 0
        for d in data:
            for index in range(len(d)):
                sheet.write(c, index, d[index])
            c += 1
        book.save(file_name)
        print(c, 'save success....')

if __name__ == '__main__':
    dp = DataProcess()
    normal_news = dp.read_excel(r'F:\education\prediction.xls')
    garbage_news = dp.read_excel(r'F:\education\prediction.xls', True)
    dp.write_excel(r'F:\education\garbage_news.xls', garbage_news)
    dp.write_excel(r'F:\education\normal_news.xls', normal_news)