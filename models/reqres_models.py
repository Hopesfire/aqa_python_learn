from pydantic import BaseModel


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
