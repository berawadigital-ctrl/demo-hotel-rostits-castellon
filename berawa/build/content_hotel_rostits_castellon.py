# Contenido de la demo Hotel Rostits (Castellón de la Plana) (es/en/fr/de). Hechos de hotelrostits.com leidos el 30/10/2026 (ver berawa/sources.json). Lo no publicado no se afirma; sin precios de habitacion ni valoraciones.
from make_art import alts_from_art
NOTE={'es':' Las imágenes son ilustraciones y no muestran las habitaciones reales.','en':' Images are illustrations and do not show the actual rooms.','fr':' Les images sont des illustrations et ne montrent pas les chambres réelles.','de':' Die Bilder sind Illustrationen und zeigen nicht die tatsächlichen Zimmer.'}
H={'es':['Dobles e individual','Triple, cuádruple y familiar'],'en':['Doubles and single use','Triple, quadruple and family'],'fr':['Doubles et usage individuel','Triple, quadruple et familiale'],'de':['Doppelzimmer und Einzelnutzung','Dreibett-, Vierbett- und Familienzimmer']}
RD={
'es':['Doble con cama de matrimonio (admite cama supletoria), doble con dos camas individuales o doble de uso individual. Aire acondicionado, escritorio, nevera pequeña con agua de bienvenida, TV y baño privado con bañera o ducha.','Triple con tres camas, cuádruple con cuatro camas individuales (admite cama supletoria) y familiar con una cama de matrimonio y dos individuales. Amplias y luminosas, con aire acondicionado, TV y baño privado.'],
'en':['Double with a double bed (extra bed available), double with two single beds, or double for single use. Air conditioning, desk, small fridge with welcome water, TV and private bathroom with bath or shower.','Triple with three beds, quadruple with four single beds (extra bed available) and family room with a double bed and two singles. Spacious and bright, with air conditioning, TV and private bathroom.'],
'fr':["Double avec lit double (lit d'appoint possible), double avec deux lits simples ou double en usage individuel. Climatisation, bureau, petit réfrigérateur avec eau de bienvenue, télévision et salle de bains privée avec baignoire ou douche.","Triple à trois lits, quadruple à quatre lits simples (lit d'appoint possible) et familiale avec un lit double et deux lits simples. Spacieuses et lumineuses, avec climatisation, télévision et salle de bains privée."],
'de':['Doppelzimmer mit Doppelbett (Zustellbett möglich), Doppelzimmer mit zwei Einzelbetten oder Doppelzimmer zur Einzelnutzung. Klimaanlage, Schreibtisch, kleiner Kühlschrank mit Begrüßungswasser, Fernseher und eigenes Bad mit Badewanne oder Dusche.','Dreibettzimmer, Vierbettzimmer mit vier Einzelbetten (Zustellbett möglich) und Familienzimmer mit Doppelbett und zwei Einzelbetten. Geräumig und hell, mit Klimaanlage, Fernseher und eigenem Bad.']}
ART={
'hero':('waves',9301,['#e6eef2','#f4f1ea','#1f5f7a','#163f52','#0d2633']),
'intro':('arches',9302,['#eef0ea','#e9b97e','#1f5f7a','#163f52','#0d2633']),
'r1':('skyline',9311,['#163f52','#e8a96a','#f5d7a8','#2e6b5e','#245548','#163a31']),
'r2':('hills',9312,['#e8eff0','#f1e7d0','#e7b874','#8fb3b0','#5e8f8c','#3e6966']),
'g1':('waves',9321,['#1f5f7a','#efc18a','#f7e0b8','#2f7a90','#1f5f7a','#123a4a']),
'g2':('columns',9322,['#edeae2','#f7f4ee','#b2532f','#163f52','#0d2633']),
'g3':('arches',9323,['#ecdfca','#ddac76','#b2532f','#163f52','#0d2633']),
'g4':('skyline',9324,['#163f52','#e2a466','#f3d19e','#2c6a5c','#22574a','#143a30'])}
IMGS=dict(hero='hero',intro='intro',rooms=['r1','r2'],gallery=['g1','g2','g3','g4'])
ALTS=alts_from_art(ART)
T={
'es':dict(title='Hotel Rostits · Hotel familiar en Castellón de la Plana',see_rooms='Ver las habitaciones',hero_k='Castellón de la Plana',hero_t='Tu hotel en Castellón: cómodo, tranquilo y bien ubicado',hero_s='Hotel familiar con 28 habitaciones amplias y luminosas, a 15 minutos a pie del centro histórico.',
 intro_t='Para trabajo, deporte o turismo',intro_p1='Muy cerca de la estación de tren y autobuses, con conexión por la CV-10 y la AP-7 y buena comunicación con Alcora, Onda y Vila-real.',
 intro_p2='Recepción presencial de 7 a 23 h y entrada con código las 24 h. Restaurante adjunto al hotel para desayunos, comidas y cenas.',
 stats=['28 habitaciones','Recepción 7–23 h','WiFi gratis','Se admiten mascotas'],nav_rooms='Habitaciones',rooms_t='Nuestras habitaciones',rooms_s='De la doble de uso individual a la familiar, todas con aire acondicionado y calefacción.',
 svcs=['WiFi gratuito en todo el hotel','Parking con reserva previa','Habitación adaptada','Limpieza diaria','Guardaequipaje','Lavandería'],
 around_s='Cerca: pistas de atletismo Gaetà Huguet, Polideportivo Ciutat de Castelló, Piscina Olímpica Municipal, La Salera, Estepark y El Corte Inglés.',
 loc_p="Av. de l'Alcora, 73 · 12006 Castelló de la Plana, a 15 minutos a pie del centro histórico.",
 chips=['¿Qué habitaciones tenéis?','¿Hay parking?','¿Puedo ir con mi perro?','¿Puedo cancelar?']),
'en':dict(title='Hotel Rostits · Family-run hotel in Castellón de la Plana',see_rooms='See the rooms',hero_k='Castellón de la Plana',hero_t='Your hotel in Castellón: comfortable, quiet and well located',hero_s='A family-run hotel with 28 spacious, bright rooms, a 15-minute walk from the historic centre.',
 intro_t='For business, sport or leisure',intro_p1='Very close to the train and coach stations, with CV-10 and AP-7 road links and good connections to Alcora, Onda and Vila-real.',
 intro_p2='Staffed reception from 7 to 23 h and code-based entry 24 hours. A restaurant attached to the hotel serves breakfast, lunch and dinner.',
 stats=['28 rooms','Reception 7–23 h','Free WiFi','Pets allowed'],nav_rooms='Rooms',rooms_t='Our rooms',rooms_s='From the double for single use to the family room, all with air conditioning and heating.',
 svcs=['Free WiFi throughout','Parking, booking required','Accessible room','Daily cleaning','Luggage storage','Laundry'],
 around_s='Nearby: Gaetà Huguet athletics tracks, Ciutat de Castelló sports centre, Municipal Olympic Pool, La Salera, Estepark and El Corte Inglés.',
 loc_p="Av. de l'Alcora, 73 · 12006 Castelló de la Plana, a 15-minute walk from the historic centre.",
 chips=['Which rooms do you have?','Is there parking?','Can I bring my dog?','Can I cancel?']),
'fr':dict(title='Hotel Rostits · Hôtel familial à Castellón de la Plana',see_rooms='Voir les chambres',hero_k='Castellón de la Plana',hero_t='Votre hôtel à Castellón : confortable, calme et bien situé',hero_s='Hôtel familial de 28 chambres spacieuses et lumineuses, à 15 minutes à pied du centre historique.',
 intro_t="Pour le travail, le sport ou le tourisme",intro_p1='Tout près des gares ferroviaire et routière, relié par la CV-10 et l\'AP-7, et bien desservi vers Alcora, Onda et Vila-real.',
 intro_p2='Réception sur place de 7 h à 23 h et accès par code 24 h/24. Restaurant attenant à l\'hôtel pour le petit-déjeuner, le déjeuner et le dîner.',
 stats=['28 chambres','Réception 7 h–23 h','WiFi gratuit','Animaux acceptés'],nav_rooms='Chambres',rooms_t='Nos chambres',rooms_s='De la double en usage individuel à la familiale, toutes avec climatisation et chauffage.',
 svcs=["WiFi gratuit dans tout l'hôtel",'Parking sur réservation','Chambre adaptée','Ménage quotidien','Bagagerie','Blanchisserie'],
 around_s="À proximité : pistes d'athlétisme Gaetà Huguet, complexe sportif Ciutat de Castelló, piscine olympique municipale, La Salera, Estepark et El Corte Inglés.",
 loc_p="Av. de l'Alcora, 73 · 12006 Castelló de la Plana, à 15 minutes à pied du centre historique.",
 chips=['Quelles chambres avez-vous ?','Y a-t-il un parking ?','Puis-je venir avec mon chien ?','Puis-je annuler ?']),
'de':dict(title='Hotel Rostits · Familienhotel in Castellón de la Plana',see_rooms='Zimmer ansehen',hero_k='Castellón de la Plana',hero_t='Ihr Hotel in Castellón: bequem, ruhig und gut gelegen',hero_s='Familiengeführtes Hotel mit 28 geräumigen, hellen Zimmern, 15 Gehminuten von der Altstadt.',
 intro_t='Für Beruf, Sport oder Urlaub',intro_p1='Ganz in der Nähe von Bahnhof und Busbahnhof, mit Anbindung an CV-10 und AP-7 und guter Verbindung nach Alcora, Onda und Vila-real.',
 intro_p2='Besetzte Rezeption von 7 bis 23 Uhr und Zugang per Code rund um die Uhr. Ein Restaurant direkt am Hotel bietet Frühstück, Mittag- und Abendessen.',
 stats=['28 Zimmer','Rezeption 7–23 Uhr','Kostenloses WLAN','Haustiere erlaubt'],nav_rooms='Zimmer',rooms_t='Unsere Zimmer',rooms_s='Vom Doppelzimmer zur Einzelnutzung bis zum Familienzimmer, alle mit Klimaanlage und Heizung.',
 svcs=['Kostenloses WLAN im ganzen Haus','Parkplatz mit Reservierung','Barrierefreies Zimmer','Tägliche Reinigung','Gepäckaufbewahrung','Wäscheservice'],
 around_s='In der Nähe: Leichtathletikanlage Gaetà Huguet, Sportzentrum Ciutat de Castelló, städtisches Olympiabad, La Salera, Estepark und El Corte Inglés.',
 loc_p="Av. de l'Alcora, 73 · 12006 Castelló de la Plana, 15 Gehminuten von der Altstadt.",
 chips=['Welche Zimmer gibt es?','Gibt es einen Parkplatz?','Darf ich meinen Hund mitbringen?','Kann ich stornieren?'])}
