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
    return "hello word"

# TODO - Endpoints
@app.post("/squiz")
def generate_squiz(query: str = Form(...), img_ctx: Union[UploadFile, List[UploadFile]] = File(...)):
    try:
        print("IMAGE:",img_ctx)
        obj_file=Image.open(img_ctx[0].file)
        content=pytesseract.image_to_string(obj_file)
        print("Encode complete")
        model=GenerateQuiz()
        print("Showing content:",content)
        response=model.generate_respose(query=query,img_to_txt=str(content))
        return response
    
    except Exception as e:
        return {"error":e}
    
## TODO - Process Request


#    if isinstance(img_ctx,List[UploadFile]):
#             pass
    #        raise HTTPException(status_code=403,detail="Invalid Format")
