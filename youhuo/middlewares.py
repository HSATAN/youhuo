# _*_ coding:utf-8 _*_

class MyMiddleware():

    def process_request(self,request,spider):
        print('---------------------')
        print(request.headers)
        print('---------------------')