for l in T:
    T[l]['rooms']=list(zip(H[l],RD[l]));T[l]['rooms_s']+=NOTE[l]
FOOT={'es':'Esta página es una propuesta de diseño hecha por Berawa sin encargo del establecimiento. Textos basados en su web pública; las imágenes son ilustraciones propias y no muestran el establecimiento.',
'en':'This page is a design proposal made by Berawa without any commission from the business. Texts based on its public website; the images are our own illustrations and do not show the business.',
'fr':"Cette page est une proposition de design réalisée par Berawa sans commande de l'établissement. Textes basés sur son site public ; les images sont des illustrations propres et ne montrent pas l'établissement.",
'de':'Diese Seite ist ein Designvorschlag von Berawa, ohne Auftrag der Unterkunft erstellt. Die Texte beruhen auf deren öffentlicher Website; die Bilder sind eigene Illustrationen und zeigen die Unterkunft nicht.'}
RB='https://booking.avirato.com/?code=53239085'
BOOK=dict(mode='engine',url={l:RB for l in ('es','en','fr','de')})
D=dict(name='Hotel Rostits',ac='#163f52',ac2='#b2532f',ac2_a11y='#8f3f22',book=BOOK,around=['Centro histórico','La Salera'],foot=FOOT,
 address="Av. de l'Alcora, 73 · 12006 Castelló de la Plana",phones=['+34 964 341 929'],emails=['reservas@hotelrostits.com'],maps="Hotel Rostits, Av. de l'Alcora 73, Castelló de la Plana",t=T)
