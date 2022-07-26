import numpy as np

ages = [57, 61, 57, 57, 58, 57, 61,
        54, 68, 51, 49, 64, 50, 48,
        65, 52, 56, 46, 54, 49, 51,
        47, 55, 55, 54, 42, 51, 56,
        55, 51, 54, 51, 60, 62, 43,
        55, 56, 61, 52, 69, 64, 46,
        54, 47, 70]

heights = [189, 170, 189, 163, 183, 171, 185,
           168, 173, 183, 173, 173, 175, 178,
           183, 193, 178, 173, 174, 183, 183,
           180, 168, 180, 170, 178, 182, 180,
           183, 178, 182, 188, 175, 179, 183,
           193, 182, 183, 177, 185, 188, 188,
           182, 185, 191]

# Criando duas array numpy
ages_arr = np.array(ages)
heights_arr = np.array(heights)

# Fazendo reshape nas array transformando em 1 coluna com 45 linhas
ages_arr = ages_arr.reshape((45, 1))
heights_arr = heights_arr.reshape((45, 1))

# Unindo as duas arrays em um array 2d, com a altura na coluna x e idade na coluna y
# [Unindo arrays horizontalmente (em linhas)]
heights_age_arr = np.hstack((heights_arr, ages_arr))
print(heights_age_arr.shape)
print(heights_age_arr[:3, ])

# [Unindo arrays verticalmente (em colunas)]
heights_arr = heights_arr.reshape((1, 45))
ages_arr = ages_arr.reshape((1, 45))

heights_age_arr = np.vstack((heights_arr, ages_arr))
print(heights_age_arr.shape)
print(heights_age_arr[:, :3])
