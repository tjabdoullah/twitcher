import sys
print('Moving Left')
args = sys.argv
print(args)
file_content = "Moved Left"
if len(sys.argv) == 2:
  file_content = sys.argv[1]
f = open("Moved Left", "a")
f.write(file_content + "\n")
f.close()
