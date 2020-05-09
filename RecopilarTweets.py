import tweepy

#Credenciales de la API de Twitter.
consumer_key = ''
consumer_secret = ''
access_token = ''
access_token_secret = ''

#Autenticación con las credenciales.
auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)
api = tweepy.API(auth, wait_on_rate_limit=True)

#Variables sobre la búsqueda.
palabra_clave = "feminismo"
max_tweets = 10
desde ="2015-01-01"

#Creación de archivos de texto y excel con los resultados.
archivo_texto = open("tweets_"+palabra_clave+".txt", 'w', encoding='utf-8')
archivo_excel = open("tweets_"+palabra_clave+".xls", 'w', encoding='utf-8')

tweets_obtenidos = 0 #Variable de corte.

#Búsqueda y almacenamiento de tweets.
print("Recopilando", max_tweets, "tweets con la palabra: '", palabra_clave,"'.")
for tweet in tweepy.Cursor( api.search,
                            q = palabra_clave+" -filter:retweets",
                            count = 10,
                            lang="es",
                            since=desde).items():
    #Auxiliares para el formato de los tweets.
    res_texto = ""
    res_excel = ""

    #Formateo de los tweets.
    res_texto = str(tweet.created_at) + ": " + str(tweet.text.encode('utf-8')) + "\n"
    res_excel = str(tweet.created_at) + "\t" + str(tweet.text.encode('utf-8')) + "\n"

    #Almacenamiento de los tweets en archivos.
    archivo_texto.write(res_texto)
    archivo_excel.write(res_excel)
    
    #Condición de paro.
    tweets_obtenidos += 1
    if tweets_obtenidos == max_tweets:
        print("Se recopilaron", max_tweets, "tweets que contienen la palabra: '", palabra_clave,"'.")
        break
    else:
        print (tweets_obtenidos, "de", max_tweets, "tweets recopilados.")

print("Se guardaron los resultados en los archivos", "tweets_"+palabra_clave+".txt", "y", "tweets_"+palabra_clave+".xls")
archivo_texto.close()
archivo_excel.close()