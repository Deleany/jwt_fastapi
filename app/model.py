from pydantic import BaseModel, Field, EmailStr


class PostSchema(BaseModel):
    id: int = Field(default=None)
    title: str = Field(default=None)
    content: str = Field(default=None)
    class Config:
        schema_extra = {
            "post_demo": {
                "title": "some title about animals",
                "content": "some content about animals"
            }
        }