#!/usr/bin/python

import boto.ec2
from termcolor import colored

def which_aws_account():
    '''This function determines which aws account we connect to based on 
    current boto config;
    Useful when you have multiple aws account to manage'''

    conn = boto.ec2.connect_to_region('us-west-2')
    
    access_id = conn.gs_access_key_id
    
    #which aws account are we connected to? based on access_id
    id_acct = {'BXQ': 'excelsys', 'DHA': 'hyao', 'D5KA':'envoy s3'}
    aws_account = [id_acct[k] for k in id_acct.keys() 
                                   if access_id.endswith(k)][0]
    
    name = colored(aws_account, 'yellow', attrs=['bold'])
    if conn:
        print '\nconnected to %s AWS account\n' %name
    

if __name__ == '__main__':
    which_aws_account()
