from pyexpat.errors import messages


class Printer:
    def print_message(self, message ):
        print(f"Drukowanie wiadomosci {message}")


class Scaner:
    def scan_document(self):
        print(f"Skanowanie dokumenut ")
        return "Zawartosc dokumentu"


class MultifunkcjonDevice (Printer, Scaner):
    def photocopy(self):
        content= self.scan_document()
        self.print_message(content)

device=MultifunkcjonDevice()
device.photocopy()

device.print_message("Komunikat")

message=device.scan_document()
print("Odczytany komunikat:", message)
print (MultifunkcjonDevice.__mro__)