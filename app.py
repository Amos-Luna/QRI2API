from fastapi import Form, File, UploadFile, FastAPI
from fastapi.responses import StreamingResponse
from io import BytesIO
from qr_decoder import decode_qr_link
from PIL import Image, ImageFilter
from pyzbar.pyzbar import decode
import uvicorn

app = FastAPI()

@app.post("/upload")
def extract_link_from_QR_image(img: UploadFile = File(..., 
                                                    title='QR Decoder', 
                                                    description='API that extract links associated at QR images')):
    try:
        decodeQRimage = decode(Image.open(img.file))
        data_linked = decodeQRimage[0].data.decode('ascii')
        return {'link':f'{data_linked}'}

    except Exception:
        return {"message": "There was an error uploading the file"}
    
    finally:
        img.file.close()
    
if __name__ == '__main__':
    uvicorn.run(app, host='127.0.0.1', port=8000)
