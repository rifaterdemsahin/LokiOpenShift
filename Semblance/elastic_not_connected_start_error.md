rifaterdemsahin ➜ /workspaces/LokiOpenShift/Symbols/Docker (main) $ docker run -it --name my-running-app3 myapp2:latest
Traceback (most recent call last):
  File "/usr/local/lib/python3.9/site-packages/urllib3/connection.py", line 174, in _new_conn
    conn = connection.create_connection(
  File "/usr/local/lib/python3.9/site-packages/urllib3/util/connection.py", line 72, in create_connection
    for res in socket.getaddrinfo(host, port, family, socket.SOCK_STREAM):
  File "/usr/local/lib/python3.9/socket.py", line 966, in getaddrinfo
    for res in _socket.getaddrinfo(host, port, family, type, proto, flags):
socket.gaierror: [Errno -2] Name or service not known

During handling of the above exception, another exception occurred:

Traceback (most recent call last):
  File "/usr/local/lib/python3.9/site-packages/urllib3/connectionpool.py", line 716, in urlopen
    httplib_response = self._make_request(
  File "/usr/local/lib/python3.9/site-packages/urllib3/connectionpool.py", line 416, in _make_request
    conn.request(method, url, **httplib_request_kw)
  File "/usr/local/lib/python3.9/site-packages/urllib3/connection.py", line 244, in request
    super(HTTPConnection, self).request(method, url, body=body, headers=headers)
  File "/usr/local/lib/python3.9/http/client.py", line 1285, in request
    self._send_request(method, url, body, headers, encode_chunked)
  File "/usr/local/lib/python3.9/http/client.py", line 1331, in _send_request
    self.endheaders(body, encode_chunked=encode_chunked)
  File "/usr/local/lib/python3.9/http/client.py", line 1280, in endheaders
    self._send_output(message_body, encode_chunked=encode_chunked)
  File "/usr/local/lib/python3.9/http/client.py", line 1040, in _send_output
    self.send(msg)
  File "/usr/local/lib/python3.9/http/client.py", line 980, in send
    self.connect()
  File "/usr/local/lib/python3.9/site-packages/urllib3/connection.py", line 205, in connect
    conn = self._new_conn()
  File "/usr/local/lib/python3.9/site-packages/urllib3/connection.py", line 186, in _new_conn
    raise NewConnectionError(
urllib3.exceptions.NewConnectionError: <urllib3.connection.HTTPConnection object at 0x781adfcbad30>: Failed to establish a new connection: [Errno -2] Name or service not known

During handling of the above exception, another exception occurred:

Traceback (most recent call last):
  File "/usr/local/lib/python3.9/site-packages/requests/adapters.py", line 439, in send
    resp = conn.urlopen(
  File "/usr/local/lib/python3.9/site-packages/urllib3/connectionpool.py", line 802, in urlopen
    retries = retries.increment(
  File "/usr/local/lib/python3.9/site-packages/urllib3/util/retry.py", line 594, in increment
    raise MaxRetryError(_pool, url, error or ResponseError(cause))
urllib3.exceptions.MaxRetryError: HTTPConnectionPool(host='none', port=80): Max retries exceeded with url: /events (Caused by NewConnectionError('<urllib3.connection.HTTPConnection object at 0x781adfcbad30>: Failed to establish a new connection: [Errno -2] Name or service not known'))

During handling of the above exception, another exception occurred:

Traceback (most recent call last):
  File "/app/main.py", line 38, in <module>
    main()
  File "/app/main.py", line 30, in main
    es_status = log_to_elasticsearch(event)
  File "/app/main.py", line 12, in log_to_elasticsearch
    response = requests.post(url, headers=headers, data=json.dumps(event))
  File "/usr/local/lib/python3.9/site-packages/requests/api.py", line 117, in post
    return request('post', url, data=data, json=json, **kwargs)
  File "/usr/local/lib/python3.9/site-packages/requests/api.py", line 61, in request
    return session.request(method=method, url=url, **kwargs)
  File "/usr/local/lib/python3.9/site-packages/requests/sessions.py", line 542, in request
    resp = self.send(prep, **send_kwargs)
  File "/usr/local/lib/python3.9/site-packages/requests/sessions.py", line 655, in send
    r = adapter.send(request, **kwargs)
  File "/usr/local/lib/python3.9/site-packages/requests/adapters.py", line 516, in send
    raise ConnectionError(e, request=request)
requests.exceptions.ConnectionError: HTTPConnectionPool(host='none', port=80): Max retries exceeded with url: /events (Caused by NewConnectionError('<urllib3.connection.HTTPConnection object at 0x781adfcbad30>: Failed to establish a new connection: [Errno -2] Name or service not known'))
@rifaterdemsahin ➜ /workspaces/LokiOpenShift/Symbols/Docker (main) $ 