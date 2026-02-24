request:

```
curl 'https://aok.zarovizsga.hu/zvb-service/methods/feladatCsoportControl/findByGyujtemenyId' \
  -H 'Accept: application/json' \
  -H 'Accept-Language: hu,en;q=0.9' \
  -H 'Connection: keep-alive' \
  -H 'Content-Type: application/json' \
  -b 'JSESSIONID=9zZk5be-2gzj3kYLH0hbGtgvcbNuginYgr33-wAk.zarovizsga; _gid=GA1.2.2108536590.1771773584; zvSchoolId=1; _gat_gtag_UA_7095558_38=1; _ga_1X8YM8D4PJ=GS2.1.s1771778673$o2$g1$t1771779025$j60$l0$h0; _ga=GA1.1.1616961707.1771773584' \
  -H 'Origin: https://aok.zarovizsga.hu' \
  -H 'Referer: https://aok.zarovizsga.hu/' \
  -H 'Sec-Fetch-Dest: empty' \
  -H 'Sec-Fetch-Mode: cors' \
  -H 'Sec-Fetch-Site: same-origin' \
  -H 'User-Agent: Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/145.0.0.0 Safari/537.36' \
  -H 'sec-ch-ua: "Not:A-Brand";v="99", "Google Chrome";v="145", "Chromium";v="145"' \
  -H 'sec-ch-ua-mobile: ?0' \
  -H 'sec-ch-ua-platform: "macOS"' \
  --data-raw '{"gyujtemenyId":26}'
```

response:

