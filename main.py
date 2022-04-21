

def calc_shipping(distance, size, breakable, workload):
    """Задача. Вам нужно написать функцию расчёта стоимости доставки.

    Стоимость рассчитывается в зависимости от:

    *расстояния до пункта назначения:*

    - более 30 км: +300 рублей к доставке;
    - до 30 км: +200 рублей к доставке;
    - до 10 км: +100 рублей к доставке;
    - до 2 км: +50 рублей к доставке;

    *габаритов груза:*

    - большие габариты: +200 рублей к доставке;
    - маленькие габариты: +100 рублей к доставке;

    *хрупкости груза.* Если груз хрупкий — +300 рублей к доставке. Хрупкие грузы нельзя возить на расстояние более 30 км;

    *загруженности службы доставки*. Стоимость умножается на коэффициент доставки:

    - очень высокая загруженность — 1.6;
    - высокая загруженность — 1.4;
    - повышенная загруженность — 1.2;
    - во всех остальных случаях коэффициент равен 1.

    Минимальная сумма доставки — 400 рублей. Если сумма доставки меньше минимальной, выводится минимальная сумма.

    На входе функция получает расстояние до пункта назначения, габариты, информацию о
    хрупкости, загруженность службы на текущий момент. На выходе пользователь получает стоимость доставки.
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
    workload_rates = {'very high': 1.6, 'high': 1.4, 'increased': 1.2, 'other': 1}
    if workload not in workload_rates:
        workload = 'other'
    delivery_coefficient = workload_rates[workload]
    shipping_cost *= delivery_coefficient
    minimal_shipping_cost = 400
    if shipping_cost < minimal_shipping_cost:
        print('Минимальная сумма доставки - 400 рублей.')
    return f'Стоимость доставки - {round(shipping_cost)} рублей.'


if __name__ == '__main__':
    shipping = calc_shipping(distance=40, size='small', breakable=False, workload='highly')
    print(shipping)
