from app import db, Computer

db.create_all()
my_mac = Computer('Macbook Air',4)
my_acer = Computer('D Nitro Black',32)

db.session.add(my_mac)
db.session.add(my_acer)
db.session.commit()

print(my_acer.memory_in_gb)