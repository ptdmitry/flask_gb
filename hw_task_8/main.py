from hashlib import sha512

hello = 'Hello!'

print(sha512(hello.encode()).hexdigest())
