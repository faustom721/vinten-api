def get_request_company(request):
    print(request.method)
    if request.method == 'GET':
        return request.query_params.get('company')
    else:
        return request.data.get('company')
