import boto3

db = boto3.resource('dynamodb')

table = db.Table('Campaign')

table.put_item(
    Item={
        'CampaignID': 3,
        'UserID': 'jdemp@cyve',
        'Name': 'Again',
    }
)

data = table.get_item(
    Key={
        'CampaignID': 2,
        'UserID': 'jdemp@cyve',
    }
)

print(data)

