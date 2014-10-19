def calculate_chi2(nu_list, m):
    n = m / 256.0
    result = 0
    for nu in nu_list:
        result += ((nu_list[i] - n)**2) / n
    return result

def calculate_chi2_advanced(nu_matrix):
    n = 0
    columns_number = rows_number = len(nu_matrix)
    nu_rows = [0] * rows_number
    nu_columns = [0] * columns_number
    for i in range(rows_number):
        for j in range(columns_number):
            nu_rows[i] += nu_matrix[i][j]
            nu_columns[j] += nu_matrix[i][j]
            n += nu_matrix[i][j]
            nu_matrix[i][j] **= 2

    result = -1
    for i in range(rows_number):
        for j in range(columns_number):
            result += nu_matrix[i][j] / (nu_rows[i] * nu_columns[j])
    result *= n

    return result
