# hintaseuranta
Tavoitteena on luoda [Polttoaine.netin](https://www.polttoaine.net) kaltainen hintatilastointisovellus, jossa käyttäjät ilmoittavat polttoaineiden hintoja eri jälleenmyyjillä.
Käyttäjät ovat joko tavallisia käyttäjiä tai ylläpitäjiä.

**Tilanne 10.10.**

Sovelluksen koekäyttö [Herokussa](https://aapohu-hintaseuranta.herokuapp.com/)

Uusia juttuja:
- E85 nyt myös mukana
- Etusivulla chat
- Ikonit
- Yläpalkissa kaikki tarpeelliset linkit
- Käyttäjillä omat profiilisivu
- Asemilla omat sivut
- Peruskäyttäjät voivat pyytää asemia lisättäväksi
- Admin voi kuitata em. pyyntöjä

Sisäänkirjautunut käyttäjä voi lisätä hintahavainnon "Lisää havainto"-linkin kautta. Hintaa lisätessä tulee manuaalisesti valita aseman numero alla olevasta listasta. 

Uuden aseman voi lisätä kirjautumalla sisään adminiksi (tunnus BOSS salasana pomo) josta löytyvästä lomakkeesta aseman voi lisätä. Kenttään Tie tulee laittaa pieninumeroisin järkevän lähellä oleva tie.

Käyttäjä voi: 
- Rekisteröityä 
- Ilmoittaa hintahavainnon (käyttöliittymä kesken)
- Ottaa yhteyden ylläpitäjään lomakkeella myyntipaikan lisäämistä varten
- Tarkastella viimeisimpiä havaintoja (lajitteluominaisuus kesken)
- Etsiä havaintoja tietyltä alueelta (kesken)
- Tarkastella tilastoja, esimerkiksi viikonpäivien keskihintoja tai kuukausittaisia keskihintoja. (kesken)

Ylläpitäjä voi:
- Muokata tietokannan tietoja
  - Lisätä/sulkea asemia 
  - Poistaa käyttäjien asemapyyntöjä
  - Bannata käyttäjän tai perua bannit
  - Poistaa havaintoja (kesken)




