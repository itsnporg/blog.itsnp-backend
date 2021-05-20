from fastapi import APIRouter

router = APIRouter()


@router.get("/test")
def test_route():
    return "Hello World"


@router.get("/")
def get_blogs():
    pass


@router.post("/")
def create_blog():
    pass


@router.get("/{id}")
def get_blog(id: int):
    pass


@router.put("/{id}")
def update_blog(id: int):
    pass


@router.delete("/{id}")
def delete_blog(id: int):
    pass
