import os
from typing import List
from pathlib import Path
from pydub import AudioSegment


def get_mp3_files(directory: str) -> List[AudioSegment]:
    mp3_files = []
    directory_path = Path(directory)

    for file in directory_path.glob("*.mp3"):
        if file.name != "combined_music.mp3":
            audio_seg = AudioSegment.from_mp3(file)
            mp3_files.append(audio_seg)

    return mp3_files


def merge_songs(sounds: List[AudioSegment], output_path: str) -> None:
    if not sounds:
        print("No mp3 audio files found.")
        return

    print("combining files...")
    combined_sound = None
    for sound in sounds:
        if combined_sound is None:
            combined_sound = sound
        else:
            combined_sound = combined_sound.append(sound, crossfade=1500)
    if combined_sound:
        combined_sound.export("./music/combined_music.mp3", format="mp3")
        print("Audio files successfully combined as 'combined_music.mp3'.")
    else:
        print("No audio files found.")


if __name__ == '__main__':
    # Enter directory of audio files
    directory = "./music/"
    output_file = "./music/combined_music.mp3"

    # alternately, use current directory
    #directory = os.getcwd()
    #output_file = f"{directory}/combined_music.mp3"

    sounds = get_mp3_files(directory)
    merge_songs(sounds, output_file)
