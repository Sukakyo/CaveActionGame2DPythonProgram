import ffmpeg
import glob

files = glob.glob("input_audio/*.wav")


for file in files:
  input_stream = ffmpeg.input(file)
  print(file)
  output_stream = ffmpeg.output(input_stream,"output_audio\\"+file.split('.')[0].split('\\')[-1] + ".mp3")
  ffmpeg.run(output_stream)



#stream = ffmpeg.input("mymusic1_intro.wav")

#stream = ffmpeg.output(stream, "mymusic1_intro.mp3")

#ffmpeg.run(stream)