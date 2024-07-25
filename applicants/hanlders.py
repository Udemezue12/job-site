from django.shortcuts import render


def unauthorized_request(request, exception):
    return render('request', 'error_pages/401.html', status=401)


def bad_request(request, exception):
    return render('request', 'error_pages/400.html', status=400)


def forbidden(request, exception):
    return render('request', 'error_pages/403.html'), 403


def page_not_found(request, exception):
    return render("request", "error_pages/404.html", status=404)


def method_not_allowed(request, exception):
    return render('request', 'error_pages/405.html', status=405)


def not_acceptable_request(request, exception):
    return render('request', 'error_pages/406.html', status=406)


def request_timeout_request(request, exception):
    return render('request', 'error_pages/408.html', status=408)


def conflict_request(request, exception):
    return render('request', 'error_pages/409.html', status=409)


def gone_request(request, exception):
    return render('request', 'error_pages/410.html'), 410


def length_required_request(request, exception):
    return render('request', 'error_pages/411.html', status=411)


def precondition_failed_request(request, exception):
    return render('request', 'error_pages/412.html', status=412)


def payload_too_large_request(request, exception):
    return render('request', 'error_pages/413.html', status=413)


def uri_too_long_request(request, exception):
    return render('request', 'error_pages/414.html', status=414)


def unsupported_media_type_request(request, exception):
    return render('request', 'error_pages/415.html', status=415)


def range_not_satisfiable_request(request, exception):
    return render('request', 'error_pages/416.html', status=416)


def expectation_failed_request(request, exception):
    return render('request', 'error_pages/417.html', status=417)


def im_a_teapot_request(request, exception):
    return render('request', 'error_pages/418.html', status=418)


def unprocessable_entity_request(request, exception):
    return render('request', 'error_pages/422.html', status=422)


def locked_request(request, exception):

    return render('request', 'error_pages/423.html', status=423)


def failed_dependency_request(request, exception):
    return render('request', 'error_pages/424.html', status=424)


def precondition_required_request(request, exception):
    return render('request', 'error_pages/428.html', status=428)


def too_many_requests_request(request, exception):
    return render('request', 'error_pages/429.html', status=429)


def request_header_fields_too_large_request(request, exception):
    return render('request', 'error_pages/431.html', status=431)


def unavailable_for_legal_reasons_request(request, exception):
    return render('request', 'error_pages/451.html', status=451)


def internal_server_request(request, exception):
    return render('request', 'error_pages/500.html', status=500)


def not_implemented_request(request, exception):
    return render('request', 'error_pages/501.html', status=501)


def bad_gateway_request(request, exception):
    return render('request', 'error_pages/502.html', status=502)


def service_unavailable_request(request, exception):
    return render('request', 'error_pages/503.html', status=503)


def gateway_timeout_request(request, exception):
    return render('request', 'error_pages/504.html', status=504)


def http_version_not_supported_request(request, exception):
    return render('request', 'error_pages/505.html', status=505)
