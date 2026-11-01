from app import create_app
from app.models import db, Room

# PLACEHOLDER DATA: replace room numbers, types and prices
# with the hotel's real tariff before the demo.
ROOMS = [
    # (room_number, room_type, floor, price_ugx, max_guests)
    ('101', 'Budget Single',  1, 180000, 1),
    ('102', 'Budget Single',  1, 180000, 1),
    ('103', 'Budget Twin',    1, 250000, 2),
    ('104', 'Budget Twin',    1, 250000, 2),
    ('201', 'Deluxe Double',  2, 320000, 2),
    ('202', 'Deluxe Double',  2, 320000, 2),
    ('203', 'Deluxe King',    2, 350000, 2),
    ('204', 'Executive Suite', 2, 450000, 3),
]

app = create_app()
with app.app_context():
    added = 0
    for number, rtype, floor, price, guests in ROOMS:
        if not Room.query.filter_by(room_number=number).first():
            db.session.add(Room(
                room_number=number, room_type=rtype, floor=floor,
                price_ugx=price, max_guests=guests, status='available'
            ))
            added += 1
    db.session.commit()
    print(f'Seeded {added} new rooms. Total rooms: {Room.query.count()}')