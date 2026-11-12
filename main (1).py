import boto3
import csv
from decimal import Decimal

def get_aws_costs():

    client = boto3.client('ce', region_name='us-east-1')

    response = client.get_cost_and_usage(
        TimePeriod={
            'Start': '2026-10-01',
            'End': '2026-11-01'
        },
        Granularity='MONTHLY',
        Metrics=['UnblendedCost'],
        GroupBy=[
            {
                'Type': 'DIMENSION',
                'Key': 'SERVICE'
            }
        ]
    )

    total = Decimal('0.00')
    report = []

    for period in response['ResultsByTime']:
        for group in period['Groups']:

            service = group['Keys'][0]
            amount = Decimal(
                group['Metrics']['UnblendedCost']['Amount']
            )

            if amount == 0:
                amount = Decimal('0.00')

            total += amount
            report.append([service, f'{amount:.2f}'])

    with open('cost_report.csv', 'w', newline='') as file:

        writer = csv.writer(file)

        writer.writerow(['AWS Service', 'Cost (USD)'])
        writer.writerows(report)
        writer.writerow(['TOTAL', f'{total:.2f}'])

    print('\nAWS COST REPORT')

    for service, amount in report:
        print(f'{service}: ${amount}')

    print('---------------------------')
    print(f'TOTAL COST: ${total:.2f}')
    print('\nReport saved as cost_report.csv')


if __name__ == '__main__':
    get_aws_costs()
