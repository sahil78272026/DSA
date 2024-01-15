def custom_message(mobile,country_code,otp):

    
    import http.client

    conn = http.client.HTTPSConnection("api.authkey.io")
    url = "https://api.authkey.io/request"
    querystring={
        "authkey":"631d38ba78dd302e",
        "country_code":f"{country_code}",
        "mobile":f"{mobile}",
        "sid":"7965",
        "sms":f"Hello, you have been registered with crosslynx. Your Password is {otp}"
        }

    conn.request("GET",url, querystring)

    res = conn.getresponse()
    data = res.read()

    print(data.decode("utf-8"))

custom_message('8285748373','+91','5431')