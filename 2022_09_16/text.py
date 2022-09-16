def main():
    title = "Howl's Moving Castle"
    genre = "Japanese Animation"
    author = "Miyazaki Hayao"
    year = 2004
    imdb = 8.2
    name_of_main_character = "Sophie"
    length_in_mins = 119
    original_lang = "Japanese"
    job_of_main_character = "hatmaker"
    
    text = """\
    {title} is a {genre} film, written by {author}.
    The film was produced in {year}. It's IMDB rating is {imdb}.
    The main character's name {name_of_main_character} is who is a {job}.
    The film is {length_in_mins} mins long. The original language is {original_lang}."""
    
    print(text.format(title = title, genre = genre, author = author, year = year, imdb = imdb, name_of_main_character = name_of_main_character, job = job_of_main_character, length_in_mins = length_in_mins, original_lang = original_lang))
    
main()