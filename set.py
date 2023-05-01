# set is a collection which is unordered, unindexed.  nop duplicate values

utensils = {'fork', 'spoon','knife', 'knife', 'knife'}
dishes = {'bowl', 'plate', 'cup'}
# utensils.add('napkin')
# utensils.remove('fork')
# # utensils.clear()
# utensils.update(dishes)
# dinner_table = utensils.union(dishes)

print(dishes.difference(utensils))
for x in utensils: 
    print(x)

 




