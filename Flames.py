def _match_char(list1, list2):
    for i in range(len(list1)):
        for j in range(len(list2)):
            if list1[i] == list2[j]:
                c = list1[i]
                list1.remove(c)
                list2.remove(c)

                list3 = list1 + ["*"] + list2
                return [list3, True]
    list3 = list1 + ["*"] + list2
    return [list3, False]


if __name__ == "__main__":
    person1 = input("\nEnter Your Name  : ")
    person1 = person1.lower()
    person1.replace(" ", " ")
    person1_list = list(person1)

    person2 = input("\nEnter Your Lover Name : ")
    person2 = person2.lower()
    person2.replace(" ", "")
    person2_list = list(person2)

    proceed = True

    while proceed:
        ret_list = _match_char(person1_list,person2_list)
        con_list = ret_list[0]
        proceed = ret_list[1]

        star_index = con_list.index("*")

        person1_list = con_list[: star_index]

        person2_list = con_list[star_index + 1:]

        count = len(person2_list) + len(person2_list)

    result = ["Friends", "Love", "Affection", "Marriage", "Enemy", "Siblings"]

    while len(result) > 1:

        split_index = (count % len(result) - 1)

        if split_index >= 0:

            right = result[split_index + 1:]
            left = result[: split_index]

            result = right + left
        else:
            result = result[: len(result) - 1]
    print(f"\nRelationship Status :  {result[0].upper()}")
