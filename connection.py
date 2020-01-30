import connection_dont_touch


@connection_dont_touch.connection_handler
def get_number_of_request_type_by_type_name(cursor, request):
    cursor.execute("""
        SELECT number
        FROM http
        WHERE request = %(request)s
    """,
                   {'request': request})
    number_of_request_type = cursor.fetchall()
    return number_of_request_type


@connection_dont_touch.connection_handler
def insert_new_http(cursor, request, request_type_number):
    cursor.execute("""
        UPDATE http
        SET number = %s
        WHERE request = %s
    """, (request_type_number, request))


@connection_dont_touch.connection_handler
def get_all_data_from_http(cursor):
    cursor.execute("""
        SELECT request, number
        FROM http
        ORDER BY id;
    """)
    all_data = cursor.fetchall()
    return all_data