```
{
    "result": {
        "feladatCsoport": [
            {
                "fejezet": [
                    {
                        "nev": "Kardiológia",
                        "sorszam": "1",
                        "id": 1
                    },
                    {
                        "nev": "Angiológia",
                        "sorszam": "2",
                        "id": 2
                    },
                    {
                        "nev": "Hypertonia",
                        "sorszam": "3",
                        "id": 3
                    },
                    {
                        "nev": "Pulmonológia",
                        "sorszam": "4",
                        "id": 4
                    },
                    {
                        "nev": "A nyelőcső és a gyomor betegségei",
                        "sorszam": "5",
                        "id": 5
                    },
                    {
                        "nev": "A bél betegségei",
                        "sorszam": "6",
                        "id": 6
                    },
                    {
                        "nev": "A máj betegségei",
                        "sorszam": "7",
                        "id": 7
                    },
                    {
                        "nev": "Az epehólyag és az epeutak betegségei",
                        "sorszam": "8",
                        "id": 8
                    },
                    {
                        "nev": "A hasnyálmirigy betegségei",
                        "sorszam": "9",
                        "id": 9
                    },
                    {
                        "nev": "Nefrológia",
                        "sorszam": "10",
                        "id": 10
                    },
                    {
                        "nev": "Endokrinológia",
                        "sorszam": "11",
                        "id": 11
                    },
                    {
                        "nev": "Diabetes mellitus és egyéb anyagcsere-betegségek",
                        "sorszam": "12",
                        "id": 12
                    },
                    {
                        "nev": "Hematológia és hemosztazeológia",
                        "sorszam": "13",
                        "id": 13
                    },
                    {
                        "nev": "Klinikai immunológia és reumatológia",
                        "sorszam": "14",
                        "id": 14
                    },
                    {
                        "nev": "Intenzív betegellátás, oxiológia, mérgezések, sav-bázis egyensúly-zavarok",
                        "sorszam": "15",
                        "id": 15
                    },
                    {
                        "nev": "Klinikai genetika",
                        "sorszam": "16",
                        "id": 16
                    },
                    {
                        "nev": "Klinikai onkológia",
                        "sorszam": "17",
                        "id": 17
                    },
                    {
                        "nev": "Fertőző betegségek",
                        "sorszam": "18",
                        "id": 18
                    },
                    {
                        "nev": "Differenciáldiagnosztika",
                        "sorszam": "19",
                        "id": 19
                    }
                ],
                "id": 31,
                "rovid": "BGY",
                "nev": "Belgyógyászat",
                "frissitesFeladatCsoport": [
                    {
                        "frissitesFormatted": 1553676348000
                    }
                ]
            },
            {
                "fejezet": [],
                "id": 32,
                "rovid": "BÖR",
                "nev": "Bőrgyógyászat",
                "frissitesFeladatCsoport": [
                    {
                        "frissitesFormatted": 1553676349000
                    }
                ]
            },
            {
                "fejezet": [],
                "id": 33,
                "rovid": "FOG",
                "nev": "Fogászat",
                "frissitesFeladatCsoport": [
                    {
                        "frissitesFormatted": 1553676351000
                    }
                ]
            },
            {
                "fejezet": [],
                "id": 34,
                "rovid": "ORL",
                "nev": "Fül-orr-gégészet",
                "frissitesFeladatCsoport": [
                    {
                        "frissitesFormatted": 1553676352000
                    }
                ]
            },
            {
                "fejezet": [
                    {
                        "nev": "Általános gyermekgyógyászat",
                        "sorszam": "1",
                        "id": 350
                    },
                    {
                        "nev": "Neonatológia",
                        "sorszam": "2",
                        "id": 351
                    },
                    {
                        "nev": "Congenitalis, strukturális és biokémiai rendellenességek",
                        "sorszam": "3",
                        "id": 352
                    },
                    {
                        "nev": "Fertőző betegségek, védőoltások",
                        "sorszam": "4",
                        "id": 353
                    },
                    {
                        "nev": "Légúti megbetegedések, pulmonológia",
                        "sorszam": "5",
                        "id": 354
                    },
                    {
                        "nev": "Kardiológia",
                        "sorszam": "6",
                        "id": 355
                    },
                    {
                        "nev": "Gasztroenterológia",
                        "sorszam": "7",
                        "id": 356
                    },
                    {
                        "nev": "Gyermeknefrológia",
                        "sorszam": "8",
                        "id": 357
                    },
                    {
                        "nev": "Diabetes mellitus és endocrin betegségek",
                        "sorszam": "9",
                        "id": 358
                    },
                    {
                        "nev": "Hematológia és daganatos megbetegedések",
                        "sorszam": "10",
                        "id": 359
                    }
                ],
                "id": 35,
                "rovid": "GYE",
                "nev": "Gyermekgyógyászat",
                "frissitesFeladatCsoport": [
                    {
                        "frissitesFormatted": 1553676353000
                    }
                ]
            },
            {
                "fejezet": [],
                "id": 36,
                "rovid": "IGÜ",
                "nev": "Igazságügyi orvostan",
                "frissitesFeladatCsoport": [
                    {
                        "frissitesFormatted": 1553676354000
                    }
                ]
            },
            {
                "fejezet": [],
                "id": 37,
                "rovid": "NET",
                "nev": "Megelőző orvostan és népegészségtan",
                "frissitesFeladatCsoport": [
                    {
                        "frissitesFormatted": 1553676355000
                    }
                ]
            },
            {
                "fejezet": [
                    {
                        "nev": "Cerebrovascularis betegségek",
                        "sorszam": "1",
                        "id": 868
                    },
                    {
                        "nev": "Fejfájás és fájdalom",
                        "sorszam": "2",
                        "id": 869
                    },
                    {
                        "nev": "Az idegrendszer gyulladásos megbetegedései, sclerosis multiplex",
                        "sorszam": "3",
                        "id": 870
                    },
                    {
                        "nev": "Epilepsia",
                        "sorszam": "4",
                        "id": 871
                    },
                    {
                        "nev": "Extrapyramidum",
                        "sorszam": "5",
                        "id": 872
                    },
                    {
                        "nev": "Neuromuscularis betegségek",
                        "sorszam": "6",
                        "id": 873
                    }
                ],
                "id": 38,
                "rovid": "NEU",
                "nev": "Neurológia",
                "frissitesFeladatCsoport": [
                    {
                        "frissitesFormatted": 1553676359000
                    }
                ]
            },
            {
                "fejezet": [
                    {
                        "nev": "Gyermeknőgyógyászat",
                        "sorszam": "1",
                        "id": 894
                    },
                    {
                        "nev": "A menses rendellenességei",
                        "sorszam": "2",
                        "id": 895
                    },
                    {
                        "nev": "A külső és belső genitalék gyulladásos betegségei",
                        "sorszam": "3",
                        "id": 896
                    },
                    {
                        "nev": "A külső és belső genitalék daganatos betegségei",
                        "sorszam": "4",
                        "id": 897
                    },
                    {
                        "nev": "Fogamzásgátlás, családtervezés",
                        "sorszam": "5",
                        "id": 898
                    },
                    {
                        "nev": "Meddőség",
                        "sorszam": "6",
                        "id": 899
                    },
                    {
                        "nev": "A terhesség élettana",
                        "sorszam": "7",
                        "id": 900
                    },
                    {
                        "nev": "Patológiai terhesség",
                        "sorszam": "8",
                        "id": 901
                    },
                    {
                        "nev": "Terhesség és extragenitalis betegségek",
                        "sorszam": "9",
                        "id": 902
                    },
                    {
                        "nev": "Spontán és művi vetélés",
                        "sorszam": "10",
                        "id": 903
                    },
                    {
                        "nev": "Szülés és szövődményei",
                        "sorszam": "11",
                        "id": 904
                    },
                    {
                        "nev": "Terhestanácsadás",
                        "sorszam": "12",
                        "id": 905
                    }
                ],
                "id": 39,
                "rovid": "NSZ",
                "nev": "Nőgyógyászat, szülészet",
                "frissitesFeladatCsoport": [
                    {
                        "frissitesFormatted": 1553676360000
                    }
                ]
            },
            {
                "fejezet": [],
                "id": 40,
                "rovid": "ORT",
                "nev": "Ortopédia",
                "frissitesFeladatCsoport": [
                    {
                        "frissitesFormatted": 1553676361000
                    }
                ]
            },
            {
                "fejezet": [
                    {
                        "nev": "ÁLTALÁNOS PSZICHIÁTRIA",
                        "sorszam": "1",
                        "id": 1655
                    },
                    {
                        "nev": "PSZICHIÁTRIAI BETEGVIZSGÁLAT",
                        "sorszam": "2",
                        "id": 1656
                    },
                    {
                        "nev": "PSZICHOPATOLÓGIA",
                        "sorszam": "3",
                        "id": 1657
                    },
                    {
                        "nev": "MENTÁLIS ZAVAROK",
                        "sorszam": "4",
                        "id": 1658
                    },
                    {
                        "nev": "PSZICHOFARMAKOTERÁPIA",
                        "sorszam": "5",
                        "id": 1659
                    },
                    {
                        "nev": "PSZICHO ÉS SZOCIOTERÁPIÁK",
                        "sorszam": "6",
                        "id": 1660
                    }
                ],
                "id": 41,
                "rovid": "PSY",
                "nev": "Pszichiátria",
                "frissitesFeladatCsoport": [
                    {
                        "frissitesFormatted": 1553676362000
                    }
                ]
            },
            {
                "fejezet": [],
                "id": 140,
                "rovid": "REU",
                "nev": "Reumatológia",
                "frissitesFeladatCsoport": [
                    {
                        "frissitesFormatted": 1553676395000
                    }
                ]
            },
            {
                "fejezet": [
                    {
                        "nev": "Általános sebészet",
                        "sorszam": "1",
                        "id": 1241
                    },
                    {
                        "nev": "Traumatológia",
                        "sorszam": "2",
                        "id": 1242
                    },
                    {
                        "nev": "Akut has, peritonitisek",
                        "sorszam": "3",
                        "id": 1243
                    },
                    {
                        "nev": "Gasztroenterológiai sebészet",
                        "sorszam": "4",
                        "id": 1244
                    },
                    {
                        "nev": "Mellkassebészet",
                        "sorszam": "5",
                        "id": 1245
                    },
                    {
                        "nev": "Szív- és érsebészet",
                        "sorszam": "6",
                        "id": 1246
                    },
                    {
                        "nev": "Idegsebészet",
                        "sorszam": "7",
                        "id": 1247
                    },
                    {
                        "nev": "Érsebészet",
                        "sorszam": "8",
                        "id": 1661
                    },
                    {
                        "nev": "Gyermeksebészet",
                        "sorszam": "9",
                        "id": 1662
                    },
                    {
                        "nev": "Plasztikai sebészet",
                        "sorszam": "10",
                        "id": 1663
                    },
                    {
                        "nev": "Aneszteziológia és intenzív terápia",
                        "sorszam": "11",
                        "id": 1664
                    }
                ],
                "id": 42,
                "rovid": "SEB",
                "nev": "Sebészet",
                "frissitesFeladatCsoport": [
                    {
                        "frissitesFormatted": 1553676363000
                    }
                ]
            },
            {
                "fejezet": [],
                "id": 43,
                "rovid": "SZEM",
                "nev": "Szemészet",
                "frissitesFeladatCsoport": [
                    {
                        "frissitesFormatted": 1553676364000
                    }
                ]
            },
            {
                "fejezet": [],
                "id": 44,
                "rovid": "URO",
                "nev": "Urológia",
                "frissitesFeladatCsoport": [
                    {
                        "frissitesFormatted": 1553676366000
                    }
                ]
            }
        ],
        "id": 26
    }
}
```

