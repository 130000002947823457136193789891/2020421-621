from Record import radio
# from voice_recognition.py import get_text_from_voice

{
    "表白":"love.exe",
    "关机":"shutdown -s -t 600",
    "重启":"shutdown -r -t 600",
    "取消":"shutdown -a",

}

while True:
    radio("record.pcm")
    word= get_text_from_voice("record.pcm")
    print(word)

