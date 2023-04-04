from .Account import AccountModel, AccountModelAdd


class TeacherModel(AccountModel):
    ...


class TeacherModelAdd(AccountModelAdd):
    role_id = 1

