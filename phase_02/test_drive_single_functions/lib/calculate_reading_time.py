def calculate_reading_time(text):
    if text == "":
        return 0
    elif type(text) != str:
        raise Exception("No text was given. Cannot estimate reading time.")
    words = text.split(" ")
    return len(words) / 200
