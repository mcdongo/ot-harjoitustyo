<h1>Cave Crawler</h1>
<hr>
Sovellus on reaaliaikainen ylhäältäkuvattu dungeon crawler -tyyppinen peli, jossa on samanlainen taistelujärjestelmä, joka tunnetaan Legend of Zeldasta.
Peli toteutetaan Pythonilla ja tämän pygame-kirjastolla.<br>
Peli koostuu kerroksista, joissa on rappuset seuraavaan kerrokseen jossakin ja pelaajan on määrä löytää kyseiset rappuset edetäkseen.
Kerroksista saattaa löytyä jonkin kaltaisia aivopähkinöitä, vihollisia ja esineitä, joista on hyötyä pelaajalle.
Pelaajalla on lähtökohtaisesti miekka sekä kilpi. Riippuen kerroksesta, saattaa huoneet olla pimeitä, eli pelaaja näkee vain lyhyeelle alueelle ympärillään.
<hr>
<h2>Ominaisuuksia:</h2>
* Pelaajan tiedot tallennetaan tietokantaan (Mikä kerros, mitä tavaroita löytyy laukusta, elämäpisteiden tilanne jne)<br>
* Kerroksia generoidaan tarvittaessa satunnaisesti (ehkä jokin endless mode tarjolle)<br>
* Peli on suunniteltu grid-tyyliin, eli kaikki asiat liikkuvat ennalta määrättyissä "laatikoissa" laatikosta toiseen<br>
* Pelaajalle sallitaan normaalien kontrollien lisäksi muutama pikanäppäin, joihin pelaaja voi linkittää asioita laukusta; eli ei tarvitse avata menua käyttääkseen jotain esinettä, jota tarvitsee usein<br>
* Laukun sisällön sekä menun avaaminen pausettaa pelin
