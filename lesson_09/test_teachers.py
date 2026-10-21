from sqlalchemy import text


def test_add_teacher(session, cleanup):
    teacher_id = session.execute(
        text(
            "INSERT INTO teachers (name) "
            "VALUES (:name) RETURNING id"
        ),
        {"name": "Test Teacher"},
    ).scalar_one()
    session.commit()
    cleanup("teachers", teacher_id)

    name = session.execute(
        text("SELECT name FROM teachers WHERE id = :id"),
        {"id": teacher_id},
    ).scalar_one()
    assert name == "Test Teacher"


def test_update_teacher(session, cleanup):
    teacher_id = session.execute(
        text(
            "INSERT INTO teachers (name) "
            "VALUES (:name) RETURNING id"
        ),
        {"name": "Teacher Old"},
    ).scalar_one()
    session.commit()
    cleanup("teachers", teacher_id)

    session.execute(
        text("UPDATE teachers SET name = :name WHERE id = :id"),
        {"name": "Teacher New", "id": teacher_id},
    )
    session.commit()

    name = session.execute(
        text("SELECT name FROM teachers WHERE id = :id"),
        {"id": teacher_id},
    ).scalar_one()
    assert name == "Teacher New"


def test_delete_teacher(session):
    teacher_id = session.execute(
        text(
            "INSERT INTO teachers (name) "
            "VALUES (:name) RETURNING id"
        ),
        {"name": "Teacher To Delete"},
    ).scalar_one()
    session.commit()

    session.execute(
        text("DELETE FROM teachers WHERE id = :id"),
        {"id": teacher_id},
    )
    session.commit()

    exists = session.execute(
        text("SELECT 1 FROM teachers WHERE id = :id"),
        {"id": teacher_id},
    ).first()
    assert exists is None