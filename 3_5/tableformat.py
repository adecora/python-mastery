# tableformat.py
class TableFormatter:
    def headings(self, headers):
        raise NotImplementedError()

    def row(self, rowdata):
        raise NotImplementedError()


class TextTableFormatter(TableFormatter):
    def headings(self, headers):
        print(' '.join('%10s' % h for h in headers))
        print(('-'*10 + ' ')*len(headers))

    def row(self, rowdata):
        print(' '.join('%10s' % d for d in rowdata))


class CSVTableFormatter(TableFormatter):
    def headings(self, headers):
        print(','.join(headers))
    
    def row(self, rowdata):
        print(','.join(str(d) for d in rowdata))


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


def create_formatter(name):
    if name == 'text':
        formatter_cls = TextTableFormatter
    elif name == 'csv':
        formatter_cls = CSVTableFormatter
    elif name == 'html':
        formatter_cls = HTMLTableFormatter
    else:
        raise RuntimeError('Unknown format %s' % name) 
    return formatter_cls()

def print_table(portfolio, fields, formatter):
    formatter.headings(fields)
    for s in portfolio:
        rowdata = [getattr(s, fieldname, None) for fieldname in fields]
        formatter.row(rowdata)