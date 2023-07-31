import pytest
from lib.calculate_reading_time import *

def test_short_text():
    result = calculate_reading_time("This is a very short sentence that contains ten words.")
    assert result == 0.05

def test_with_two_hundred_words():
    result = calculate_reading_time("Lorem ipsum dolor sit amet, consectetur adipiscing elit. Morbi ipsum ex, pharetra a blandit non, malesuada at odio. Vivamus faucibus rutrum est, ut cursus sem porttitor vitae. Nullam congue sem id orci fermentum, non pretium diam feugiat. Nulla placerat odio quis ipsum efficitur condimentum. Suspendisse lacus felis, faucibus sit amet turpis in, varius sodales arcu. Maecenas viverra mattis mauris. Quisque molestie porttitor massa non auctor. Nunc non odio ac lacus gravida pretium. Maecenas efficitur pretium est dapibus tempus. Duis id metus cursus, tincidunt nibh et, maximus turpis. Interdum et malesuada fames ac ante ipsum primis in faucibus. Donec efficitur facilisis dui, quis volutpat lectus lacinia id. Nulla mattis luctus ex, a semper ligula ullamcorper eget. Aenean pulvinar, nibh id ornare rhoncus, ligula nisi sollicitudin lectus, sed fermentum est nisi sed est. Phasellus lorem tellus, iaculis id quam viverra, aliquam vestibulum dolor. Phasellus id nisi mauris. Phasellus non justo urna. Vivamus et massa elementum, condimentum nisl non, maximus diam. Proin in erat eget eros volutpat euismod. Sed venenatis nisl mi, nec eleifend augue scelerisque mollis. Pellentesque sit amet feugiat nisi. Nam vel auctor nulla. Etiam finibus at risus a eleifend. Mauris fermentum odio in nibh euismod, eget varius enim laoreet. Nam.")
    assert result == 1

def test_with_three_hundred_words():
    words = []
    for i in range(0, 300):
        words.append("word")
    result = calculate_reading_time(" ".join(words))
    assert result == 1.5
    
def test_with_an_empty_string():
    result = calculate_reading_time("")
    assert result == 0

def test_none_input():
    with pytest.raises(Exception) as e:
        calculate_reading_time(None)
    error_message = str(e.value)
    assert error_message == 'No text was given. Cannot estimate reading time.'
