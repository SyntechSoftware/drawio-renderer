import uuid
import logging
import subprocess

from fastapi import FastAPI, File, Form, HTTPException
from fastapi.responses import FileResponse


logger = logging.getLogger(__name__)


app = FastAPI()


@app.post("/")
async def render(file: bytes = File(), ext: str = Form()):
    source_file_path = f'/tmp/{uuid.uuid4()}.{ext}'
    target_file_path = f'/tmp/{uuid.uuid4()}.png'
    with open(source_file_path, 'wb') as f:
        f.write(file)

    try:
        subprocess.check_output(
            f"xvfb-run --auto-servernum --server-num=1 --server-args='-screen 0, 1920x1080x24' "
            f"drawio -x -f png -o {target_file_path} {source_file_path} --no-sandbox",
            shell=True
        )
    except Exception as e:
        message = 'Failed to generate image from the XML'
        logger.exception(message)
        raise HTTPException(status_code=400, detail={'error': message})

    return FileResponse(target_file_path)
