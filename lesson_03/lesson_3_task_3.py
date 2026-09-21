from address import Address
from mailing import Mailing

mailing = Mailing(
    Address('123456', 'Москва', 'Тверская', '10', '25'),
    Address('654321', 'Санкт-Петербург', 'Невский', '5', '7'),
    350,
    'TRK123456789',
)

print(f'Отправление {mailing.track} из {mailing.from_address} '
      f'в {mailing.to_address}. Стоимость {mailing.cost} рублей.')