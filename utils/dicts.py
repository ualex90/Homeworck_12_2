def get_val(collection: dict, key, default='git'):
    """
    Функция возвращает значение из словаря по переданному ключу, если ключ существует.
    В ином случае возвращается значение по-умолчанию
    :param collection: исходный словарь
    :param key: искомый ключ
    :param default: значение по-умолчанию
    :return: значение из словаря по ключу или по-умолчанию
    """
    val = collection.get(key)
    value = val if val else default
    return value
