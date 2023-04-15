def get_filters_from_request(request):

    type_of_derm = request.query_params.get('d')
    brand = request.query_params.get('b')
    product_for_who = request.query_params.get('w')

    filters_for_product = [type_of_derm, brand, product_for_who]
    for index, filter_for_field in enumerate(filters_for_product):
        try:
            filters = filter_for_field.split(',')
            filters_for_product[index] = filters
        except (AttributeError, TypeError):
            filters_for_product[index] = []
    
    return filters_for_product
