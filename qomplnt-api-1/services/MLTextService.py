from typing import List, Optional

from fastapi import Depends, HTTPException, status
from models.QomplntModel import MultiLingualText
from reposetories.MLTextRepositry import MLTextRepositry 
from schemas.QomplntSchema import MultiLingualTextSchema


class MLTextService:
    mlTextReposetry: MLTextRepositry

    def __init__(
            self, mlTextReposetry: MLTextRepositry = Depends()
    ) -> None:
        self.mlTextReposetry = mlTextReposetry  # Ensure variable names match

    def create(self, mlText_body: MultiLingualTextSchema) -> MultiLingualText:
        mlText = self.mlTextReposetry.create(
            MultiLingualText(
                keys = mlText_body.keys,
                lang_code = mlText_body.lang_code,
                display_text = mlText_body.display_text
            )
        )
        return [mlText]
    


