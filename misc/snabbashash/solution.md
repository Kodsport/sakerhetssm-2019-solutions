När man anslutit till adressen given i beskrivingen så blir man ombedd att ta fram md5 hashar av
en massa strängar. En rimlig början är att ta den första strängen och generera md5 av den m.h.a.
typ nån hemsida eller nått. När man testar den så märker man dock att man var för långsam. Man
kan försöka vara snabbare, men det kommer inte gå. Man kommer alltså behöva automatisera det här
och skriva ett skript som löser det åt en. Det skriptet ska då ansluta till adressen, extrahera
strängarna som ska hashas, hasha strängarna, och sedan skicka tillbaka hasharna till servern. 
Se filen `solve.py` för ett exempel på ett sånt skript.