request:

```
curl 'https://aok.zarovizsga.hu/zvb-service/methods/kerdesControl/getGroupOrChapterQuestionsCount' \
  -H 'Accept: application/json' \
  -H 'Accept-Language: hu,en;q=0.9' \
  -H 'Connection: keep-alive' \
  -H 'Content-Type: application/json' \
  -b 'JSESSIONID=9zZk5be-2gzj3kYLH0hbGtgvcbNuginYgr33-wAk.zarovizsga; _gid=GA1.2.2108536590.1771773584; zvSchoolId=1; _gat_gtag_UA_7095558_38=1; _ga_1X8YM8D4PJ=GS2.1.s1771778673$o2$g1$t1771778674$j59$l0$h0; _ga=GA1.1.1616961707.1771773584' \
  -H 'Origin: https://aok.zarovizsga.hu' \
  -H 'Referer: https://aok.zarovizsga.hu/' \
  -H 'Sec-Fetch-Dest: empty' \
  -H 'Sec-Fetch-Mode: cors' \
  -H 'Sec-Fetch-Site: same-origin' \
  -H 'User-Agent: Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/145.0.0.0 Safari/537.36' \
  -H 'sec-ch-ua: "Not:A-Brand";v="99", "Google Chrome";v="145", "Chromium";v="145"' \
  -H 'sec-ch-ua-mobile: ?0' \
  -H 'sec-ch-ua-platform: "macOS"' \
  --data-raw '{"feladatcsoport_id":44,"fejezet_id":null}'
```

