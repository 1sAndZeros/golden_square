def make_snippet(snippet):
    words = snippet.split(' ')
    if len(words) >= 5:
        return ' '.join(words[:5]) + '...'
    else:
        return snippet