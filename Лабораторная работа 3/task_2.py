# TODO Напишите функцию find_common_participants
def find_common_participants(fir_gr, sec_gr, n=','):
    first_group = set(fir_gr.split(n))
    second_group = sec_gr.split(n)
    common_person = list(first_group.intersection(second_group))
    common_person.sort()
    print(common_person)


participants_first_group = "Иванов|Петров|Сидоров"
participants_second_group = "Петров|Сидоров|Смирнов"
find_common_participants(participants_first_group, participants_second_group, '|')
