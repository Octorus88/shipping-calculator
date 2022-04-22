def calc_shipping_cost(distance: int, size: str, breakable: bool, workload: str):
    """
    :param distance: расстояние до пункта назначения
    :param size: габариты груза
    :param breakable: хрупкость груза
    :param workload: загруженность службы доставки
    :return: shipping_cost: стоимость доставки
    """
    shipping_cost = 0
    if distance > 30:
        shipping_cost += 300
    if 10 < distance <= 30:
        shipping_cost += 200
    if 2 < distance <= 10:
        shipping_cost += 100
    if distance <= 2:
        shipping_cost += 50
    if size == 'large':
        shipping_cost += 200
    if size == 'small':
        shipping_cost += 100
    if breakable:
        if distance > 30:
            exit('Хрупкие грузы нельзя возить на расстояние более 30 км')
        shipping_cost += 300
    workload_rates = {'very high': 1.6, 'high': 1.4, 'increased': 1.2}
    try:
        delivery_coefficient = workload_rates[workload]
    except KeyError:
        delivery_coefficient = 1
    shipping_cost *= delivery_coefficient
    min_shipping_cost = 400
    if shipping_cost < min_shipping_cost:
        print('Минимальная сумма доставки - 400 рублей.')
    return shipping_cost


if __name__ == '__main__':
    shipping = calc_shipping_cost(distance=40, size='small', breakable=False, workload='highly')
    print(shipping)
