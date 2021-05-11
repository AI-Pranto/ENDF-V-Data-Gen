new_readme = "ENDF-V8 Data Generator. \n"
	"Processed ENDF-V8 endf in h5 file format using GitHub actions CI pipline.\n"

with open("README.md", "w") as text_file:
    text_file.write(new_readme)
