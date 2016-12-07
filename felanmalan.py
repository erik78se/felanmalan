# -*- coding: utf-8 -*-
#
# Run with: python3 felanmalan.py
# This is the damn site: http://www.strangnas.se/sv/Trafik--infrastruktur/felanmalan/

import requests

headers = {'Content-Typei' : 'application/x-www-form-urlencoded'}
data = {'ctl00$MainRegion$FullContentRegion$ContentRegion$XForm1$FormControl$Namn': 'En medborgare',
        'ctl00$MainRegion$FullContentRegion$ContentRegion$XForm1$FormControl$Adress' : 'Åkers styckebruk',
        'ctl00$MainRegion$FullContentRegion$ContentRegion$XForm1$FormControl$Beskrivning' : 'Belysningen pa Lundbyvägen, fotbollsplanens stora lampa har varit trasig i säkert 10 år. Det ar kålsvart och barnen ser inget. Kan ni fixa den och se till att barnen kan se något när de försöker åka pulka i backen bakom?',
        'ctl00$MainRegion$FullContentRegion$ContentRegion$XForm1$FormControl$Adress_omrade' : 'Lundbyvägen, Åkers styckebruk',
        'ctl00$MainRegion$FullContentRegion$ContentRegion$XForm1$FormControl$Vad_galler_anmalan': 'Parker och grönytor' 
}

r = requests.post('http://www.strangnas.se/sv/Trafik--infrastruktur/felanmalan/', data=data, headers=headers)

print(r.text)
