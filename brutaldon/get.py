from requests import Request, Session

def get(url, params=None):
    request = Request('GET', url, None, params=params)
    with Session() as session:
        prepared = session.prepare_request(request)
        settings = session.merge_environment_settings(prepared.url, {}, None, None, None)
        response = session.send(prepared, **settings)
    return response

def get_instance(domain):
    return get("https://{}/api/v1/instance".format(domain)).json()

def get_timeline(domain, timeline, params=None):
    print("https://{}/api/v1/timelines/{}".format(domain, timeline))
    return get("https://{}/api/v1/timelines/{}".format(domain, timeline)).json()

#print(get_instance("chitter.xyz")['uri'])
