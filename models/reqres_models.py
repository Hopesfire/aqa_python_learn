from pydantic import BaseModel, EmailStr, HttpUrl


class ReqresUser(BaseModel):
    id: int
    email: EmailStr
    first_name: str
    last_name: str
    avatar: HttpUrl


class ReqresUsersResponse(BaseModel):
    page: int
    per_page: int
    total: int
    total_pages: int
    data: list[ReqresUser]


class ReqresResource(BaseModel):
    id: int
    name: str
    year: int
    color: str
    pantone_value: str


class ReqresResourcesResponse(BaseModel):
    page: int
    per_page: int
    total: int
    total_pages: int
    data: list[ReqresResource]
