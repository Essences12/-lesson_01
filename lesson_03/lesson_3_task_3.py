from address import Address
from mailing import Mailing

to_address = Address('123456', 'Москва', 'Тверская', '10', '25')
from_address = Address('654321', 'Санкт-Петербург', 'Невский', '5', '7')

mailing = Mailing(
    to_address=to_address,
    from_address=from_address,
    cost=350,
    track='TRK123456789',
)

print(
    f'Отправление {mailing.track} из '
    f'{mailing.from_address.index}, {mailing.from_address.city}, '
    f'{mailing.from_address.street}, {mailing.from_address.house} - '
    f'{mailing.from_address.apartment} в '
    f'{mailing.to_address.index}, {mailing.to_address.city}, '
    f'{mailing.to_address.street}, {mailing.to_address.house} - '
    f'{mailing.to_address.apartment}. '
    f'Стоимость {mailing.cost} рублей.'
)