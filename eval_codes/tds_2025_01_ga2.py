import base64
from io import BytesIO
from PIL import Image

def check_image(base64_string, original_image_path):
    
    # Decode Base64 back to bytes
    try:
        decoded_data = base64.b64decode(base64_string)
    except Exception as e:
        return {"error": f"Invalid Base64 string: {e}"}
    
    # Check file size
    if len(decoded_data) > 1500:
        return {"error": f"Compressed image exceeds 1,500 bytes: {len(decoded_data)} bytes"}
    
    # Load the original image
    try:
        original_image = Image.open(original_image_path)
    except Exception as e:
        return {"error": f"Unable to open original image: {e}"}
    
    # Load the decoded image from Base64 data
    try:
        decoded_image = Image.open(BytesIO(decoded_data))
    except Exception as e:
        return 
    
    # Check dimensions match
    if decoded_image.size != original_image.size:
        return False
    
    return True
