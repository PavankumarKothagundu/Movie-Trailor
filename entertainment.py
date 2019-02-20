import mediafile

import fresh_tomatoes

agnyathavasi=mediafile.Tollywoodmovies("Agnyathavasi",
                                       "Trivikram celluloid",
                                       "http://jollyhoo.com/wp-content/uploads/2017/12/Agnathavasi-Movie-Poster-Designs-2-2-650x974.jpeg",
                                       "https://youtu.be/97h9fBWltBM")
attharintikidharedhi=mediafile.Tollywoodmovies("Attharintiki Dharedhi",
                                "Blockbuster in TFI HISTORY",
                                "https://in.bmscdn.com/iedb/movies/images/website/poster/large/attarintiki-daredi--telugu--et00016283-24-03-2017-20-02-20.jpg",
                                "https://www.youtube.com/watch?v=yMDHv-BtGHQ")
katamarayudu=mediafile.Tollywoodmovies("Katamarayudu",
                                       "Powerpacked action",
                                       "https://image.tmdb.org/t/p/original/sCpQN3MEjryl2n5uooadADP5en5.jpg",
                                       "https://www.youtube.com/watch?v=XpAaOER_6iY")
gabbarsingh=mediafile.Tollywoodmovies("Sabbarsingh",
                                      "Harishshankar film",
                                      "https://photogallery.navbharattimes.indiatimes.com/photo/12791299.cms",
                                      "https://www.youtube.com/watch?v=FpFoQPj4sgs")
sardar=mediafile.Tollywoodmovies("Sardar",
                                 "Guts Guns and Love",
                                 "https://timesofindia.indiatimes.com/thumb/61284794.cms?width=219&height=317&imgsize=167106",
                                 "https://www.youtube.com/watch?v=JoYJga1A_UY")
gopalagopala=mediafile.Tollywoodmovies("GopalaGopala",
                                       "Multistarer Performance",
                                       "https://upload.wikimedia.org/wikipedia/en/thumb/5/5f/Gopala_Gopala_poster.jpg/220px-Gopala_Gopala_poster.jpg",
                                       "https://www.youtube.com/watch?v=bqEcBIaSRBE")

                                       
                                 
movies=[agnyathavasi,attharintikidharedhi,katamarayudu,gabbarsingh,sardar,gopalagopala]
fresh_tomatoes.open_movies_page(movies)
                                
