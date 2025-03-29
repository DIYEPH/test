import requests

def post_account(uid, password,cookie,email,otp,useragent):
    try:
        response = requests.post('https://fbapi-5m2g.onrender.com/accounts', json={"email": email, "password": password, "cookie": cookie, "uid": uid, "otp": otp, "useragent": useragent})
        if response.status_code == 200:
            return "success"
        else:
            return None
    except:
        return None

status=post_account("Ấdad","adsd","adsd","adđâsds","adsd","ádad")
print(status)