alphas = [0.1, 0.05, 0.01]
quantiles = {0.9: 1.2816, 0.95: 1.6449, 0.99: 2.3263}

def calculate_chi2_critical(alpha, l=255):
    return ((2*l)**0.5) * quantiles[alpha] + l

def calculate_chi2(nu_list, m):
    n = m / 256.0
    result = 0
    for nu in nu_list:
        result += ((nu - n)**2) / n
    return result

def calculate_chi2_advanced(nu_matrix, a, b):
    n = 0
    columns_number = rows_number = len(nu_matrix)
    for i in range(rows_number):
        for j in range(columns_number):
            n += nu_matrix[i][j]
    '''
    nu_rows = [0] * rows_number
    nu_columns = [0] * columns_number
    for i in range(rows_number):
        for j in range(columns_number):
            nu_rows[i] += nu_matrix[i][j]
            nu_columns[j] += nu_matrix[i][j]
            n += nu_matrix[i][j]
            nu_matrix[i][j] **= 2
    '''

    result = -1.0
    for i in range(rows_number):
        for j in range(columns_number):
            if a[i] > 0 and b[j] > 0:
                result += (nu_matrix[i][j]**2.0) / (a[i] * b[j])
    result *= n

    return result
