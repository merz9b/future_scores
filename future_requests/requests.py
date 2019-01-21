from requests import request
import json


def handle_data(data):
    result = dict(
        ExamDate=data['ExamDate'],
        ExamPlace=data['ExamPlace'],
        ExamScore=data['ExamScore'],
        SubjectName=data['SubjectName']
    )
    return result


def handle_response(resp):
    json_resp = resp.json()
    json_data = json_resp['Data']
    return list(map(handle_data, json_data))


def request_future_score(name, id_number):
    headers = {
        'Pragma': 'no-cache',
        'Origin': 'http://exam.cfachina.org',
        'Accept-Encoding': 'gzip, deflate',
        'Accept-Language': 'zh-CN,zh;q=0.9',
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/71.0.3578.98 Safari/537.36',
        'Content-Type': 'application/json;charset=UTF-8',
        'Accept': 'application/json, text/plain, */*',
        'Cache-Control': 'no-cache',
        'APIKey': '116ce9c7-186e-43cd-87fb-1263ad263262',
        'Connection': 'keep-alive',
        'Referer': 'http://exam.cfachina.org/cjcx/',
    }

    url = 'http://exam.cfachina.org/SiteService/GradesQueryService/GetUserGradesQuery'

    req_data = {
        "fExamUserName": name,
        "fExamUserNum": str(id_number).strip()
    }

    data = json.dumps(req_data, ensure_ascii=True).encode('utf-8')
    resp = request('post', url, headers=headers, data=data)

    return handle_response(resp)
