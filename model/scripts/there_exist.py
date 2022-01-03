def there_exist(voice_data, terms):
    """ Identificação da existencia dos termos na fala """
    for term in terms:
        if term in voice_data:
            return True