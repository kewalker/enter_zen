with open ("data/lotus_sutra.txt", "r") as f:

	lines = [line.strip() for line in f]

	cleaned = []

	#removes newlines and 'year unknown text'
	for line in lines:
		if line != '' and line != 'year unknown':
			#removes integers
			try:
				(int(line))
				pass
			except:
				cleaned.append(line)

	# print (len(lines))
	# print (len(cleaned))
	# print (cleaned)

	with open ("data/lotus_sutra_cleaned.txt", 'w') as writer:
		for line in cleaned:
			writer.write("{}\n".format(line))
