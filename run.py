
import time
from future_requests.requests import request_future_score
from mail_service import render_to_html, send_email


if __name__ == '__main__':
    name = '张三'
    id_num = '3301xxxxxxxxxxx'
    last_req = None
    while True:
        res = request_future_score(name, id_num)

        if res != last_req:
            contents = render_to_html(res)
            send_email(contents, name='name)
            last_req = res

        time.sleep(600)
