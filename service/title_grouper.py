class TitleGrouper:

    @staticmethod
    def create_groups(lectures):
        groups = []

        last_index = 0
        for i in range(len(lectures)):
            if(lectures[i].id < i and i != 0):
                groups.append(lectures[last_index:i])
                last_index = i

        return groups
