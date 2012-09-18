#!/usr/bin/env python

#simple script to iter through and delete all keys of a riak bucket
#and thus the bucket itself

import sys
import riak

def delete_bucket(bk_name):
    import riak
    client = riak.RiakClient()
    if bk_name not in client.get_buckets():
        raise SystemExit, 'bucket %s does not exist' %bk_name
    bucket = client.bucket(bk_name)
    for key in bucket.get_keys():
        bucket.get(key).delete()
    print 'bucket %s deleted.' %bk_name


if __name__ == '__main__':
    if len(sys.argv) != 2:
        raise SystemExit, 'usage: %s bucket_to_delete' %sys.argv[0]
    delete_bucket(sys.argv[1])
    
