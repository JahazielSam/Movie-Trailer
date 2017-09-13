import media
import fresh_tomatoes

priceless=media.Movie("Priceless","A man saving two women who were marked as they were worth a certain price.","http://pricelessthemovie.com/_images/share_main.jpg","https://www.youtube.com/watch?v=zbKempXyz9I")

the_last_song=media.Movie("The Last Song","A love story of the international song writer Miley Cyrus","https://images-na.ssl-images-amazon.com/images/M/MV5BMjE2MTcyMjMyNF5BMl5BanBnXkFtZTgwODg2ODU1MDE@._V1_UY1200_CR90,0,630,1200_AL_.jpg","https://www.youtube.com/watch?v=vZH0Nf4KLBo")

finding_nemo=media.Movie("Finding Nemo","A story of a marine world where a father clown fish finds his son travelling all across the sea","https://fiu-assets-2-syitaetz61hl2sa.stackpathdns.com/static/use-media-items/17/16316/full-900x1300/56702cc2/pva6ds.jpeg?resolution=0","https://www.youtube.com/watch?v=wZdpNglLbt8")


#priceless.show_trailer()
movies=[priceless,the_last_song,finding_nemo]
fresh_tomatoes.open_movies_page(movies)


