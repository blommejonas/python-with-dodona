## Voordelen van Python
Python wordt door velen gezien als een taal die bij uitstek geschikt is om mensen te leren programmeren. Het is een krachtige taal, die gemakkelijk te gebruiken is, en die alle mogelijkheden biedt die andere talen ook bieden. Je kunt Python programma’s draaien op verschillende machines en verschillende besturingssystemen. Het is gratis verkrijgbaar. Voor beginnende programmeurs heeft het het voordeel dat het dwingt om nette code te schrijven. Python wordt ook in de praktijk veel gebruikt, soms als basis voor complete programma’s, soms als uitbreiding op programma’s die in een andere taal geschreven zijn.

Het belangrijkste voordeel is dat Python het mogelijk maakt om je te concentreren op “denken als een programmeur,” in plaats van op alle excentrieke afwijkingen die een specifieke taal heeft. Hier volgt een voorbeeld van het verschil tussen Python en een aantal andere populaire programmeertalen.

Het eerste programma dat iedereen schrijft in een computertaal is <code>Hello World</code>. Dit is een programma dat de tekst <code>“Hello, world!”</code> op het scherm zet. In de zeer populaire taal C++, wordt <code>Hello World</code> als volgt gecodeerd:

<pre><code>
#include <iostream>
int main() {
    std::cout << "Hello, world!";
}
</code></pre>

In C#, de populaire variant van C++ die uitgebracht is door Microsoft, is het:

<pre><code>
using System;
namespace HelloWorld {
    class Hello {
        static void Main() {
            Console.WriteLine( "Hello, world!" );
            Console.ReadKey();
        }
    }
}
</code></pre>

In Objective-C, Apple’s variant op C++, is het nog erger:

<pre><code>
#import <Foundation/Foundation.h>
int main ( int argc, const char * argv[] ) {
    NSAutoreleasePool *pool = [[NSAutoreleasePool alloc] init];
    NSLog (@"Hello, world!");
    [pool drain];
    return 0;
}
</code></pre>

In Java, dat voor veel studenten aan universiteiten en hogescholen de eerst-geleerde programmeertaal is, wordt het:

<pre><code>
class Hello {
    public static void main( String[] args ) {
        System.out.println( "Hello, world!" );
    }
}
</code></pre>

En zie nu wat Hello World in Python is:

<pre><code>
print( "Hello, world!" )
</code></pre>

Ik neem aan dat we het met elkaar eens zijn dat de Python versie van dit programma leesbaarder en begrijpelijker is dan de andere varianten – zelfs als je de taal niet kent.

## Python’s beperkingen als programmeertaal
Python is een universele programmeertaal. Dat betekent dat je het kunt gebruiken voor alles wat je maar met een programmeertaal zou willen of kunnen doen. Mag je dan concluderen dat als je eenmaal Python beheerst, je nooit meer een andere taal hoeft te leren?

Het antwoord is dat dat afhangt van wat je wilt bereiken. Python kun je inderdaad voor alles gebruiken, maar het is niet voor alles het meest geschikt. Bijvoorbeeld, game ontwikkelaars gebruiken meestal C++ of C#, omdat die talen heel snelle programma’s opleveren, en snelheid is van groot belang voor games. Mensen die complexe statistische berekeningen moeten doen hebben ook hun eigen talen. Soms moet je programma’s schrijven die moeten samenwerken met andere programma’s die in een specifieke taal geschreven zijn, en moet je ook die taal gebruiken. En voor sommige programmeertaken zijn talen met een andere filosofie tot het schrijven van code het meest geschikt.

Samenvattend heeft Python op zich geen beperkingen, maar zijn voor specifieke problemen specifieke andere talen geschikter. Dat gezegd hebbende, voor de meeste mensen is kennis van Python voldoende om alles te doen wat nodig is voor hun studie of beroep. Daarbij komt dat als je eenmaal Python beheerst, je een sterke basis hebt om andere talen te leren. Daarom denk ik dat Python uitermate geschikt is om beginnelingen te leren programmeren.
