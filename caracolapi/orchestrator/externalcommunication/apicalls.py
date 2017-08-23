import requests
from uuid import uuid4


def requestLoginERP(args):

    ## request endpoint args
    #request to ERP --> args
    args = {
        'type': 'success',
        'errors': '', # solamente se incluye si existe error
        'expiry':'2019-08-21T00:00',
        'user_token': str(uuid4()),
        'user_rights': 'client'
    }
    return args

def requestNewOrderToERP(args):
    args['type'] = 'success'
    args['order_token'] = str(uuid4())
    print(args['order'])
    print('orden: '+str(args['order'][2]))
    return args

def sendOrderToProduction(args):
    args['status'] = 'ready'
    return args

def sendNotificationToUsers(args):
    return args