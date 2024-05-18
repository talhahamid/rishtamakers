from django.shortcuts import render,redirect

def auth_middlware(get_response):


    def middleware(request):
        if request.session.get('uid'):
            redirect('index')
            print("middleware")
        else:
            redirect('delete')
            print('heyyy')
        response=get_response(request)
        return response

    

    return middleware    
