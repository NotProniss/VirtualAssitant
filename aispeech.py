from transformers import AutoProcessor, BarkModel
import scipy
import torch

device = "cuda" if torch.cuda.is_available() else "cpu"
processor = AutoProcessor.from_pretrained("suno/bark")
#model = BarkModel.from_pretrained("suno/bark", torch_dtype=torch.float16, use_flash_attention_2=True).to(device)
model = BarkModel.from_pretrained("suno/bark").to(device)
model =  model.to_bettertransformer()


inputs = processor(
    text=["Hello, my name is Lucy. And, uh — and I like pizza. [laughs] But I also have other interests such as playing tic tac toe."],
    return_tensors="pt",
)
inputs = inputs.to(device)
speech_values = model.generate(**inputs, do_sample=True)

sampling_rate = 24000
scipy.io.wavfile.write("bark_out.wav", rate=sampling_rate, data=speech_values.cpu().numpy().squeeze())
