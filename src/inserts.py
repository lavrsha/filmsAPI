from datetime import date

from src import db, app
from src.models import Film




def populate_films():
    harry_potter_and_ph_stone = Film(
            title='Harry Potter and the Philosopher\'s Stone',
            release_date=date(2001, 11, 4),
            description='aaaabsdsawqdsaa',
            distributed_by='Warner Bros. Pictures',
            length=152,
            rating=7.6,
        )
    harry_potter_and_ch_s = Film(
            title='Harry Potter and the Chamber of Secrets',
            release_date=date(2002, 11, 3),
            description='asdsafaskfkasfkaskm',
            distributed_by='Warner Bros. Pictures',
            length=161,
            rating=7.4,
        )
    harry_potter_and_pris_az = Film(
            title='Harry Potter and the Prisoner of the Azkaban',
            release_date=date(2004, 6, 4),
            description='asfmmkaskmfkmaskfmas',
            distributed_by='Warner Bros. Pictures',
            length=142,
            rating=7.9,
        )




    db.session.add(harry_potter_and_ph_stone)
    db.session.add(harry_potter_and_ch_s)
    db.session.add(harry_potter_and_pris_az)

    db.session.commit()
    db.session.close()

if __name__ == '__main__':
    print('Populating db...')
    with app.app_context():
        populate_films()
    print('Successfully populated')
