import hashlib
def md5func(msg):
    hash_obj=hashlib.md5(b"msg")
    print(hash_obj.hexdigest)
def sha1func(msg):
    hash_obj2=hashlib.sha1(b"msg")
    print(hash_obj2.digest)


message=input("enter a message")
md5func(message)
sha1func(message)