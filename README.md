# Network Rail National Hazard Directory data

This is all of the [National Hazard Directory](https://on-trac.co.uk/nhd/) data that is made available to the public via the [Railhub Access Points](https://play.google.com/store/apps/details?id=uk.co.ontrac.accesspoints) app.

It is a mix of JSON and CSV, and we have yet to convert the CSV to anything better. Some notes on the CSV column meanings are below as they lack headers.

This data is automatically updated daily.

# Regions (data/regions.json)
```
{"QT":"Anglia","QK":"Kent","QG":"London North East","QR":"London North West (North)","QS":"London North West (South)","QM":"East Midlands","QL":"Scotland","QC":"Wales","QW":"Wessex","QD":"Western","QX":"CVL"}```
```

# Region last updated timestamps
```
{"QC":"2024-07-25 17:29:01","QD":"2024-07-25 17:33:43","QG":"2024-07-25 17:18:16","QK":"2024-07-25 17:13:24","QL":"2024-07-25 17:26:52","QM":"2024-07-25 17:45:02","QR":"2024-07-25 17:20:55","QS":"2024-07-25 17:23:37","QT":"2024-07-25 17:03:47","QU":"2015-06-01 09:05:03","QV":"2020-02-06 20:48:34","QW":"2024-07-25 17:31:19","QX":"2024-07-25 17:05:45"}
```

# Access points in a region (data/XX/core_data.csv)
**Columns:**
``` 
ACCESS_ID = 0;
ACCESS_ELR = 1;
ACCESS_START_MILEAGE = 2;
ACCESS_END_MILEAGE = 5;
ACCESS_ITEM_CODE = 8;
ACCESS_EASTING = 10;
ACCESS_NORTHING = 11;
ACCESS_LOCAL_NAME = 12;
```
**Data:**
```
20155779,CFP,3.044,QT,1252,4.0682,,,HEO,,,,,HTJ8,,FALSE,,,,,0,,,0,20155779,08-Sep-08,ST01_KTOFT,,8888,,N,
20171105,EMP,22.0088,QT,,22.0088,,,HBE,,,,"Peterborough Crescent Workshops: Fly Ash Facs: Ele",HTJ8,,FALSE,,,,,0,,,0,20171105,08-Sep-08,ST01_KTOFT,,8888,,N,
20171106,EMP,22.0088,QT,,22.0088,,,HBE,,,,"Peterborough Crescent Workshops: Fly Ash Facs: Ele",HTJ8,,FALSE,,,,,0,,,0,20171106,08-Sep-08,ST01_KTOFT,,8888,,N,
...
```

# Engineer Line References in a region (data/XX/elr_lookup.csv)
**Columns:**
```
ELR_ID = 1;
ELR_SYSID = 2;
ELR_STARTMILES = 3;
ELR_ENDMILES = 4;
ELR_DESCRIPTION = 5;
ELR_SUBZONE = 6;
ELR_INCLUDE = 9;
ELR_SMA = 10;
ELR_ELECTRIFICATION = 11;
```

**Data:**
```
QT,ACW,11,0.0246,0.0772,"ACTON CANAL WHARF TO WILLESDEN",,1,0,FALSE,,
QT,ATG,12,9.1155,9.1686,"TURNHAM GREEN <LTE BOUNDARY> - GUNNERSBURY JN <SR>",,1,0,FALSE,,
QT,AWL,13,0.0858,0.1073,"ACTON EAST - ACTON WELLS JN (ACTON WELLS LINE) (FORMERLY AWB)",,1,0,FALSE,,
...
```

# Free text (data/XX/freetext.csv)
No idea how it is supposed to be used

```
"Various service equipment located at Fenchurch Place, Station entrance by retail outlets. A switch room within the Superdrug premises which houses a telephone enhancer, a distribution switch board and electricity meter for ""FENNS"", the sandwich bar adjace",110148664
"Within the leased premises, offices, storerooms etc, there is a suspended ceiling with a void above containing various services. These can be accessed from the hatch in the Telecoms Switch room. This area has low headroom. Consideration must be given to a",110148666
"Air Conditioning Units located to the side of the marked walkway and behind handrails. These serve retail unit.The ventilation duct from below ground level at the end of the walkway would indicate basement services. The access for these are unknown but if",110148652
"All Tracks: Under Bridge N. 128: Owner Brentwood Gas Company.Wayleave Ref Unknown:RTP 297, 298, 299, 300",30112434
...
```

# Subzone codes (data/XX/subzone_code.csv)
Again, no idea.

curl http://mobile.nationalhazards.co.uk/regions/QT/subzone_code?token=af0e9da61f9511ed861d

```
QT,HTJ6,1,"Romford MDU"
QT,HTJ7,2,"Ipswich MDU"
QT,HTJ8,3,"Tottenham MDU"
...
```

# Subzone lookup (data/XX/subzone_lookup.csv)
No idea.

```
QT,ACW,0.0246,4,0.0772,"ACTON CANAL WHARF TO WILLESDEN",HTJ8,TRUE,
QT,ATG,9.1155,5,9.1686,"TURNHAM GREEN <LTE BOUNDARY> - GUNNERSBURY JN <SR>",HTJ8,TRUE,
QT,AWL,0.0858,6,0.1073,"ACTON EAST - ACTON WELLS JN (ACTON WELLS LINE) (FORMERLY AWB)",HTJ8,TRUE,
...
```
