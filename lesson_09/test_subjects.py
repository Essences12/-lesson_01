from sqlalchemy import text


def test_add_subject(session, cleanup):
    subject_id = session.execute(
        text(
            "INSERT INTO subjects (name) "
            "VALUES (:name) RETURNING id"
        ),
        {"name": "Test Subject"},
    ).scalar_one()
    session.commit()
    cleanup("subjects", subject_id)

    name = session.execute(
        text("SELECT name FROM subjects WHERE id = :id"),
        {"id": subject_id},
    ).scalar_one()
    assert name == "Test Subject"


def test_update_subject(session, cleanup):
    subject_id = session.execute(
        text(
            "INSERT INTO subjects (name) "
            "VALUES (:name) RETURNING id"
        ),
        {"name": "Old Subject"},
    ).scalar_one()
    session.commit()
    cleanup("subjects", subject_id)

    session.execute(
        text("UPDATE subjects SET name = :name WHERE id = :id"),
        {"name": "New Subject", "id": subject_id},
    )
    session.commit()

    name = session.execute(
        text("SELECT name FROM subjects WHERE id = :id"),
        {"id": subject_id},
    ).scalar_one()
    assert name == "New Subject"


def test_delete_subject(session):
    subject_id = session.execute(
        text(
            "INSERT INTO subjects (name) "
            "VALUES (:name) RETURNING id"
        ),
        {"name": "Subject To Delete"},
    ).scalar_one()
    session.commit()

    session.execute(
        text("DELETE FROM subjects WHERE id = :id"),
        {"id": subject_id},
    )
    session.commit()

    exists = session.execute(
        text("SELECT 1 FROM subjects WHERE id = :id"),
        {"id": subject_id},
    ).first()
    assert exists is None