response:
`{"count":88}`

request:

```
curl '<https://aok.zarovizsga.hu/zvb-service/methods/kerdesControl/getQuestionByLimit>' \
 -H 'Accept: application/json' \
 -H 'Accept-Language: hu,en;q=0.9' \
 -H 'Connection: keep-alive' \
 -H 'Content-Type: application/json' \
 -b 'JSESSIONID=9zZk5be-2gzj3kYLH0hbGtgvcbNuginYgr33-wAk.zarovizsga; \_gid=GA1.2.2108536590.1771773584; zvSchoolId=1; \_gat_gtag_UA_7095558_38=1; \_ga_1X8YM8D4PJ=GS2.1.s1771778673$o2$g1$t1771778674$j59$l0$h0; \_ga=GA1.1.1616961707.1771773584' \
 -H 'Origin: <https://aok.zarovizsga.hu>' \
 -H 'Referer: <https://aok.zarovizsga.hu/>' \
 -H 'Sec-Fetch-Dest: empty' \
 -H 'Sec-Fetch-Mode: cors' \
 -H 'Sec-Fetch-Site: same-origin' \
 -H 'User-Agent: Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/145.0.0.0 Safari/537.36' \
 -H 'sec-ch-ua: "Not:A-Brand";v="99", "Google Chrome";v="145", "Chromium";v="145"' \
 -H 'sec-ch-ua-mobile: ?0' \
 -H 'sec-ch-ua-platform: "macOS"' \
 --data-raw '{"feladatcsoport_id":44,"fejezet_id":null,"tol":0,"darab":20,"token":null}'`

