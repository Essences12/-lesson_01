from smartphone import Smartphone

catalog = [
    Smartphone('Apple', 'iPhone 15', '+79000000001'),
    Smartphone('Samsung', 'Galaxy S24', '+79000000002'),
    Smartphone('Xiaomi', 'Redmi Note 13', '+79000000003'),
    Smartphone('Huawei', 'P60 Pro', '+79000000004'),
    Smartphone('Google', 'Pixel 8', '+79000000005'),
]

for smartphone in catalog:
    print(f'{smartphone.brand} - {smartphone.model}. '
          f'{smartphone.phone_number}')