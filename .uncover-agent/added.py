        'href': f"{api.base_url}/?f={F_JSON}"
        'href': f"{api.base_url}/?f={F_JSONLD}"
        'href': f"{api.base_url}/?f={F_HTML}",
        'href': f"{api.base_url}/?f={F_JSON}"
        'href': f"{api.base_url}/?f={F_HTML}"
        'href': f"{api.base_url}/?f={F_JSON}"
        'href': f"{api.base_url}/?f={F_HTML}"
            job_result_url = f"{api.base_url}/jobs/{job_['identifier']}/results?f={F_JSON}"  # noqa
                'title': f"Results of job {job_['identifier']} as {job_['mimetype']}"  # noqa
    elif request.format == F_HTML:
        headers['Content-Type'] = "text/html"
        data = {
            'job': {'id': job_id},
            'result': job_output
        }
        content = render_j2_template(
            api.config, api.config['server']['templates'],
            'jobs/results/index.html', data, request.locale)
        content = json.dumps(job_output, sort_keys=True, indent=4,
                             default=json_serial)
    assert root['links'][1]['href'].endswith('/?f=json')
    assert any(link['href'].endswith('/?f=jsonld') and link['rel'] == 'alternate'  # noqa
    assert any(link['href'].endswith('/?f=html') and link['rel'] == 'alternate'  # noqa