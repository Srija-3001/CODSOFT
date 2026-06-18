from transformers import BlipProcessor, BlipForConditionalGeneration
from PIL import Image

# Load pre-trained model
processor = BlipProcessor.from_pretrained(
    "Salesforce/blip-image-captioning-base"
)

model = BlipForConditionalGeneration.from_pretrained(
    "Salesforce/blip-image-captioning-base"
)

# Load image
image = Image.open("images/dog.jpg").convert("RGB")

# Convert image into model format
inputs = processor(
    image,
    return_tensors="pt"
)

# Generate caption
output = model.generate(**inputs)

caption = processor.decode(
    output[0],
    skip_special_tokens=True
)

print("\nIMAGE CAPTIONING")
print("----------------")
print("Generated Caption:", caption)