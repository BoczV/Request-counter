import connection


def insert_new_request_method(request):
    request_type_number = connection.get_number_of_request_type_by_type_name(request)
    print(request_type_number)
    request_type_number[0]["number"] += 1
    connection.insert_new_http(request, request_type_number[0]["number"])


def get_all_data_from_http():
    all_data = connection.get_all_data_from_http()
    return all_data
