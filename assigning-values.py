import numpy as np

heights = [189, 170, 189, 163, 183,
           171, 185, 168, 173, 183,
           173, 173, 175, 178, 183,
           193, 178, 173, 174, 183,
           183, 180, 168, 180, 170,
           178, 182, 180, 183, 178,
           182, 188, 175, 179, 183,
           193, 182, 183, 177, 185,
           188, 188, 182, 185, 191]

ages = [57, 61, 57, 57, 58, 57, 61,
        54, 68, 51, 49, 64, 50, 48,
        65, 52, 56, 46, 54, 49, 51,
        47, 55, 55, 54, 42, 51, 56,
        55, 51, 54, 51, 60, 62, 43,
        55, 56, 61, 52, 69, 64, 46,
        54, 47, 70]

heights_and_ages = heights + ages
heights_and_ages_arr = np.array(heights_and_ages)
heights_and_ages_arr = heights_and_ages_arr.reshape(2, 45)
# Assimilando valores em um array 1d ou 2d
heights_and_ages_arr[0, 3] = 165
print(heights_and_ages_arr[0, 3])

# Assimilando valores em uma coluna inteira
heights_and_ages_arr[0, :] = 180
print(heights_and_ages_arr[0, :])


# Assimilando dois valores em todas as colunas (:2) e em todas as linhas (:2)
# Deixando o espaço antes do : vazio significa assimular em tudo até o limite delimitado em :2
heights_and_ages_arr[:2, :2] = 0
print(heights_and_ages_arr)
# [NOTA] se deixar o limite vazio "heights_and_ages_arr[:, :] = 0"
# A array inteira será assimilada em 0