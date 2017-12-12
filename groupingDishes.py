#You have a list of dishes. Each dish is associated with a list of ingredients used to prepare it. You want to group the dishes by
#ingredients, so that for each ingredient you'll be able to find all the dishes that contain it (if there are at least 2 such dishes).
#Return an array where each element is a list with the first element equal to the name of the ingredient and all of the other elements 
#equal to the names of dishes that contain this ingredient. The dishes inside each list should be sorted lexicographically. 
#The result array should be sorted lexicographically by the names of the ingredients in its elements.


def groupingDishes(dishes):
    d = {}
    for ar in dishes:
        dish = ar[0]
        ingredients = ar[1:]
        for ingredient in ingredients:
            if ingredient in d.keys():
                d[ingredient].append(dish)
            else:
                d[ingredient]=[dish]
    for key in d.keys():
        d[key] = sorted(d[key])
    sorted_ingredients = sorted(d.keys())
    all_res = [[i] + d[i] for i in sorted_ingredients]
    return [i for i in all_res if len(i)>2]
        
