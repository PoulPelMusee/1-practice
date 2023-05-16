import math


def matmul(a, b):
	res = []
	for row in a:
		res_row = []
		for col_i in range(len(b[0])):
			element = 0
			for i in range(len(a[0])):
				element += b[i][col_i]*row[i]
			res_row.append(element)
		res.append(res_row)
	return res
				
	
def use_matrix(vector, matrix):
	res = []
	for i in range(len(vector)):
		element = 0
		for j in range(len(vector)):
			element += vector[j] * matrix[j][i]
		res.append(element)
	return res


def scale_matrix(scale):
    return [[scale[0], 0, 0], [0, scale[1], 0], [0, 0, 1]]


def rotation_matrix(angle):
    sin = math.sin(angle)
    cos = math.cos(angle)
    return [[cos, sin, 0], [-sin, cos, 0], [0, 0, 1]]


def move_matrix(move):
	return [[1, 0, 0], [0, 1, 0], [move[0], move[1], 1]]


def modelMatrix(inMatrix, sequence):
	matrix = None

	for operation in sequence:
		if operation == 'S':
			new_matrix = scale_matrix(inMatrix['S'])
			if matrix is None:
				matrix = new_matrix
			else:
				matrix = matmul(new_matrix, matrix)

		elif operation == 'R':
			new_matrix = rotation_matrix(inMatrix['R'] * math.pi / 180)
			if matrix is None:
				matrix = new_matrix
			else:
				matrix = matmul(new_matrix, matrix)

		else:
			new_matrix = move_matrix(inMatrix['T'])
			if matrix is None:
				matrix = new_matrix
			else:
				matrix = matmul(new_matrix, matrix)

	return use_matrix([inMatrix['V'][0], inMatrix['V'][1], 1], matrix)


if __name__ == '__main__':
	data1 = {'S': (1, 2.2), 'R': 12.6, 'T': (2, 2), 'V': (3, 2)}
	j = modelMatrix(data1, 'SRT')
	print('j = ', j)

	data2 = {'S': (1.3, 1.2), 'R': 36.4, 'T': (1, 1), 'V': (3, 2)}
	k = modelMatrix(data2, 'TRS')
	print('k = ', k)
