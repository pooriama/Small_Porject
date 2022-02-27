def secret_code(secret_list, customer_list):
    # initialize counter of both lists
    secret_list_counter=0
    customer_list_counter=0

    #  loop to check size of both list
    while secret_list_counter<len(secret_list) and customer_list_counter<len(customer_list):

        # consider the each list belongs to secret_list one by one
        each_list = secret_list[secret_list_counter]

        # counter for the previous list
        list_counter = 0

        # check it is the same or not
        while list_counter<len(each_list) and customer_list_counter<len(customer_list):
            if each_list[list_counter] == "anything" or each_list[list_counter] == customer_list[customer_list_counter]:
                list_counter = list_counter+1
            else:
                list_counter = 0

            customer_list_counter = customer_list_counter+1

        if list_counter != len(each_list):
            return False

        # go to the next list
        secret_list_counter = secret_list_counter+1

    if secret_list_counter < len(secret_list):
        return False

    return True


# Example 1
secret_list = [["apple", "apple"], ["banana", "anything", "banana"]]
customer_list = ["orange", "apple", "apple", "banana", "orange", "banana"]

# Example 2
# secret_list = [["apple", "apple"], ["banana", "anything", "banana"]]
# customer_list=["banana", "orange", "banana", "apple", "apple"]


print(secret_code(secret_list, customer_list))
