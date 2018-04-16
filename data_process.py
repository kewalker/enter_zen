with open ("ten_thousand_haikus.txt", "r") as f:

	lines = [line.strip() for line in f]

	cleaned = []

	for line in lines:
		if line != '' and line != 'year unknown':
			try:
				(int(line))
				pass
			except:
				cleaned.append(line)

	# print (len(lines))
	# print (len(cleaned))
	# print (cleaned)

	with open ("haiku_lines.txt", 'w') as writer:
		for line in cleaned:
			writer.write("{}\n".format(line))
