from DB import *
from sqlalchemy import Column, Integer, String
from sqlalchemy.orm import Session

from entities.User import User
from entities.Project import Project
from helper.ultils import to_dict

Base.metadata.create_all(bind=engine)


db = SessionLocal()
# user = User(email='test3@test.com', first_name='test', last_name='test', password='123456')
# created_user = User.Create(db, user)

# project = Project(user_id=1, project_name='tét project', project_type='object dê', classes='[]')
# # Project.Create(db, project)

# user = User.GetById(db ,1)

# for p in user.projects:
#     print(to_dict(p))
# # print(to_dict(User.GetById(db, 1)))

print(to_dict(User.Update(db, 1, {
    'password' : 'lam123',
    'first_name': 'Lâm'
    # 'email': 'lam@gmail.com'
})))
DBController().print_table('users')