from calendar import c
import sys 
import logging 
import traceback 
import json
import uuid
import os 
import boto3
from boto3.dynamodb.conditions import Key


logging.basicConfig(level=logging.INFO)
logger = logging.getLogger()


def delete_product(product_id):
    dynamodb = boto3.resource('dynamodb')
    table = dynamodb.Table(os.environ['PRODUCTS_TABLE_NAME'])

    response = table.delete_item(Key = {'product_id': product_id})

    return response 


def handler(event, context):

    response = {}
    response['headers'] = {}
    response['headers']['Content-Type'] = 'application/json'

    try:
        product_id = event['pathParameters']['productId']

        delete_product(product_id)

        response['statusCode'] = 204
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