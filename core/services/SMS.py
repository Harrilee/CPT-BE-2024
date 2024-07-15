# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
import sys

from typing import List

from alibabacloud_tea_openapi.client import Client as OpenApiClient
from alibabacloud_tea_openapi import models as open_api_models
from alibabacloud_tea_util import models as util_models
from alibabacloud_openapi_util.client import Client as OpenApiUtilClient


class SmsService:
    with open('access_key_ID.txt') as f:
        access_key_id = f.read().strip()
    with open('access_key_secret.txt') as f:
        access_key_secret = f.read().strip()

    @staticmethod
    def create_client(
        access_key_id: str,
        access_key_secret: str,
    ) -> OpenApiClient:
        """
        使用AK&SK初始化账号Client
        @param access_key_id:
        @param access_key_secret:
        @return: Client
        @throws Exception
        """
        config = open_api_models.Config(
            # 必填，您的 AccessKey ID,
            access_key_id=access_key_id,
            # 必填，您的 AccessKey Secret,
            access_key_secret=access_key_secret
        )
        # 访问的域名
        config.endpoint = f'dysmsapi.aliyuncs.com'
        return OpenApiClient(config)

    @staticmethod
    def create_api_info() -> open_api_models.Params:
        """
        API 相关
        @param path: params
        @return: OpenApi.Params
        """
        params = open_api_models.Params(
            # 接口名称,
            action='SendSms',
            # 接口版本,
            version='2017-05-25',
            # 接口协议,
            protocol='HTTPS',
            # 接口 HTTP 方法,
            method='POST',
            auth_type='AK',
            style='RPC',
            # 接口 PATH,
            pathname=f'/',
            # 接口请求体内容格式,
            req_body_type='json',
            # 接口响应体内容格式,
            body_type='json'
        )
        return params

    @staticmethod
    def send(phone_number:str,code:str) -> dict:
        # 工程代码泄露可能会导致AccessKey泄露，并威胁账号下所有资源的安全性。以下代码示例仅供参考，建议使用更安全的 STS 方式，更多鉴权访问方式请参见：https://help.aliyun.com/document_detail/378659.html
        client = SmsService.create_client(SmsService.access_key_id, SmsService.access_key_secret)
        params = SmsService.create_api_info()
        # query params
        queries = {}
        queries['PhoneNumbers'] = f'{phone_number}'
        # queries['PhoneNumbers'] = '18918311300'
        queries['SignName'] = '上纽大压力与健康研究'
        queries['TemplateCode'] = 'SMS_225121390'
        queries['TemplateParam'] = f'{{"code":"{code}"}}'
        # queries['TemplateParam'] = '{"code":"4561"}'

        # runtime options
        runtime = util_models.RuntimeOptions()
        request = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(queries)
        )
        # 复制代码运行请自行打印 API 的返回值
        # 返回值为 Map 类型，可从 Map 中获得三类数据：响应体 body、响应头 headers、HTTP 返回的状态码 statusCode
        return client.call_api(params, request, runtime)
    
    @staticmethod
    def sendMsg(phone_number:str, templete_code:str):
        client = SmsService.create_client(SmsService.access_key_id, SmsService.access_key_secret)
        params = SmsService.create_api_info()
        queries = {}
        queries['PhoneNumbers'] = f'{phone_number}'
        queries['SignName'] = '上纽大压力与健康研究'
        queries['TemplateCode'] = f'{templete_code}'
        runtime = util_models.RuntimeOptions()
        request = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(queries)
        )
        return client.call_api(params, request, runtime)



    @staticmethod
    async def send_async(
        args: List[str],
    ) -> None:
        # 工程代码泄露可能会导致AccessKey泄露，并威胁账号下所有资源的安全性。以下代码示例仅供参考，建议使用更安全的 STS 方式，更多鉴权访问方式请参见：https://help.aliyun.com/document_detail/378659.html
        client = SmsService.create_client(SmsService.access_key_id, SmsService.access_key_secret)
        params = SmsService.create_api_info()
        # query params
        queries = {}
        queries['PhoneNumbers'] = '18918311300'
        queries['SignName'] = '上纽大压力与健康研究'
        queries['TemplateCode'] = 'SMS_225121390'
        queries['TemplateParam'] = '{"code":"4321"}'
        # runtime options
        runtime = util_models.RuntimeOptions()
        request = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(queries)
        )
        # 复制代码运行请自行打印 API 的返回值
        # 返回值为 Map 类型，可从 Map 中获得三类数据：响应体 body、响应头 headers、HTTP 返回的状态码 statusCode
        await client.call_api_async(params, request, runtime)



if __name__ == '__main__':
    a = {'body': {'Message': 'OK', 'RequestId': '77F2F489-7175-54F7-9F95-121DFCF982D5', 'Code': 'OK',
                  'BizId': '407805875367551256^0'},
         'headers': {'date': 'Thu, 02 Feb 2023 19:52:31 GMT', 'content-type': 'application/json;charset=utf-8',
                     'content-length': '110', 'connection': 'keep-alive', 'access-control-allow-origin': '*',
                     'x-acs-request-id': '77F2F489-7175-54F7-9F95-121DFCF982D5',
                     'x-acs-trace-id': '3c061b4e6176b5b6e538078867f84b36'},
         'statusCode': 200}


# import json
#
# import requests
#
#
# def send(number:str,code:str):
#     # post request with from data to localhost
#     url = 'https://rookietherapist.hosting.nyu.edu/SMS_Server/src/sms.php'
#     data = { 'number': number, 'code': code }
#     res = requests.post(url, data=data)
#     return res
#
#
# if __name__ == '__main__':
#     res = send('110','6699')
#     print(res.status_code)
#     print(res.text)