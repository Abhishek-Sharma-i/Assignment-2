def capitalize_name(full_name):
    words = full_name.split()
    capitalized_words = [word.capitalize() for word in words]
    return ' '.join(capitalized_words)

full_name = input("Enter the Name:").strip()
print(capitalize_name(full_name))