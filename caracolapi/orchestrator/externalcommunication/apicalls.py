import requests


def requestLoginERP(args):

    ## request endpoint args
    #request to ERP --> args
    args = {
        'type': 'success',
        'errors': '', # solamente se incluye si existe error
        'expiry':'2019-08-21T00:00',
        'user_token': '2351asetqw3gq31b',
        'user_rights': []
    }
    return args

def requestNewOrderToERP(args):
    args['type'] = 'success'
    args['order_token'] = 'aosntaspoi125'
    return args

def sendOrderToProduction(args):
    return args