def read_emails(file_name):
	with open(file_name) as file:
		content = file.readlines()

	#Strip newlines
	content = [x.strip() for x in content]
	#Strip empty strings
	content = list(filter(None, content))
	#Strip comments
	content = [x for x in content if "#" not in x]

	return(content)