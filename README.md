# hintaseuranta
Tavoitteena on luoda [Polttoaine.netin](https://www.polttoaine.net) kaltainen hintatilastointisovellus, jossa käyttäjät ilmoittavat polttoaineiden hintoja eri jälleenmyyjillä.
Käyttäjät ovat joko tavallisia käyttäjiä tai ylläpitäjiä.

**Tilanne 26.9.**

Sovelluksen koekäyttö [Herokussa](https://aapohu-hintaseuranta.herokuapp.com/)

Toistaiseksi sovellus näyttää vain kaikki tuoreimmat havainnot. 
Sisäänkirjautunut käyttäjä voi lisätä hintahavainnon "Lisää havainto"-linkin kautta. Hintaa lisätessä tulee manuaalisesti valita aseman numero alla olevasta listasta. 

Uuden aseman voi lisätä kirjautumalla sisään adminiksi (tunnus BOSS salasana pomo) ja menemällä urliin "/addstation", josta löytyvästä lomakkeesta aseman voi lisätä. Kenttään Tie tulee laittaa pieninumeroisin järkevän lähellä oleva tie.

Käyttäjä voi: 
- Rekisteröityä (valmis)
- Tarkastella viimeisimpiä havaintoja (toimii) ja lajitella niitä esimerkiksi sijainnin, hinnan tai ajankohdan mukaan. 
- Etsiä havaintoja tietyltä alueelta
- Tarkastella tilastoja, esimerkiksi viikonpäivien keskihintoja tai kuukausittaisia keskihintoja.
- Ilmoittaa hintahavainnon (toimii)
- Ottaa yhteyden ylläpitäjään lomakkeella myyntipaikan lisäämistä varten

Ylläpitäjä voi:
- Muokata tietokannan tietoja
  - Lisätä/poistaa polttoaineita asemilta (lisääminen toimii)
  - Lisätä/poistaa asemia (lisääminen toimii)
  - Poistaa käyttäjiä 
  - Poistaa havaintoja 