META=dict(repo='demo-hotel-rostits-castellon',name='Hotel Rostits',legal_name='HSK 57, SL',registry_ids=['NIF B12266839'],
 url='https://hotelrostits.com/',domain='hotelrostits.com',municipality='Castelló de la Plana',province='Castellón',sector='hotel familiar de 28 habitaciones en Castellón de la Plana',
 read_at='2026-10-30T07:03:20+01:00',created_at='2026-10-30T07:02:30+01:00',built_at='2026-10-30T07:15:00+01:00',audit_date='2026-10-30T06:50:00+01:00',
 rating=dict(value=4.2,coincide=['telefono','web'],date='2026-10-29T16:22:47+01:00',url='https://www.google.com/maps/place/Hotel+ROSTITS/@39.9865585,-0.0576764,17z/data=!4m9!3m8!1s0xd5ffe18cd93ad1d:0x9357f01f96bc5e53!5m2!4m1!1i2!8m2!3d39.9865585!4d-0.0576764!16s%2Fg%2F1tdrgq1y'),
 book=dict(mode='engine',url=RB,note='motor de reservas real de su web (Avirato), HTTP 200 comprobado el 30/10/2026; el mismo enlace en es/en/fr/de.'),first_of_type=None)
QS={
'es':[('¿Qué habitaciones tenéis?','K01'),('Somos cinco, ¿tenéis cuádruple con supletoria?','K02'),('¿Hay parking?','K03'),('¿Puedo ir con mi perro?','K04'),('Llego a medianoche, ¿cómo entro?','K05'),('¿Tenéis restaurante para cenar?','K06'),('¿Puedo cancelar?','K07'),('¿Dónde está el hotel?','K08'),('¿Cómo reservo?','K09'),('¿Podéis confirmarme disponibilidad para mañana?','K09'),('¿Cuánto cuesta una noche?',None),('¿Tenéis piscina?',None)],
'en':[('Which rooms do you have?','K01'),('We are five, do you have a quadruple with an extra bed?','K02'),('Is there parking?','K03'),('Can I bring my dog?','K04'),('I arrive at midnight, how do I get in?','K05'),('Do you have a restaurant for dinner?','K06'),('Can I cancel?','K07'),('Where is the hotel?','K08'),('How do I book?','K09'),('Can you confirm availability for tomorrow?','K09'),('How much is a night?',None),('Do you have a swimming pool?',None)],
'fr':[('Quelles chambres avez-vous ?','K01'),("Nous sommes cinq, avez-vous une quadruple avec lit d'appoint ?",'K02'),('Y a-t-il un parking ?','K03'),('Puis-je venir avec mon chien ?','K04'),("J'arrive à minuit, comment entrer ?",'K05'),('Avez-vous un restaurant pour dîner ?','K06'),('Puis-je annuler ?','K07'),("Où se trouve l'hôtel ?",'K08'),('Comment réserver ?','K09'),('Pouvez-vous me confirmer la disponibilité pour demain ?','K09'),('Combien coûte une nuit ?',None),('Avez-vous une piscine ?',None)],
'de':[('Welche Zimmer gibt es?','K01'),('Wir sind fünf, gibt es ein Vierbettzimmer mit Zustellbett?','K02'),('Gibt es einen Parkplatz?','K03'),('Darf ich meinen Hund mitbringen?','K04'),('Ich komme um Mitternacht an, wie komme ich hinein?','K05'),('Haben Sie ein Restaurant zum Abendessen?','K06'),('Kann ich stornieren?','K07'),('Wo liegt das Hotel?','K08'),('Wie kann ich buchen?','K09'),('Können Sie mir die Verfügbarkeit für morgen bestätigen?','K09'),('Was kostet eine Übernachtung?',None),('Haben Sie ein Schwimmbad?',None)]}
