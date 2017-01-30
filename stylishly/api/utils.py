def register_resources(app, api_resources):
    for resource, endpoints in api_resources.items():
        _init_resource(app, resource, endpoints)


def _init_endpoint(resource, function_name, route_rules):
    endpoint_function = getattr(resource, function_name)
    route, methods, options = route_rules
    resource.blueprint.add_url_rule(route, view_func=endpoint_function,
                                    methods=methods, **options)


def _init_resource(app, resource, endpoints):
    log = []
    for endpoint in endpoints.items():
        _init_endpoint(resource, *endpoint)
        log.append('\nADDED API {} RESOURCE {}.{}: '
                   '{}'.format(resource.blueprint.url_prefix,
                               resource.__name__, *endpoint))
    app.logger.info(''.join(log))
    app.register_blueprint(resource.blueprint)
