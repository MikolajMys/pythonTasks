def game_of_life(input_str, rules_str):
    output_str = ""
    rules = {
        "***": "_", #0
        "**_": "*", #1
        "*_*": "_", #0
        "*__": "*", #1
        "_**": "*", #1
        "_*_": "_", #0
        "__*": "*", #1
        "___": "_"  #0
    }

    for i, rule in enumerate(rules_str):
        if rule == "1":
            key = list(rules.keys())[i]
            rules[key] = "*"
        else:
            key = list(rules.keys())[i]
            rules[key] = "_"

    input_str = input_str[-1] + input_str + input_str[0]
    #print(input_str)

    for i in range(len(input_str)-2):
        triplet = input_str[i:i+3]

        output_str += rules.get(triplet)
        #print(triplet+"="+output_str)

    return output_str

input_str = "______*______"

rules_str = "01010010"
n = 5
output_str = input_str
for _ in range(n):
    output_str = game_of_life(output_str, rules_str)
    print(output_str)
