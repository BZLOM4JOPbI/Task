def get_filters_from_request(request):

    type_of_derm = request.query_params.get('d').split(',')
    brand = request.query_params.get('b').split(',')
    product_for_who = request.query_params.get('w').split(',')

    return [type_of_derm, brand, product_for_who]
