from address import Address
from mailing import Mailing


to_address = Address("34576", "Moscow", "Krylatsky hills", "21", "79")
from_address = Address ("0113", "Tbilisi", "Besarion Chichinadze", "17", "44")

my_mailing = Mailing(to_address, from_address, 4720, "F67")

print("Отправление "+ my_mailing.track + " из", my_mailing.to_address , "в", my_mailing.from_address,  ".Стоимость", my_mailing.cost,  "рублей.")
