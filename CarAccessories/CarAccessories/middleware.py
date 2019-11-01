import time
import logging
from django.utils.deprecation import MiddlewareMixin
from django.http import HttpResponse

MAX_REQUEST_PER_SECOND = 2  # 访问频率
logging.basicConfig(level=logging.DEBUG,format='%(asctime)s %(filename)s[line:%(lineno)d] %(levelname)s %(message)s',
            datefmt='%a, %d %b %Y %H:%M:%S',
            filename='ip_recv.log',
            filemode='a+')


class RequestBlockingMiddleware(MiddlewareMixin):

    def process_request(self, request):
        now = time.time()
        request_queue = request.session.get('request_queue', [])
        if len(request_queue) < MAX_REQUEST_PER_SECOND:
            request_queue.append(now)
            request.session['request_queue'] = request_queue
            logging.info('首次登录'+self.get_ip(request))
        else:
            time0 = request_queue[0]
            if (now - time0) < 1:
                logging.info(self.get_ip(request))
                return HttpResponse('访问频率过高！')
            request_queue.append(time.time())
            request.session['request_queue'] = request_queue[1:]

    def get_ip(self, request):
        x_forwarded_for = request.META.get('HTTP_X_FORWARDED_FOR')
        if x_forwarded_for:
            ip = x_forwarded_for.split(',')[0]  # 所以这里是真实的ip
            IP = '真实ip:' + str(ip)
        else:
            ip = request.META.get('REMOTE_ADDR')  # 这里获得代理ip
            IP = '代理ip:' + str(ip)

        return IP