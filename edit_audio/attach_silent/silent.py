from pydub import AudioSegment
import glob

files = glob.glob("non_silent/*.wav")

for file in files:
  a = AudioSegment.silent(duration=0.03) #0.03秒
  b = AudioSegment.from_file(file)
  c = a + b
  new_file_name = "silent\\"+file.split('.')[0].split('\\')[-1] + ".mp3"
  print(file + " is attached! Save " + new_file_name +"!")
  c.export(new_file_name,format="mp3")