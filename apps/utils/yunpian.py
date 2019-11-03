import requests
import json


class YunPian(object):
    def __init__(self,api_key):
        self.api_key = api_key
        self.single_send_url = "https://sms.yunpian.com/v2/sms/single_send.json"

    def send_sms(self,code,phone):
        parmas = {
            "apikey":self.api_key,
            "mobile":phone,
            "text":"【云片网】您的验证码是{code}".format(code=code),
        }

        response = requests.post(self.single_send_url,data=parmas)
        re_dict = json.loads(response.text)
        return re_dict


if __name__ == '__main__':
    yun_pian = YunPian("b6d906c93c3d6dd2f79e3a93a7f13722")
    yun_pian.send_sms("2019","15219740694")
