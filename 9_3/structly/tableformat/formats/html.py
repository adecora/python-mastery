# formats/html.py
from ..formatter import TableFormatter


class HTMLTableFormatter(TableFormatter):
    def headings(self, headings):
        print('<tr>', end=' ')
        for h in headings:
            print('<th>%s</th>' % h, end=' ')
        print('</tr>')

    def row(self, rowdata):
        print('<tr>', end=' ')
        for d in rowdata:
            print('<td>%s</td>' % d, end=' ')
        print('</tr>')
