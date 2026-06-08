from fastapi import FastAPI, UploadFile, File
from fastapi.responses import FileResponse
from rembg import remove
import uuid

app = FastAPI()

@app.post("/remove-bg")
async def remove_bg(file: UploadFile = File(...)):

    input_data = await file.read()

    output_data = remove(input_data)

    output_path = f"/tmp/{uuid.uuid4()}.png"

    with open(output_path, "wb") as f:
        f.write(output_data)

    return FileResponse(
        output_path,
        media_type="image/png",
        filename="output.png"
    )