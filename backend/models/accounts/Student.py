from .Account import AccountModel, AccountModelAdd


class StudentModel(AccountModel):
    pass


class StudentModelAdd(AccountModelAdd):
    role_id = 2
