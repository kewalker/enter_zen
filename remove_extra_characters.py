import numpy as np

#set hyperparameters
max_len = 40
step = 2
num_units = 128
learning_rate = 0.001
batch_size = 200
epoch = 30
temperature = 0.5

def read_data(file_name):
	'''
	 open and read text file
	'''
	text = open(file_name, 'r').read()
	return text.lower()

def featurize(text):
    '''
     featurize the text to train and target dataset
    '''
    unique_chars = list(set(text))
    len_unique_chars = len(unique_chars)

    input_chars = []
    output_char = []

    for i in range(0, len(text) - max_len, step):
        input_chars.append(text[i:i+max_len])
        output_char.append(text[i+max_len])

    train_data = np.zeros((len(input_chars), max_len, len_unique_chars))
    target_data = np.zeros((len(input_chars), len_unique_chars))

    for i , each in enumerate(input_chars):
        for j, char in enumerate(each):
            train_data[i, j, unique_chars.index(char)] = 1
        target_data[i, unique_chars.index(output_char[i])] = 1
    return train_data, target_data, unique_chars, len_unique_chars

text = read_data('haiku_lines.txt')
train_data, target_data, unique_chars, len_unique_chars = featurize(text)

text2 = read_data('rumi_masnavi_djvu.txt')
train_data2, target_data2, unique_chars2, len_unique_chars2 = featurize(text2)

diff = list(set(unique_chars2) - set(unique_chars))

print(diff)

for char in diff:
	print (char)
temp_file = ''
with open ("rumi_cleaned.txt", 'w') as writer:
	for line in text2:
		temp_line = ''
		for word in line:
			if word not in diff:
				temp_line += word
				# break
		writer.write("{}".format(temp_line))





print (unique_chars)
print (unique_chars2)