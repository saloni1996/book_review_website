import webbrowser

class  Book():
     def __init__(self,book_name,book_author,book_cover,author_interview,book_summary):
         self.title =book_name
         self.author =book_author
         self.cover_image =book_cover
         self.interview  =author_interview
         self.summary = book_summary
     def show_interview(self):
        webbrowser.open(self.interview)
