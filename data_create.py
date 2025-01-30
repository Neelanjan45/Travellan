from app import app, db
from models import Locations, Sites

l1 = Locations(id=1, title="Location One", description="Lorem ipsum dolor sit amet consectetur, adipisicing elit. Omnis, iste labore adipisci explicabo")
l2 = Locations(id=2, title="Location Two", description="Lorem ipsum dolor sit amet consectetur, adipisicing elit. Omnis, iste labore adipisci explicabo")
l3 = Locations(id=3, title="Location Three", description="Lorem ipsum dolor sit amet consectetur, adipisicing elit. Omnis, iste labore adipisci explicabo")

s1 = Sites(id=1, title="Site One", description="Lorem ipsum dolor sit amet consectetur adipisicing elit. Deleniti accusamus eligendi totam aut molestias facilis architecto quibusdam beatae hic veritatis illum eveniet", image="Image", loc_id=l1.id)
s2 = Sites(id=2, title="Site Two", description="Lorem ipsum dolor sit amet consectetur adipisicing elit. Deleniti accusamus eligendi totam aut molestias facilis architecto quibusdam beatae hic veritatis illum eveniet", image="Image", loc_id=l2.id)
s3 = Sites(id=3, title="Site Three", description="Lorem ipsum dolor sit amet consectetur adipisicing elit. Deleniti accusamus eligendi totam aut molestias facilis architecto quibusdam beatae hic veritatis illum eveniet", image="Image", loc_id=l3.id)
s4 = Sites(id=4, title="Site Four", description="Lorem ipsum dolor sit amet consectetur adipisicing elit. Deleniti accusamus eligendi totam aut molestias facilis architecto quibusdam beatae hic veritatis illum eveniet", image="Image", loc_id=l3.id)
s5 = Sites(id=5, title="Site Five", description="Lorem ipsum dolor sit amet consectetur adipisicing elit. Deleniti accusamus eligendi totam aut molestias facilis architecto quibusdam beatae hic veritatis illum eveniet", image="Image", loc_id=l2.id)
s6 = Sites(id=6, title="Site Six", description="Lorem ipsum dolor sit amet consectetur adipisicing elit. Deleniti accusamus eligendi totam aut molestias facilis architecto quibusdam beatae hic veritatis illum eveniet", image="Image", loc_id=l1.id)

with app.app_context():
    db.session.add(l1)
    db.session.add(l2)
    db.session.add(l3)

    db.session.add(s1)
    db.session.add(s2)
    db.session.add(s3)
    db.session.add(s4)
    db.session.add(s5)
    db.session.add(s6)

    db.session.commit()
