import pytest
from sqlalchemy import create_engine, text
from sqlalchemy.orm import sessionmaker

DATABASE_URL = (
    "postgresql://myuser:mypassword@localhost:5432/mydatabase"
)

engine = create_engine(DATABASE_URL, future=True)
SessionLocal = sessionmaker(bind=engine, future=True)


@pytest.fixture()
def session():
    """Сессия SQLAlchemy с откатом после теста как страховка."""
    sess = SessionLocal()
    try:
        yield sess
    finally:
        sess.rollback()
        sess.close()


@pytest.fixture()
def cleanup(session):
    """
    Фикстура для гарантированной очистки созданных данных.
    Возвращает функцию-регистратор: cleanup(table, id).
    """
    created = []

    def register(table: str, row_id: int):
        created.append((table, row_id))

    yield register

    # Удаляем всё, что было создано, в обратном порядке
    for table, row_id in reversed(created):
        session.execute(
            text(f"DELETE FROM {table} WHERE id = :id"),
            {"id": row_id},
        )
    session.commit()