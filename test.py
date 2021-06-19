class AuthData:
    t_id = -1
    titles = ["id", "login", "password", "email"]

    def __init__(self, login, password, email):
        AuthData.t_id += 1
        self.t_id = AuthData.t_id
        self.login = login
        self.password = password
        self.email = email

    def get_data_like_list(self):
        return [self.t_id, self.login, self.password, self.email]


class UserData:
    titles = ["id", "фамилия", "имя", "отчество", "email", "телефонный номер"]

    def __init__(self, t_id, surname, name, patronymic, email, phone):
        self.t_id = t_id
        self.surname = surname
        self.name = name
        self.patronymic = patronymic
        self.email = email
        self.phone = phone

    def get_data_like_list(self):
        return [self.t_id, self.surname, self.name, self.patronymic, self.email, self.phone]


class PupilPersonalData:
    titles = ["id_учителя", "класс", "id_ученика", "фамилия", "имя", "отчество",
              "пол", "телефонный номер", "номера родителей", "адресс", "email", "дата рождения"]
    pup_id = -1

    def __init__(self, teacher_id, class_num, surname, name, patronymic, sex, phone, parents_phones, address, email,
                 birth_date):
        PupilPersonalData.pup_id += 1
        self.pup_id = PupilPersonalData.pup_id
        self.teacher_id = teacher_id
        self.class_num = class_num
        self.surname = surname
        self.name = name
        self.patronymic = patronymic
        self.sex = sex
        self.phone = phone
        self.parents_phones = parents_phones
        self.address = address
        self.email = email
        self.birth_date = birth_date

    def get_data_like_list(self):
        return [self.teacher_id, self.class_num, self.pup_id, self.surname, self.name, self.patronymic, self.sex,
                self.phone,
                self.parents_phones, self.address, self.email, self.birth_date]


class PupilEducData:
    titles = ["id_ученика", "id_отчета", "год", "триместр", "Алгебра", "Английский", "Биология", "География",
              "Геометрия", "ИЗО", "Информатика", "История", "Литература", "Музыка", "Обществознание",
              "Русский язык", "Русская родная литература", "Русский родной язык", "Технология", "Физика",
              "Физическая культура", "Химия", "Черчение"]
    review_id = -1

    def __init__(self, pup_id, year, sem, marks):
        PupilEducData.review_id += 1
        self.review_id = PupilEducData.review_id
        self.pup_id = pup_id
        self.year = year
        self.sem = sem
        self.marks = marks

    def get_data_like_list(self):
        final = [self.review_id, self.pup_id, self.year, self.sem] + self.marks
        return final
