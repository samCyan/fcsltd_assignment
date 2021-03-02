import csv

from sqlalchemy_utils import database_exists


def init_db(db, table):
    if not database_exists("sqlite:///investors/locations.db"):
        db.create_all()
    table.query.delete()

    with open("investors/investors.csv") as csv_file:
        csv_reader = csv.reader(csv_file, delimiter=",")
        line_count = 0
        for row in csv_reader:
            if line_count == 0:
                line_count += 1
            else:
                investor = table(
                    fullname=row[0], location=row[1], latitude=row[2], longitude=row[3]
                )
                db.session.add(investor)
                line_count += 1
        db.session.commit()
