from django.http import HttpResponseNotFound, JsonResponse
from django.views import View

class APIViewMixin(View):
    def options(self, request, *args, **kwargs):

        res = JsonResponse(
            {},
            safe=False
        )
        res["Access-Control-Allow-Origin"] = "*"
        res["Access-Control-Allow-Methods"] = "GET, OPTIONS, POST"
        res["Access-Control-Max-Age"] = "1000"
        res["Access-Control-Allow-Headers"] = "*"
        res["X-Frame-Options"] = "*"
        return res
    
    def post(self, request, *args, **kwargs):
        cmd = request.POST.get("cmd")
        if cmd and cmd in self.post_services:
            data = getattr(self, "_%s" % cmd)(request.POST)

            response = JsonResponse(data, safe=False)
            response["Access-Control-Allow-Origin"] = "*"
            response["Access-Control-Allow-Methods"] = "GET, OPTIONS, POST"
            response["Access-Control-Max-Age"] = "1000"
            response["Access-Control-Allow-Headers"] = "*"
            response["X-Frame-Options"] = "*"

            return response
        else:
            return HttpResponseNotFound("Not found")
    
    def get(self, request, *args, **kwargs):
        cmd = request.GET.get("cmd")
        if cmd and cmd in self.get_services:
            data = getattr(self, "_%s" % cmd)(request.GET)

            response = JsonResponse(data, safe=False)
            response["Access-Control-Allow-Origin"] = "*"
            response["Access-Control-Allow-Methods"] = "GET, OPTIONS, POST"
            response["Access-Control-Max-Age"] = "1000"
            response["Access-Control-Allow-Headers"] = "*"
            response["X-Frame-Options"] = "*"
            
            return response
        else:
            return HttpResponseNotFound("Not found")