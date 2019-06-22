"""
Save transformed records to the database.
"""
import db_conn


def save_violation(record):
    db_conn.session.add(db_conn.Violation(**record))
    db_conn.session.commit()
