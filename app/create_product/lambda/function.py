import sys 
import logging 
import traceback 
import json
import os 
import uuid
import boto3


logging.basicConfig(level=logging.INFO)
logger = logging.getLogger()


def create_product(product):
    dynamodb = boto3.resource("dynamodb")
    table = dynamodb.Table(os.environ['PRODUCTS_TABLE_NAME'])

    response = table.put_item(Item=product)

    return response.get('Attributes')


def handler(event, context):
    logger.info(f'event: {event}')

    response = {}
    response['headers'] = {}
    response['headers']['Content-Type'] = 'application/json'

    try:        
        product = json.loads(event['body'])
        product['product_id'] = str(uuid.uuid4())

        create_product(product)

        response['statusCode'] = 201
        response['body'] = json.dumps(product)

    except Exception as e:
        exception_type, exception_value, exception_traceback = sys.exc_info()
        traceback_string = traceback.format_exception(exception_type, exception_value, exception_traceback)
        err_msg = json.dumps({
            "errorType": exception_type.__name__,
            "errorMessage": str(exception_value),
            "stackTrace": traceback_string
        })
        logger.error(err_msg)
        
        response['statusCode'] = 500
        response['body'] = err_msg

    return response