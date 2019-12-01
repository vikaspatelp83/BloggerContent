def get_chart(file="chart.txt"):
	data = []
	with open(file) as chart:
		for line in chart:
			data.append(line.split("\n")[0].split(","))
	char_dictionary = dict(data)
	return char_dictionary


def encode(string,chart=get_chart()):
	enc = ""
	for s in string.lower():
		for k in chart.keys():
			if s==k:
				# print(s,k,chart[s])
				enc+=  chart[s]
	return str(enc)


def decode(enc,chart = get_chart()):
	j = 0
	i = 2
	dec = ""
	enc_list = []
	for _ in range(int(len(enc)/2)):
		enc_list.append(enc[j:i])
		j += 2
		i += 2

	for s in enc_list:
		for key, value in chart.items():
			if s==value:
				dec += key
	return str(dec)


s = input("(Text) to encode :")

print("encoded.",encode(s))
print("decoded.",decode(encode(s)))
