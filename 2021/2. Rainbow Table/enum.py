# init for i and j
i = 1
j = 1

while i <= 26:
	while j <= 26:
		my_enum = unichr(i+96) + unichr(j+96)
		print(my_enum)
		j += 1
	print("--")
	j = 1
	i += 1
	# end j
	
# end i
