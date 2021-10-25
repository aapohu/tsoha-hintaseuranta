# hintaseuranta
Kurssityö Tietokantasovellus-kurssille.
Tavoitteena oli luoda PostgreSQL-tietokannalla ja Pythonin Flask-kirjastolla [Polttoaine.netin](https://www.polttoaine.net) kaltainen hintatilastointisovellus, jossa käyttäjät ilmoittavat polttoaineiden hintoja eri jälleenmyyjillä.
Käyttäjät ovat joko tavallisia käyttäjiä tai ylläpitäjiä. 


Käyttäjä voi: 
- Tarkastella viimeisimpiä havaintoja
- Rekisteröityä 
- Tarkastella hintatilastoja
- Etsiä havaintoja tietyltä alueelta

Rekisteröitynyt käyttäjä voi:
- Ottaa yhteyden ylläpitäjään lomakkeella aseman lisäämistä varten
- Lähettää viestejä chatissa
- Ilmoittaa hintahavainnon

Ylläpitäjä voi:
- Muokata tietokannan tietoja
  - Lisätä/sulkea asemia 
  - Poistaa käyttäjien asemapyyntöjä
  - Bannata käyttäjän tai perua bannit
  - Poistaa havaintoja

**Tilanne 24.10.**

**HUOM! Testatessa ilmeni kriittinen ongelma jonka korjasin deadlinen jälkeen klo 4:24. Tarkistusmoduuli oli rikkonut sovelluksen tärkeimmän ominaisuuden eli hintojen lisäämisen.**

Sovelluksen koekäyttö [Herokussa](https://aapohu-hintaseuranta.herokuapp.com/)

Käyttöohjeet löytyvät sivulta Info.

Admin-käyttäjä on 

|Tunnus|Salasana|
| ----------- | ----------- |
| BOSS     | pomo   |
