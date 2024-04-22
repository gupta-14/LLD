from group.group import Group

class GroupController:
    def __init__(self) -> None:
        self.group_list: list[Group] = []

    def create_group(self, group_id, group_name, created_by_user):
        group = Group()
        group.set_group_id(group_id)
        group.set_group_name(group_name)
        group.add_member(created_by_user)
        self.group_list.append(group)

    def get_group(self, group_id):
        for group in self.group_list:
            if group.get_group_id() == group_id:
                return group
        return None