response:
`[
    {
        "csorszam": "URO - 1",
        "magyarazatPlaintext": null,
        "alSorszam": 0,
        "subSorszam": 0,
        "vanKepIn": 0,
        "kerdesValasz": [
            {
                "helyes": 0,
                "magyarazatPlaintext": null,
                "vanKepIn": 0,
                "betujel": "B",
                "szoveg": "heretorzió",
                "magyarazat": null,
                "id": 256444,
                "szovegPlaintext": "heretorzió"
            },
            {
                "helyes": 0,
                "magyarazatPlaintext": null,
                "vanKepIn": 0,
                "betujel": "A",
                "szoveg": "sérülés",
                "magyarazat": null,
                "id": 256443,
                "szovegPlaintext": "sérülés"
            },
            {
                "helyes": 0,
                "magyarazatPlaintext": null,
                "vanKepIn": 0,
                "betujel": "D",
                "szoveg": "BRCA2 mutáció",
                "magyarazat": null,
                "id": 256446,
                "szovegPlaintext": "BRCA2 mutáció"
            },
            {
                "helyes": 1,
                "magyarazatPlaintext": "Heretumor kialakulásában az egyetlen bizonyított rizikófaktor a retineált here (ebben az esetben a heretumor 10-20-szor gyakoribb). A sérülés, heretorsio, genetikai prediszpozíció szerepe nem bizonyított. ",
                "vanKepIn": 0,
                "betujel": "C",
                "szoveg": "retineált here",
                "magyarazat": "Heretumor kialakulásában az egyetlen bizonyított rizikófaktor a retineált here (ebben az esetben a heretumor 10-20-szor gyakoribb). A sérülés, heretorsio, genetikai prediszpozíció szerepe nem bizonyított. ",
                "id": 256445,
                "szovegPlaintext": "retineált here"
            }
        ],
        "leiras": "A heretumor kialakulásában az alábbi okok közül csak egy igaz:",
        "nehezseg": null,
        "feladatTipusId": 1,
        "statuszId": null,
        "sorszam": 1,
        "magyarazat": null,
        "id": 63610,
        "leirasPlaintext": "A heretumor kialakulásában az alábbi okok közül csak egy igaz:",
        "nemperm": false,
        "aktiv": true
    },
    {
        "csorszam": "URO - 2",
        "magyarazatPlaintext": null,
        "alSorszam": 0,
        "subSorszam": 0,
        "vanKepIn": 0,
        "kerdesValasz": [
            {
                "helyes": 0,
                "magyarazatPlaintext": null,
                "vanKepIn": 0,
                "betujel": "D",
                "szoveg": "varicokele",
                "magyarazat": null,
                "id": 256450,
                "szovegPlaintext": "varicokele"
            },
            {
                "helyes": 0,
                "magyarazatPlaintext": null,
                "vanKepIn": 0,
                "betujel": "C",
                "szoveg": "hydrokele",
                "magyarazat": null,
                "id": 256449,
                "szovegPlaintext": "hydrokele"
            },
            {
                "helyes": 1,
                "magyarazatPlaintext": "Epididymitis esetében a beteg mellékheréje és heréje megnagyobbodott, tapintáskor kifejezett fájdalmat jelez. Heretumor esetében fájdalmatlan göb tapintható a herében, vagy az egész here megnagyobbodott, fájdalmatlan. A varicokele húzó jellegű heretáji fájdalmat okozhat, tapinthatók a tyúkbélszerűen tágult vénák, a here tapintáskor nem fájdalmas. A hydrokele átvilágítható, fájdalmatlan, tapintáskor fluktuáló folyadék észlelhető. ",
                "vanKepIn": 0,
                "betujel": "B",
                "szoveg": "epididymitis",
                "magyarazat": "Epididymitis esetében a beteg mellékheréje és heréje megnagyobbodott, tapintáskor kifejezett fájdalmat jelez. Heretumor esetében fájdalmatlan göb tapintható a herében, vagy az egész here megnagyobbodott, fájdalmatlan. A varicokele húzó jellegű heretáji fájdalmat okozhat, tapinthatók a tyúkbélszerűen tágult vénák, a here tapintáskor nem fájdalmas. A hydrokele átvilágítható, fájdalmatlan, tapintáskor fluktuáló folyadék észlelhető. ",
                "id": 256448,
                "szovegPlaintext": "epididymitis"
            },
            {
                "helyes": 0,
                "magyarazatPlaintext": null,
                "vanKepIn": 0,
                "betujel": "A",
                "szoveg": "heretumor",
                "magyarazat": null,
                "id": 256447,
                "szovegPlaintext": "heretumor"
            }
        ],
        "leiras": "Jelölje meg azt a kórképet, melyben típusos esetben a scrotum tartalmának tapintásakor a beteg fájdalmat jelez:",
        "nehezseg": null,
        "feladatTipusId": 1,
        "statuszId": null,
        "sorszam": 2,
        "magyarazat": null,
        "id": 63611,
        "leirasPlaintext": "Jelölje meg azt a kórképet, melyben típusos esetben a scrotum tartalmának tapintásakor a beteg fájdalmat jelez:",
        "nemperm": false,
        "aktiv": true
    },
...
```

