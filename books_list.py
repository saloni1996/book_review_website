import book_main as bm
import fresh_tomatoes

hp_1 = bm.Book('Harry Potter and Philospher Stone','J.K. Rowling',"http://i.huffpost.com/gen/989163/images/o-NEW-HARRY-POTTER-COVER-facebook.jpg","https://www.youtube.com/watch?v=i_up1VTG7Fs","Book is about a young wizard Harry Potter and his adventures in wizarding world at the first year with his other wizard friends Hermoine and Ron ")

hp_2 = bm.Book('Harry Potter and Chambers of Secret','J.K. Rowling',"http://static2.hypable.com/wp-content/uploads/2013/05/harry-potter-new-chamber-of-secrets-cover-630.jpg","https://www.youtube.com/watch?v=i_up1VTG7Fs","Book is about a young wizard Harry Potter and his adventures in wizarding world at his second year with his friends to unravel the mystery of Chambers of Secret")

hp_3 = bm.Book('Harry Potter and Prisoner of Azkaban','J.K. Rowling',"http://static3.businessinsider.com/image/522e2499ecad04ee4dba226d-1200-900/prisoner%20of%20azkaban-1.jpg","https://www.youtube.com/watch?v=i_up1VTG7Fs","Book is about a young wizard Harry Potter and his adventures in wizarding world at his third year and is met with a new guest Sirius Black")

hp_4 = bm.Book('Harry Potter and Goblet of Fire','J.K. Rowling',"https://dotgumbi.files.wordpress.com/2014/07/goblet.png","https://www.youtube.com/watch?v=i_up1VTG7Fs","Book is about a young wizard Harry Potter and his adventures in wizarding world at his fourth year and participates in Triwizard Cup")

hp_5 = bm.Book('Harry Potter and Order of Phoenix','J.K. Rowling',"https://s-media-cache-ak0.pinimg.com/736x/33/fc/e3/33fce36acccd956d4b3dfa64c8ba1589.jpg","https://www.youtube.com/watch?v=i_up1VTG7Fs","Book is about a young wizard Harry Potter and his adventures in wizarding world at his fifth year and fighting with Order of Phoenix")

hp_6 = bm.Book('Harry Potter and Half Blood Prince','J.K. Rowling',"https://s-media-cache-ak0.pinimg.com/736x/67/c6/7f/67c67fa19b630b8998c65b9e0572bf17.jpg","https://www.youtube.com/watch?v=i_up1VTG7Fs","Book is about a young wizard Harry Potter and his adventures in wizarding world at his sixth year and guided by Dumbledore")

hp_7 = bm.Book('Harry Potter and Deathly Hallows','J.K. Rowling',"http://bookriotcom.c.presscdn.com/wp-content/uploads/2014/08/HP_pb_new_7.jpg","https://www.youtube.com/watch?v=i_up1VTG7Fs","Harry Potter is all set to destroy Voldermort and his hocruxes")

hp_8 = bm.Book('Harry Potter and Cursed Child','J.K. Rowling',"http://mediaroom.scholastic.com/files/HP_CURSED_CHILD_COVER_FINAL.jpg","https://www.youtube.com/watch?v=i_up1VTG7Fs","Epilogue of harry potter series with their children")

hunger_games1 =bm.Book('Hunger Games','Sussane Collins',"http://static2.hypable.com/wp-content/uploads/2011/10/422825083.jpeg","https://www.youtube.com/watch?v=tpCeDopdlwU","The story revolves around Panem, a depressed country, which ")

#hunger_games1.show_interview()

list_of_books = [hp_1,hp_2,hp_3,hp_4,hp_5,hp_6,hp_7,hp_8,hunger_games1]

fresh_tomatoes.open_book_page(list_of_books)
