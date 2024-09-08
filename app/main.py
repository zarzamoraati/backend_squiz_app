from fastapi import FastAPI
from fastapi import UploadFile
from typing import Union,List
from fastapi import HTTPException,Form,File
from PIL import Image
import pytesseract
from squiz_model import GenerateQuiz
from pydantic import BaseModel

app=FastAPI()


@app.get("/home")
def home():
    return "Home Server"

# TODO - Endpoints
@app.post("/squiz")
def generate_squiz(query: str = Form(...), img_ctx: Union[UploadFile, List[UploadFile]] = File(...)):
    try:
        model=GenerateQuiz()
        if len(img_ctx) == 1:
            print(img_ctx)
            obj_file=Image.open(img_ctx[0].file)
            content=pytesseract.image_to_string(obj_file)
            response=model.generate_respose(query=query,img_to_txt=str(content))
            return response
        else:
            images=""
            for image in img_ctx:
                obj_file=Image.open(image.file)
                content=pytesseract.image_to_string(obj_file)
                images+=str(content)
            response=model.generate_respose(query=query,img_to_txt=images)

    except Exception as e:
        return {"error":e}
    
