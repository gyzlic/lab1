def find_common_participants(group1, group2, separator=","):
    set_group1 = set(group1.split(separator))
    set_group2 = set(group2.split(separator))
    common_participants = set_group1.intersection(set_group2)
    return sorted(common_participants)

participants_first_group = "Иванов|Петров|Сидоров"
participants_second_group = "Петров|Сидоров|Смирнов"

common = find_common_participants(participants_first_group, participants_second_group, separator="|")
print(f"Общие участники: {common}")
