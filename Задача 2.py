import hashlib

def main(n):
	with open('Text_1.txt', encoding='utf8') as f:
		while n != 0:
			text = f.readline().rstrip()
			textUtf8 = text.encode('utf-8')
			hash = hashlib.md5(textUtf8)
			hexa = hash.hexdigest()
			n -= 1
			yield hexa

result = main(250)
print(next(result))

