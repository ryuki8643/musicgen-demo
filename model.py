import torchaudio, os, shutil
from audiocraft.models import MusicGen
from audiocraft.data.audio import audio_write

model = MusicGen.get_pretrained("melody")
model.set_generation_params(duration=30)


def genarate_melody(text):
    input_file = "input.wav"
    output_file = "output.wav"

    if os.path.isfile(input_file):
        os.remove(input_file)

    if os.path.isfile(output_file):
        shutil.copy(output_file, input_file)

        input_melody, sr = torchaudio.load(output_file)

        wav = model.generate_with_chroma(text, input_melody, sr)

        audio_write(
            output_file,
            wav.cpu(),
            model.sample_rate,
            strategy="loudness",
            loudness_compressor=True,
        )
    else:
        wav = model.generate(
            [
                text,
            ],
        )
