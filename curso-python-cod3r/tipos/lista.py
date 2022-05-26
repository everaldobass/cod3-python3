# Tipos de Lista
nums = [1,2,3]
print(type(nums))

# Adicionar numero na lista
nums.append(3)
nums.append(4)
nums.append(500)
print(len(nums))

# Adicionar no indece 3 o valor 100
nums[3] = 100
print(nums)

# Inserir numero 200 no indece Zero
nums.insert(0, -200)
print(nums)

# Pegar o ultimo elemento
print(nums[-1])