ft_list = ["Hello", "tata!"]
ft_tuple = ("Hello", "toto!")
ft_set = {"Hello", "tutu!"}
ft_dict = {"Hello" : "titi!"}

#your code here
# list : change value by index
ft_list[1] = "World!"
# we cannot change Tuple value directelly
# but we can convert it to list and then
# update element and convert the list back to tuple
tmp_tuple = list(ft_tuple)
tmp_tuple[1] = "Maroc"
ft_tuple = tuple(tmp_tuple)

# set : first we remove element
# and then add
ft_set.remove("tutu!")
ft_set.add("Rabat!")

# Dictionaries : we can change value by index (key)
ft_dict["Hello"] = "1337 Coding school!"

print(ft_list)
print(ft_tuple)
print(ft_set)
print(ft_dict)
