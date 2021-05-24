def main():
    my_list = [1,'hello',True,4.5]
    my_dict = {"first_name":"Diego","Last_name":"Bejarano"}

    #A dictionary can be stored within a list
    super_list = [
        {"first_name":"Diego","Last_name":"Bejarano"}, 
        {"first_name":"Daniel","Last_name":"Suárez"},
        {"first_name":"Laura","Last_name":"Prada"},
        {"first_name":"Esperanza","Last_name":"Prada"},
        {"first_name":"Mercedes","Last_name":"De Prada"},
    ]

    #A list can be also stored within a dictionary
    super_dict = {
        "natural_nums":[1,2,3,4,5],
        "integer_nums":[-1,-2,0,1,2],
        "floating_nums":[1.1,4.5,6.4,7.2,8.5]
    }

    for key, value in super_dict.items():
        print(key, '-', value)
    
    for i in super_list:
        print(i)

if __name__ == '__main__':
    main()