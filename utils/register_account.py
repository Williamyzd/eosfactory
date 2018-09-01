from  eosfactory import *
import testnet_data
import argparse

def register_account(
    testnode_url, alias, account_name, owner_key, active_key):

    set_nodeos_address(testnode_url)
    if not verify_testnet():
        return

    testnet_data.mapped()

    create_wallet(file=True)
    account_object_name = "account_master"   
    create_master_account(
        account_object_name,
        account_name=account_name,
        owner_key=owner_key,
        active_key=active_key)

    if account_object_name in globals():
        testnet_data.add_to_map(
            testnode_url, account_name, owner_key, active_key, alias)

    testnet_data.mapped()

parser = argparse.ArgumentParser(description='''
Given an url and an testnet pseudo (not obligatory), get registration data.
Apply the data to the registration form of the testnet.
Enter 'go' when ready.

Example:
    python3 register_account.py https://api.kylin-testnet.eospace.io

If additional -- flagged ``--orphan`` -- arguments are given, the completely 
defined account is checked for existence, and possibly added as any other 
testnet entry.
''')

parser.add_argument("testnode_url", help="An URL of a public node offering access to the testnet, e.g. http://88.99.97.30:38888")
parser.add_argument("-p", "--pseudo", default=None, help="Testnet pseudo")
parser.add_argument(
            "-o", "--orphan", nargs=3,
            help="<name> <owner key> <active key>")

args = parser.parse_args()

account_name = None
owner_key = None
active_key = None
if args.orphan: 
    account_name = args.orphan[0]
    owner_key = args.orphan[1]
    active_key = args.orphan[2]

register_account(
    args.testnode_url, args.pseudo, account_name, owner_key, active_key)

# python3 register_account.py https://api.kylin-testnet.eospace.io --pseudo kylin2 --orphan dgxo1uyhoytn 5JE9XSurh4Bmdw8Ynz72Eh6ZCKrxf63SmQWKrYJSXf1dEnoiKFY 5JgLo7jZhmY4huDNXwExmaWQJqyS1hGZrnSjECcpWwGU25Ym8tA