from pydantic import BaseModel
from typing import Optional


class LoadDocumentRequest(BaseModel):

    file_path: str
    encoding: Optional[str] = "utf-8"