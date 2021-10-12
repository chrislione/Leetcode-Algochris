def intToRoman(num):
    romans = ["I", "V", "X", "L", "C", "D", "M"]
    output = ""

    intger_num = int(num)
    inputs = str((num))
    list_input = list(inputs)
    length_input = int(len(list_input))  # finding length will help determine what unit it will be
    # print(length_input)

    if length_input == 1:  # unit
        if intger_num <= 3:
            intger_num = intger_num * romans[0]

            output = intger_num
            # print(num)
        if intger_num == 4:
            intger_num = romans[0] + romans[1]
            output = intger_num
        if num >= 5 and num < 9:
            num = romans[1]
            add = intger_num - 5
            k = romans[1] + add * romans[0]

            output = k
        if intger_num == 9:
            output = romans[2] + romans[0]

    if length_input == 2:   #Tens
        int_list_input_x = int(list_input[0])  #converted to int
        int_list_input_y = int(list_input[1])
        if int_list_input_x >= 1 and int_list_input_x <= 3:
            if int_list_input_y >= 1 and int_list_input_y <= 3:
                j="I"
                print(int_list_input_y)

                output=int_list_input_x*"X" + int_list_input_y*j
        if int_list_input_x >= 1 and int_list_input_x <= 3:
            if int_list_input_y == 4:
                j="IV"
                output = int_list_input_x * "X" +  j
        if int_list_input_x>=1 and int_list_input_x<=3:
            if int_list_input_y >=5 and int_list_input_y<=8:
                j="I"
                q=int_list_input_y-5
                q=q*j

                # output=q
                output= int_list_input_x *"X" + "V" + q






    print(output)


# call fuction
user_input=input("please enter a number:")
user_input=int(user_input)
intToRoman(user_input)
































# def intToRoman(num):
#     romans = ["I", "V", "X", "L", "C", "D", "M"]
#     output = ""
#
#     intger_num = int(num)
#     inputs = str((num))  # converted to string, so purpose to use list function to get length
#     list_input = list(inputs)  # work with this
#
#
#     length_input = int(len(list_input))  # finding length will help determine what unit it will be
#     # print(length_input)
#
#     if length_input == 1:  # unit
#         if intger_num <= 3:
#             intger_num = intger_num * romans[0]
#
#             output = intger_num
#             # print(num)
#         if intger_num == 4:
#             intger_num = romans[0] + romans[1]
#             output = intger_num
#         if num >= 5 and num < 9:
#             num = romans[1]
#             add = intger_num - 5
#             k = romans[1] + add * romans[0]
#
#             output = k
#         if intger_num == 9:
#             output = romans[2] + romans[0]
#     if length_input == 2: #Tens
#         int_list_input_x = int(list_input[0]) #converted to int
#         int_list_input_y = int(list_input[1])
#
#         # if int(list_input[1])>=1 and int(list_input)<=3: #need to convert list_input to int so I can use inequality signs so this learn gives traceback
#         if int_list_input_y >= 1 and int_list_input_y <= 3:
#             j="I"
#             print(int_list_input_y)
#
#             output=int_list_input_x*"X" + int_list_input_y*j
#
#         # if int_list_input_y >= 5 and int_list_input_y <= 8:
#         #     J = "I"
#         #     output = int_list_input_x * "X" + int_list_input_y * J+"V"
#
#         # if int_list_input_y >= 1 and int_list_input_y <= 3:
#         #     j = "I"
#         #     # ten_digit=int(int_list_input_y*0.1)
#         #     print(int_list_input_y)
#         #     # output=ten_digit*"X" + int(int_list_input_y *0.1)*j
#         #     output = int_list_input_y * "X" + int_list_input_y * j
#
#     print(output)