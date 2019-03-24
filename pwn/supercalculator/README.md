# Super Calculator
#### Problemskapare: Herman Karlsson
#### Poäng: 250
#### Antal solves: 24

Super Calculator - Lösning

I uppgiftsbeskrivningen så får vi en ip-address och en port som vi kan ansluta till med netcat.
När vi anslutit så kan vi skriva in något sorts matematiskt uttryck, vilket vi kan testa.
När man får nått sånt här så är det bra att testa malformade strängar, så en sak man 
kan testa är `1/0`, vilket ger ett error:

```
Traceback (most recent call last):
  File "./superCalculator.py", line 42, in <module>
    print(eval(input()))
  File "<string>", line 1, in <module>
ZeroDivisionError: division by zero
```

Från vilket vi kan se att vi har ett pythonprogram som kör `eval` på det vi skriver in,
vilket innebär att vi kan få programmet att köra godtycklig kod.
Här skulle man kunna testa lite saker, man kulle exempelvis kunna gissa att det finns 
en fil med namn "flag.txt" i samma directory som innehåller flaggan, i vilket fall man
kan skriva `open('flag.txt').read()`, vilket skulle räcka i det här fallet.

Det är dock svårt att veta att det är just så, så en lite mer generell strategi är att
försöka få tillgång till ett shell. Detta gör man lämpligast genom anropa funktionen `system`
i pythonmodulen `os`, som kör shellkomandon. Vi kan kolla att `os` är importerad genom att ge 
programmet strängen `os`. Man kan därefter inputta `os.system('sh')`, vilket ger tillgång till 
en shell, som vi kan köra typ `ls`, `cat flag.txt` i för att få flaggan.

Om det skulle vara så att `os` inte var importerad skulle vi kunna komma runt det genom att
skicka strängen `__import__('os').system('sh')`

