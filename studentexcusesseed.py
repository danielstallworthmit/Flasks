from app import db, Student, Excuse

d = Student('D', 'S')
l = Student('L', 'S')
n = Student('DN', 'S')

db.session.add_all([d,l,n])
db.session.commit()
print(len(Student.query.all()))

d = Student.query.get(1)
excuse1 = Excuse('Dog ate the homework', False, 1)
db.session.add(excuse1)
db.session.commit()
print(d.excuses.all())

excuse2 = Excuse('Overslept', True, 1)
db.session.add(excuse2)
db.session.commit()
print(len(d.excuses.all()))
