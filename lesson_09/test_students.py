from sqlalchemy import text


def test_add_student(session, cleanup):
    result = session.execute(
        text(
            "INSERT INTO students (name) "
            "VALUES (:name) RETURNING id"
        ),
        {"name": "Test Student"},
    )
    student_id = result.scalar_one()
    session.commit()
    cleanup("students", student_id)

    row = session.execute(
        text("SELECT name FROM students WHERE id = :id"),
        {"id": student_id},
    ).one()
    assert row.name == "Test Student"


def test_update_student(session, cleanup):
    student_id = session.execute(
        text(
            "INSERT INTO students (name) "
            "VALUES (:name) RETURNING id"
        ),
        {"name": "Before Update"},
    ).scalar_one()
    session.commit()
    cleanup("students", student_id)

    session.execute(
        text("UPDATE students SET name = :name WHERE id = :id"),
        {"name": "After Update", "id": student_id},
    )
    session.commit()

    name = session.execute(
        text("SELECT name FROM students WHERE id = :id"),
        {"id": student_id},
    ).scalar_one()
    assert name == "After Update"


def test_delete_student(session):
    student_id = session.execute(
        text(
            "INSERT INTO students (name) "
            "VALUES (:name) RETURNING id"
        ),
        {"name": "To Be Deleted"},
    ).scalar_one()
    session.commit()

    session.execute(
        text("DELETE FROM students WHERE id = :id"),
        {"id": student_id},
    )
    session.commit()

    exists = session.execute(
        text("SELECT 1 FROM students WHERE id = :id"),
        {"id": student_id},
    ).first()
    assert exists is None