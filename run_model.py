model.load(filename)
for _ in range(5):
 p = train[np.random.randint(0,len(train)-1)]
 print("Seed:")
 print("\"",''.join([intchar[value] for value in p]), "\"")
 for _ in range(100):
 sys.stdout.write((intchar[np.argmax(model.predict((np.reshape(p, (1, len(p), 1))/float(len(chars)))))]))
 p.append(np.argmax(model.predict((np.reshape(p, (1, len(p), 1))/float(len(chars))))))
 p = p[1:len(p)]
 print("\n============================\n")