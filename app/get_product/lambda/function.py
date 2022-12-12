import sys 
import logging 
import traceback 
import json
import uuid
import os 
import boto3
from botocore.exceptions import ClientError
from boto3.dynamodb.conditions import Key


logging.basicConfig(level=logging.INFO)
logger = logging.getLogger()


def get_product(product_id):
    dynamodb = boto3.resource('dynamodb')
    table = dynamodb.Table(os.environ['PRODUCTS_TABLE_NAME'])

    try:
        response = table.get_item(Key={'product_id': product_id})
    except ClientError as e:
        logger.error(e.response['Error']['Message'])
        raise e
    else:
        return response.get('Item')


def handler(event, context):

    response = {}
    response['headers'] = {}
    response['headers']['Content-Type'] = 'application/json'


    try:
        product_id = event['pathParameters']['productId']
        product = get_product(product_id=product_id)
        logger.info(f'Product for product_id {product_id}: {product}')
        if product is None:
            response['statusCode'] = 404
            response['body'] = json.dumps(f'Product with product_id {product_id} not found.')
        else:
            response['statusCode'] = 200
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