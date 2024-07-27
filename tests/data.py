
COURIER_EMPTY_LOGIN = {'login': '', 'password': 'password'}
COURIER_WITHOUT_LOGIN = {'password': 'password'}
COURIER_WITHOUT_PASSWORD = {'login': 'login', 'password': ''}
COURIER_EMPTY_PASSWORD = {'login': 'login', 'password': ''}


# Примеры данных для курьерских запросов
COURIER_DATA_VALID = {
    'login': 'Galina_qa_sprint_7',
    'password': 'password'
}

# Наборы тестовых данных для заказа
ORDER_WITH_SINGLE_COLOR = {
    'first_name': 'Emily',
    'last_name': 'Brown',
    'address': '321 Birch St',
    'metro_station': '5',
    'phone': '5551234567',
    'rent_duration': 1,
    'delivery_date': '2024-06-15T18:00:00.000Z',
    'comment': 'Sample order',
    'color': ['GREY']
}

ORDER_WITH_MULTIPLE_COLORS = {
    'first_name': 'Galyu',
    'last_name': 'Test_ya',
    'address': 'some adress',
    'metro_station': '6',
    'phone': '89997776655',
    'rent_duration': 2,
    'delivery_date': '2024-07-25T18:00:00.000Z',
    'comment': 'some_comment',
    'color': ['BLACK', 'GREY']
}

ORDER_WITHOUT_COLOR = {
    'first_name': 'Test_Galyu_papapa',
    'last_name': 'Second_Name',
    'address': 'Some another adress',
    'metro_station': '7',
    'phone': '8999555433',
    'rent_duration': 3,
    'delivery_date': '2024-07-30T18:00:00.000Z',
    'comment': 'nothing'
}