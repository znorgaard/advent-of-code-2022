def load_txt_data(file_name):
    """Loads text data from file as a single string

    Args:
        file_name: name of file to be read
    Returns:
        data from file as single string
    """
    text_file = open(file_name)
    data = text_file.read()
    text_file.close()
    return data
