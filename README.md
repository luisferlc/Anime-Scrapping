<img src="https://github.com/luisferlc/Anime-Scrapping/blob/master/images/saitama.png">

# Web Scrapping
Durante el bootcamp en Iron Hack nos dieron la tarea de hacer algun proyecto de scrapping a alguna página web. Siendo alguien que ve anime, encontre en Kaggle un dataset que tiene rankeados a miles de animes, así como otra información sobre ellos (https://www.kaggle.com/canggih/anime-data-score-staff-synopsis-and-genre).

Este es un proyecto que hice en noviembre del 2019 y ahora acabo de modificar, ya que por lo general, las páginas web cambian su estructura seguido. Entonces, tuve que meterme y probar el sistema para ver si funcionaba bien. Encontre algunos cambios, mismos que ya se hicieron. Mi intención fue crear un scrapping que me permitiera obtener un dataset igual al que vi en la página de Kaggle.

Dentro de este repositorio voy a dejar un .csv con los top 1500 animes según https://myanimelist.net/, el cual tiene un formato adecuado para empezar a hacer análisis de información.

# Información de myanimelist.net vs scrapping

Directamente desde la página web, esta es la información que vas a encontrar:

<img src="https://github.com/luisferlc/Anime-Scrapping/blob/master/images/full.PNG">
<img src="https://github.com/luisferlc/Anime-Scrapping/blob/master/images/fullm.PNG">

Así es como se ve el .csv scrapeeado:

<img src="https://github.com/luisferlc/Anime-Scrapping/blob/master/images/scrapped.PNG">

Si deseas poder utilizar este sistema de scrapping para descargarte la información de myanimelist.net, necesitas descargar el exe_web_project.py y web_project_anime.py, y ponerlos en un mismo directorio. Después, dentro del exe_web_project.py hay una variable llamada "anime_to_scrape" la cual esta definida con 50. Tu podrías modificar este valor y decidir descargar la información de los animes que desees. Luego solamente ejecutras el exe_web_project.py y el .csv se va generar.

## Librerías utilizadas:
* pandas
* BeautifulSoup
* requests
* time
