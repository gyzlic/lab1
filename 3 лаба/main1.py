# TODO Напишите функцию для поиска индекса товара


items_list = ['яблоко', 'банан', 'апельсин', 'груша', 'киви', 'банан']

for find_item in ['банан', 'груша', 'персик']:
    try:
        index_item = items_list.index(find_item)
        print(f"Первое вхождение товара '{find_item}' имеет индекс {index_item}.")
    except ValueError:
        print(f"Товар '{find_item}' не найден в списке.")
