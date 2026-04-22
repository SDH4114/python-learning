#кортежи

kortej=(3,4,8,True,8,"frog",3.14)
#kortej[0]= "tree" не возможно. кортели нельзя менять
print(kortej[3])

print(kortej.count(8))
print(len(kortej))
print(kortej)

kortel= 4,8,"dfg","pep",3.14,False,8 #так тоже можно записывать кортежи

instant=(5) # это не кортежь хоть и есть скобки
instant2=(5,)# это уже кортежь потому что есть ,

nums= [4,8,7,9]
new_kortej= tuple(nums) # tuple() создает кортеж из списка
print(new_kortej) #(4, 8, 7, 9)

word="hello world"
word_kortel=tuple(word) #из стрингов тоже можно делать кортежи
print(word_kortel) #('h', 'e', 'l', 'l', 'o', ' ', 'w', 'o', 'r', 'l', 'd')