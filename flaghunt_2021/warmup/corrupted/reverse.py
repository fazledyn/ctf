
in_file = open("file", "r")
content = in_file.read()

out_file = open("outfile.svg", "w")
out_file.write(content[::-1])
out_file.close()

#	After this, remove the <rect> tag from SVG