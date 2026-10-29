from app.repositories import cat_repository as repo


def get_cats() -> list[str]:
    return repo.get_cats()
