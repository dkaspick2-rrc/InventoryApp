import json
import requests
import boto3

def lambda_handler(event, context):
  

    # DynamoDB setup
    dynamodb = boto3.resource('dynamodb')
    table = dynamodb.Table('Inventory')

    # Get the key from the path parameters
    if 'pathParameters' not in event or 'id' not in event['pathParameters']:
        return {
            'statusCode': 400,
            'body': json.dumps("Missing 'id' path parameter")
        }

    key_value = event['pathParameters']['id']

    try:
        table.delete_item(Key=key_value)
        return {
            'statusCode': 200,
            'body': json.dumps(f"Item deleted successfully.")
        }
    except Exception as e:
        return {
            'statusCode': 500,
            'body': json.dumps(f"Error adding item: {str(e)}")
        }