```
 {
        "csorszam": "BGY - 6.20",
        "magyarazatPlaintext": null,
        "fejezetId": 6,
        "alSorszam": 20,
        "subSorszam": 0,
        "vanKepIn": 0,
        "kerdesValasz": [
            {
                "helyes": 0,
                "magyarazatPlaintext": "",
                "vanKepIn": 0,
                "betujel": "D",
                "szoveg": "csak a 4. válasz helyes",
                "magyarazat": "",
                "id": 133427,
                "szovegPlaintext": "csak a 4. válasz helyes"
            },
            {
                "helyes": 1,
                "magyarazatPlaintext": "A szénhidrátok felszívódási zavarait (különböző szinteken) a kérdésben felsorolt lehetőségek egyaránt jellemzik.",
                "vanKepIn": 0,
                "betujel": "E",
                "szoveg": "mind a 4 válasz helyes",
                "magyarazat": "A szénhidrátok felszívódási zavarait (különböző szinteken) a kérdésben felsorolt lehetőségek egyaránt jellemzik.",
                "id": 133428,
                "szovegPlaintext": "mind a 4 válasz helyes"
            },
            {
                "helyes": 0,
                "magyarazatPlaintext": "",
                "vanKepIn": 0,
                "betujel": "B",
                "szoveg": "az 1. és 3. válasz helyes",
                "magyarazat": "",
                "id": 133425,
                "szovegPlaintext": "az 1. és 3. válasz helyes"
            },
            {
                "helyes": 0,
                "magyarazatPlaintext": "",
                "vanKepIn": 0,
                "betujel": "C",
                "szoveg": "a 2. és 4. válasz helyes",
                "magyarazat": "",
                "id": 133426,
                "szovegPlaintext": "a 2. és 4. válasz helyes"
            },
            {
                "helyes": 0,
                "magyarazatPlaintext": "",
                "vanKepIn": 0,
                "betujel": "A",
                "szoveg": "az 1., 2. és 3. válasz helyes",
                "magyarazat": "",
                "id": 133424,
                "szovegPlaintext": "az 1., 2. és 3. válasz helyes"
            }
        ],
        "leiras": "A szénhidrátok felszívódási zavarait az alábbiak jellemzik:",
        "nehezseg": null,
        "feladatTipusId": 2,
        "statuszId": null,
        "sorszam": 6,
        "magyarazat": null,
        "id": 31813,
        "kerdesElemiValasz": [
            {
                "vanKepIn": 0,
                "szam": "1",
                "szoveg": "alacsony cukorterheléses görbe",
                "id": 17395
            },
            {
                "vanKepIn": 0,
                "szam": "2",
                "szoveg": "laktózterhelés során hasmenés jelentkezik",
                "id": 17396
            },
            {
                "vanKepIn": 0,
                "szam": "3",
                "szoveg": "lapos keményítőterhelési görbe",
                "id": 17397
            },
            {
                "vanKepIn": 0,
                "szam": "4",
                "szoveg": "laktulózterhelés során a kilégzett levegő hidrogén mennyisége megnövekszik",
                "id": 17398
            }
        ],
        "leirasPlaintext": "A szénhidrátok felszívódási zavarait az alábbiak jellemzik:",
        "nemperm": true,
        "aktiv": true
    },
```
