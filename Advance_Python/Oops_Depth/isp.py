# ❌ WRONG DESIGN (forced methods)
# class OfficeDevice:
#     def print(self):
#         pass
#     def scan(self):
#         pass
#     def fax(self):
#         pass
#
# class BasicPrinter(OfficeDevice):
#     def scan(self):
#         raise Exception("Not supported")


# ✅ CORRECT DESIGN

class Printer:
    def print(self, document):
        print(f"Printing {document}")


class Scanner:
    def scan(self, document):
        print(f"Scanning {document}")


class FaxMachine:
    def fax(self, document):
        print(f"Faxing {document}")


class MultiFunctionPrinter(Printer, Scanner, FaxMachine):
    pass


printer = Printer()
printer.print("Report.pdf")

mfp = MultiFunctionPrinter()
mfp.scan("Invoice.pdf")
