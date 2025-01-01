# The script of the game goes in this file.

# Declare characters used by this game. The color argument colorizes the
# name of the character.
# The game starts here.
define c = Character("Cariye")
define e = Character("Emir Timur")
define me= Character("Sen")
define k= Character("Koruma")

label start:

    play music harp2 fadein 1.0 fadeout 4.0

    # Show a background. This uses a placeholder by default, but you can
    # add a file (named either "bg room.png" or "bg room.jpg") to the
    # images directory to show it.

    scene room

    # This shows a character sprite. A placeholder is used, but you can
    # replace it by adding a file named "eileen happy.png" to the images
    # directory.
    "Güzel çini işlemeli bir odada, muazzam bir baş ağrısı ile gözlerimi araladım"
    me "Agh, başım çok ağrıyor."
    me "Burası da neresi ?"
    show tmr
    with dissolve
    # These display lines of dialogue.

    e "Merhaba yabancı..."
    "Gördüğüm adam, pahalı ipek elbiseler ile sarılmış, başında altın tacının parıltısı ile göz kamaştırıyor"
    "Buraya nasıl geldiğimi bile hatırlamazken karşımda böyle birini görmenin verdiği heyecan ile ister istemez nabzım yükseldi"
    "Elimden geldiğince sakinleşmeye çalıştım. Karşımdaki adam önemli birine benziyor..."
    me "Merhaba siz de kimsiniz ?"
    e "Asıl bunu soran ben olmalıydım, burası benim hanem..."
    me "Üzgünüm hiçbir şey hatırlamıyorum."
    me "Buraya nasıl geldim ?"
    e "Askerlerim seni kapının önünde baygın bir halde buldu."
    me "Verdiğim rahatsızlık sebebiyle çok özür dilerim."
    e "Sorun değil uzun zamandır ziyaretçim olmuyor zaten..."
    me "Peki siz kimsiniz?"
    e """Ben, Timur İmparatorluğu'nun kurucusu ve ilk hükümdarı Emir Timur,
    sarayıma hoşgeldin..."""
    e "Çağatay Boyu ulusunu oluşturan kabilelerden Barlaslar'ın reisi olan Turagay ile Tekina Hatun'un çocuğu Timur'um"
    e "Semerkant yakınlarındaki Şehr-i-Sebz'e bağlı Hoca Ilgar köyünde dünyaya geldim"
    "Timur İmparatorluğu mu ? Sanki bir yerden kulağımı ısırıyor ama yine de hatırlayamadım. Yine de karşımdaki bir hükümdar.Hareketlerime dikkat etmeliyim."
    me "Hmm... Anlıyorum..."

    label devam:
        e "Evet bu kadar çene çalmak yeter. İstersen kendine gelene kadar biraz daha burada ikamet edebilirsin. Şimdiklik bir işim var görüşmek üzere"
        scene koridor
        "2 Tane muhafız koridor boyunca, bana ayrılan odaya kadar eşlik ettiler."
        "Saray tahmin ettiğimden biraz daha büyüktü..."
        "Bir süre yürüdükten sonra odaya vardık"
        scene oda
        with fade
        "Oda gayet sessiz ve huzurlu, dinlenmek isteyen birisi için çok ideal bir yer..."
        stop music fadeout 7.0
        me "Kendimi toparlayıp olan şeyleri hatırlamalıyım..."
        play music harp fadeout 1.0 fadein 1.0
        "Bu düşünceyi zihnimde sayıklayarak uykuya daldım."
        scene rüya
        with fade
        "Gözlerimin önüne gelen görüntü cennetten gelme gibiydi..."
        "Büyülenmiş gibi manzarayı izliyorken, her bir detayına - çiçeklerin renklerine, renklerin doyumuna, görüntünün huzuruna- kendimi kaptırdım."
        "Bu sırada istemeden değerli manzaradan koparıldım, sebepsizce uyanmıştım..."
        scene oda
        with fade
        "Yeniden uykuma dönmeye çalıştım..."
        scene rüya2
        with fade
        "Bu sefer bulutların üstünde bir dağın tepesinde gibiydim, ayaklarımın altındaki taşların arasından akan lavları görebiliyordum."
        "Karşımda dağın en tepesinde zerafetini bulutlarla birleştirmiş bir kiraz ağacı çiçek açıyordu."
        "Lavların arasında zorlukla yaşamış ama güzelliğinden ödün vermemiş yalnız bir şekilde çiçeklerini rüzgara savuruyordu..."
        "...Sanki..."
        "Yalnız güçlü bir hükümdar gibi..."
        scene oda
        with fade
        "Kesilip duran uykumdan bir kez daha uyandım ve bu sefer geri yatmamaya karar verdim."
        stop music fadeout 5.0
        me "Biraz dolaşsam iyi olacak sanırım."
        play music harp2 fadein 1.0
        scene koridor
        with fade
        "Bana tahsis edilen rahat ve huzurlu odadan dışarı çıktım ve koridorda biraz dolanmaya başladım."
        me"Emir Timur beni, kim olduğunu bile bilmediği bir adamı neden yanına aldı."
        me"Acaba gücün getirdiği yalnızlığı bir nebze olsun azaltmek için mi ?"
        me"...veya sadece iyilik yapmak istemiştir..."
        me"ve ben hala buraya nasıl geldiğimi hatırlayamıyorum..."
        show kapı
        with dissolve
        "Burası neresi ki ? İçeriden Timur'un sesi geliyor"
        e "Evet fil ve deve arasında bir seçim yapmalıyım,"
        e "Hayır, veziri oraya koymak olmaz..."
        "Tam ne hakkında konuştuğunu merak etmeye başlamıştım ki bir nöbetçi ile gözlerimiz kesişti, içten içe bana buradan gitmemi söylüyor gibiydi..."
        show korumayakın
        with dissolve
        k "Efendim, sabahın bu saatlerinde burada olmanızın hükümdarımızın hoşuna gideceğini sanmam lütfen odanıza dönünüz!"
        me "Üzgünüm uyku tutmadıydı ama..."
        show korumayakın
        with dissolve
        "Bakışları uykumun umrunda olmadığını, sadece gitmemi söylediğini anlatır gibiydi..."
        menu:
            "Tabi dönüyorum odama, iyi nöbetler dilerim.":
                jump devam2
            "Emir Timur Hazretleri ne hakkında konuşuyor acep ?":
                jump alaka

    label alaka:

        k "Bunu bilmemekle beraber sizin de bilmeniz gerektiğini düşünmüyorum..."
        k "Lütfen artık odanıza dönün."
        jump devam2

    label devam2:

        scene palace
        with fade
        "Odama dönmek üzere koridora yöneldim,"
        "Timur'un bahsettiği şeyler -vezir,deve,fil-..."
        "...neyden bahsediyordu ki ? "
        show cariye
        with dissolve
        c "Hmm..."
        "Yüzünü tülle kapatmış bu kadın şüpheci bir bakışla beni süzüyordu,"
        "Sarayın cariyesi falan mı ki..."
        c "Bu saatte burada ne arıyorsunuz ? "
        menu:

            "Sizi ilgilendirmez. Kendi işine bak !":
                jump sel
            "Uykumdan uyandım da biraz dolaşmanın iyi gelebileceğini düşündüm...":
                jump es

    label sel:

        c "Sultanımızın misafiri olmanız size kaba konuşma hakkı tanımıyor..."
        c "Görüşmek üzere, hidayet bulasınız !"
        hide cariye
        with dissolve
        jump yalın

    label es:

        c "Hmm...  Anladım size odanıza kadar eşlik etmemi ister misiniz ? "
        menu:

            "Olur":
                jump eslik

            "Gerek yok kendim dönerim...":
                jump yalın

    label eslik:

        c "Efendimiz sizi baygın halde kapıda bulduğunu belirtmişti, geçmiş olsun."
        me "Çok teşekkür ederim... "
        c "Peki kimsiniz, necisiniz, nereden gelirsiniz ?"
        me "Ne yalan söylesem ben de bu soruların cevabını bilmek isterdim lakin zihnim bulanık geçmişe dair pek bir şey hatırlamıyorum maalesef."
        "Tül nedeniyle çok belirgin olmayan yüzünden bana karşı acıyan bir bakış sezdim"
        me "Peki siz kimsiniz acaba ?"
        c "Öylesine bir saray cariyesiyim efendime hizmet eder dileklerini gerçekleştiririm."
        me "Anladım, size bir soru sorabilir miyim ?"
        c "Tabi, cevaplayabileceğim bir soruysa yardımcı olmak isterim..."
        me "Koridordan geçerken yanlışlıkla Timur-Han'ın odasından gelen bir kaç nağaraya kulak misafiri oldum"
        me "Vezir, fil, deve gibi şeyler söylüyordu."
        me "Ne oldukları hakkında bir fikriniz var mı ?"
        hide cariye
        show c_düşünce
        with dissolve
        c "O sesler mi ? Onları duymamanız gerekirdi..."
        me "Ne?! Nasıl Yani?!"
        "Yüzündeki ciddi ifade bir anlık kalbimin sıkışmasına yetecek kadar korkuttu beni..."
        hide c_düşünce
        show c_mutlu
        with dissolve
        "Sonrasında tülün altında şeydani bir gülümseme gördüm."
        "Ardından ise hafif bir kıkırtı...."
        c "Pfhahaha!"
        me "?"
        c "Kaba davranışımı bağışlayın."
        c "Yüz ifadeniz çok gülünesi bir hal aldı kendimi tutamadım..."
        c "Tehlikede falan değilsiniz. O sesler muhtemelen efendimizin satranç oynarken düşündüğü şeylerdi"
        "İnsanı ölümle tehdit edip üstüne bununla dalga geçmek pek hoş bir davranış değil lakin ölmeyeceğimi bilmek içimi rahatlattı"
        me " Benimle tekrardan mı dalga geçiyorsunuz acep? Satranç ile devenin ne alakası var?"
        c "Odanıza geldik. Bunu size açıklamak biraz zaman alır, şimdilik bu yaşanmamış gibi davranın. Tekrar karşılaştığımızda ne demek istediğimi anlayacaksınız."
        c "İyi günler dilerim !"
        hide c_mutlu
        with dissolve
        stop music fadeout 4.0
        "Son kez bunları söyleyip yanımdan ayrılan cariyenin arkasından bakakaldım..."
        "Bir süre sonra, merak etmenin bir şeye yaramayacağına kendimi inandırıp odama girdim"
        jump oda
    label yalın:
        "Odamın yolunu tuttum"
        "Aklımdaki sorulara yenileri eklenmişti..."
        "Timur neyden bahsediyordu ve o kadın kimdi ?"
        me " Bunları düşünmek zihnimi meşgul etmekten başka bir işe yaramayacak..."
        "Odamın önüne geldim"
        stop music fadeout 4.0
        me "İçeri girsem iyi olur sanırım... "
        jump oda

    label oda:
        scene oda
        with fade
        "Odaya girdiğimde, yatmadan önce farketmediğim bir şey farkettim.."
        "Kapının hemen yanında içinde bazı kitapların bulunduğu bir kitaplık vardı..."
        play music harps fadein 7.0
        scene kitaplık
        with dissolve
        "Hepsi birbirine benziyordu."
        "İçinden gözüme çarpan eski, uzun bir kitabı aldım ve masaya oturdum. "
        scene kitap
        with fade
        "İçinde satranç hakkında bilgiler, satrancın doğumu, mucidi, doğarken nelerin yaşandığına dair bir öykü gibi konular vardı... "
        "İlk sayfalar sıkıcı gelse de ilerleyen sayfalarda kitaptan zevk almaya başladım."
        "Hatta bir kısmında satrancın öyküsü kısa bir şekilde anlatılmıştı ve dikkatimi en çok çeken kısım orası olmuştu..."
        "(Anlatılana göre...)"
        """Hindistan'da hüküm süren çok zalim, savaştan zevk alan bir kral varmış. Hükümdarın savaş sevgisi ülkedeki insanlara zorluklar yaştıyormuş."""
        """Günün birinde bir alim gelip kralın huzuruna çıkmış ve ona demiş ki..."""
        """...\"Kralım siz savaşmayı çok seviyorsunuz o yüzden ben de size dilediğiniz gibi savaşabileceğiniz bir oyun getirdim,
        şu ufak taşlar sizin piyonlarınız askerleriniz,"""
        show abo at left
        with dissolve
        "...iki tane atlı, iki tane de filli birliğiniz var. 2 tane de kaleniz , siz tabiki de şahsınız yanınızdaki de yardımcınız veziriniz, artık dilediğiniz gibi savaşabilirsiniz\"."
        show kale at right
        with dissolve
        "Kral başta ismi \"{b}Çaturanga{/b}\" olan bu oyunu çok beğenmiş ve alime dile benden ne dilersen demiş... "
        "Alim ise zalim krala karşılık olarak ilk karede 1 tane arpa olmak üzere her karede bir öncekinin iki katı miktarda arpa istediğini belirtmiş."
        "Kral ise hiç düşünmeden isteğinin yerine getirilmesini emretmiş, lakin hesaplamaya başlanıldığında 25.karede 1.5 ton , 31.karede ise 92 ton arpa ettiği görülmüş..."
        scene satranç
        with fade
        "Kitap öyküyü burada sonlandırdı lakin oyunun doğma öyküsünün böyle olması beni hayretler içinde bıratkı."
        stop music fadeout 3.0
        "Ve en son ne zaman satranç oynadığımı hatırlamaya çalıştım..."
        play sound knock
        "Bir anda kapı tıklatma sesi ile irkildim..."
        scene kitap
        with dissolve
        #buraya kapı tıklatma sesi koyacağız
        me "Buyurun !"
        k "Efendim, öğlen yemeği vakti gelmiş bulunmakta. Emir Timur Hazretleri kendisine eşlik etmenizi rica ediyor."
        play music harp3 fadein 4.0 fadeout 4.0
        me "Tabi hemen geliyorum..."
        "Yavaşça kapıya yöneldim ve yemek salonuna doğru yola koyuldum..."
        scene ymeek
        with fade
        "Salon, cidden asil birine olduğunu belli ediyordu duvarda asılı mızrak ve kılıçlarda, masa ve dizilimlerde açıklayamadığım bir Avrupa esintisi mevcuttu."
        show tmr
        with dissolve
        e "Hoşgeldin,  buyur karşıma otur..."
        me "Teşekkürler..."
        e "Kendini daha iyi hissediyor musun ?"
        me "Sayenizde efendim bu gün daha iyiyim."
        e "Adına sevindim."
        "Fazla konuşmadan onun yemeğina başlamasını bekledim, kişiliğimi pek hatırlayamasam da edep ve adabım..."
        "...ev sahibi başlayana kadar yemeğe başlanılmayacağını zihnime fısıldıyordu."
        "Timur'un çatala davranmasıyla yemeğe başlamış olduk..."
        "Acaba ne hakkında konuşalım diye düşünürken karşımda zarif bir şekilde etini yiyen hükümdar ile gözgöze geldik..."
        e "Bir sorun mu var ?"
        me "Yok efendim sadece..."
        e "?"
        "Neden böyle bir şey dedim ki ?"
        "Bir şeyler söylemezsem ayıp olacak sanırım..."
        me "Yemek çok lezzetli..."
        "Cidden mi ?"
        "Koskoca Timur İmparatorluğu'nun sahibine yemeğin çok lezzetli olduğunu mu söyledim..."
        e "(Gülümser)"
        e "Aşçılarım bu diyarın en iyileridir. Afiyet olsun..."
        me "Teşekkürler"
        "Bir kaç dakika konuşmadan yemeğimizi yedik..."
        e "Satrancı sever misin ?"
        "Bu soru da nereden çıktı ki ?"
        me "Ben,en son ne zaman oynadığımı pek hatırlamıyorum lakin kuralları bilirim..."
        e "Hmm..."
        e "Yemekten sonra bana esşlik eder misin sana bir şey göstereceğim ?"
        me "Tabi efendim..."
        hide tmr
        with dissolve
        "Bu diyalog sonrasında bir şey fark ettim."
        "Bu gün {b}satranç{/b} kelimesini çok işitiyorum..."
        "Acaba sabah duyduğum develi satrançla bir alakası mı var ?"
        "Yemeğimizi bitirene kadar ki düşüncem bu yöndeydi..."
        show tmr
        with dissolve
        e "Eğer yemeğin bittiyse kalkabiliriz..."
        menu:
            "Bitti efendim, yemek için teşekkürler.":
                jump gidelim
            "Son birkaç şey daha yemek istiyorum.":
                jump obur
    label obur:
        "Uzun zamandır yemediğim kadar güzel bir yemek yerken Timur'un bakışlarıyla karşılaştığımı sezdim, bayağıdır yiyorduk..."
        "Her ne kadar istemesemde yemek faslının bittiğini belirttim..."
        jump gidelim
    label gidelim:
        e "Haydi gidelim..."
        scene g_koridor
        with fade
        "Odadan çıktık ve sabah önünden geçtiğim odaya doğru yola koyulduk..."
        "Giderken tastan yapılmış kolonların arasından geçtik."
        "Geçtiğimiz koridor kapalı taştan mekanın serinliğini hissettiriyordu..."
        scene kapı
        with fade
        "Evet, sabah önünde durduğum kapıdan şimdi Emir Timur Hazretleri ile birlikte geçiyorum."
        scene sarayoda
        with fade
        "Odaya girdik ve altın rengi temanın gözlerimi kamaştırmasına izin verdim..."
        e "Evet odama hoşgeldin..."
        e "Burayı genellikle kişisel hobilerim için kullanıyorum."
        me "Ne gibi hobiler ?"
        e "Satranç, Mangala, Go gibi oyunları çok severim."
        "Evet satrancı duymayı bekliyordum zaten"
        "Emin olamadığım için tekrar sormaya karar verdim."
        me " Bildiğimiz satranç mı ?"
        "Öncelikle tepkimin neden böyle olduğunu anlamaya çalışır gibi bir yüz ifadesi takındı..."
        e "Nasıl bir satranç bekliyordun ki ?"
        me "Bu sabah vezir deve fil gibi şeyler söylediğiniz duydum buradan geçerken..."
        me "...İlk başta normal satranç olduğunu düşünmüştüm lakin deveyi duyduğumda biraz garipsedim. Bildiğim kadarıyla satrançta \n deve isimli bir taş bulunmamakta. "
        e "Hmm... Haklısın iyi bir yere değindin."
        me "?"
        e "Normal satrancı aslında çok severim ve uzun zamandır oynuyordum."
        e "Lakin artık bir şeyler eklemek, duyulmamış görülmemiş şeyler yönetmek istediğimin farkına vardım."
        e "Ve kendi satranç oyunumu {b}\"Timur Satrancını\"{/b} tasarladım..."
        "Timur Satrancı mı ? "
        "Neden bahsediyor ki bu adam ?"
        me "Efendim Timur Satrancı da ne ola ki ? "
        e "Gel sana şöyle göstereyim..."
        "İki tane karşılıklı koltuğun arasında bulunan masanın alt gözünden bir kutu çıkardı"
        "İlk başta bildiğimiz alıştığımız satranç kutularına benzettim lakin kutuyu açıp masaya taşları boşalttığında bir şey farkettim... "
        "Kutu gerekenden büyük ve taş sayısı gereğinden fazlaydı..."
        e "İlk olarak kavramak biraz güç olabilir..."
        e " Gel sana anlatayım."
        scene mor
        show timurlane
        with fade
        "Tahtayı çıkardı ve taşları yerleştirdi..."
        stop music fadeout 4.0
        me "Tahtanın görünümü biraz garibime gitti."
        play music teach fadein 4.0 fadeout 3.0
        show tmr
        with dissolve
        e "Şaşırman normal, her gören aynı tepkiyi veriyor..."
        e "Normal satrancın aksine benim satrancımın tahtası 10x11 boyutlarında..."
        e "İstersen sana taşları anlatayım..."
        me "Olur da ilk olarak bir şey sormak istiyorum..."
        e "Evet ?"
        me "Şu köşedeki birer tane fazlalık kare nedir ?"
        e "Onlar iç kalelerdir, eğer şahını rakibin iç kalesine sokabilirsen oyun berabere biter."
        e "Kazanma ihtimalin kalmadığında en iyi seçenek budur..."
        me "Anladım, diğer taşları anlatın lütfen."
        hide timurlane
        show piyon at left
        with dissolve
        e "Bunların her biri piyonlardır, piyonlar önceki taşın piyonu olarak tanınır..."
        e "Normal satrançtaki gibi hareket eder. Fakat ilk hareketinde normal satrançta olduğu gibi iki kare ilerleyemez."
        e "Ayrıca her taşın kendine ait piyonu bulunur. Vezirin piyonu, filin piyonu, devenin piyonu gibi. Bu piyonlardan hangisi rakibin ilk sırasına ulaşırsa onun taşı oyuna tekrar dönebilir."
        e " Örneğin devenin piyonu rakibin ilk sırasına ulaşırsa oyuna sadece deve geri alınabilir. Şahın piyonu ve piyonun piyonu hariç onların durumu biraz farklı."
        me "Nasıl yani ? "
        e "Şahın piyonu eğer rakibin son ilk karesine ulaşırsa {b}Prens{/b} isminde şaha eşdeğer bir taş ortaya çıkar."
        e "Eğer prens mevcutken şah düşse bile oyun devam eder."
        me "Piyonun piyonu nasıl oluyor peki ?"
        e "Oyunun en karmaşık taşı {b}piyonun piyonu{/b}dur."
        e "Piyonun piyonu rakibin ilk sırasına ulaştığında öylece kalır. Ayrıca rakip de bu taşa hamle yapamaz."
        e "Fakat bir piyon rakibin iki taşını aynı anda tehdit edebilecek bir konumda olabiliyorsa piyonun piyonu direkt olarak bu noktaya ilerler. Böylece rakibin bir taşı bu piyon ile alınır."
        hide piyon
        show piyonun1
        with dissolve
        e "Aynı bu şekilde."
        me "Yani o iki taştan herhangi birini yiyebiliriz değil mi ? "
        e "Evet !"
        hide piyonun1
        show piyonun2
        with dissolve
        e "Ayrıca, diğer bir piyonun piyonu kullanımı ise rakibin kendi taşını sıkıştırmasıyla oluşur."
        e "Örneğin fil iki kare çapraz olarak hareket eder. Fakat hareket yerlerinde rakibin taşları varsa yani filin hareketi kısıtlanmışsa, piyonun piyonu fili alacak konuma taşınır."
        hide piyonun2
        with dissolve
        e " Bu iki durumunda da eğer piyonun koyulacağı karede bir taş varsa bu taş da alınmış gibi oyun tahtasından çıkarılır."
        me "Yani piyonun piyonunun gelebileceği yerde bir taş daha varsa o taş da mı saf dışı kalmış oluyor ?"
        e "Çabuk kavrıyorsun !"

        show fil
        with dissolve
        e "Bu taşın adı ise tahmin edebileceğin gibi fil."
        me "Tahmin edeyim fil de çapraz gidiyor."
        e "Evet, lakin bildiğimiz satrançtaki gibi değil..."
        hide fil
        show fil_h
        with dissolve
        e "...normal şartlarda çapraza gidebildiği kadar gider lakin bu fil sadece iki kare çapraza gidebiliyor."
        me "Yani çaprazındaki ikinci kareye gidebiliyor, anladım."
        e "Aynen öyle ! Aynı zamanda fil diğer taşların üzerinden atlayabilir."
        hide fil_h
        show ad
        with dissolve
        e "Süvarilerin gözdesi at..."
        e "At, normal satrançtakinin tamamen aynısı bir şekilde hareket ediyor. {b}L{/b} şeklinde..."
        hide ad
        show at_h
        with dissolve
        me "Yani atın pek bir olayı yok..."
        e "Her ne kadar farklı bir şey göstermese de atlar hafif ve hızlı birliklerin vazgeçilmezi olan birliklerdir."
        e "Onlarla yıldırım gibi saldırılar yapıp insan zaiyatını aza indirgeyebilirsin."
        hide at_h
        with dissolve
        "Atlarla yapılabilecekleri anlatırken gözleri parıldıyordu,bu adam satranç tahtasını bir oyun gibi değil ..."
        "...gerçek bir savaş alanı gibi görüyor."
        me "Anladım..."
        "Karşıda gördüğüm alışılmadık bir şekle sahip olan taş dikkatimi çekti..."
        show debabe
        with dissolve
        "Timur bunun farkına varmış olacak ki hafif gülümseyerek taşı eline aldı."
        e "Demek bunu merak ettin..."
        e "Bu taşın adı {b}debbabe{/b}, mancınık olarak da anılır."
        me "Peki nasıl hareket ediyor..."
        hide debabe
        show debabe_h
        with dissolve
        e "Hareketi böyle, iki kare düz olarak hareket eder ve diğer taşların üstünden atlayabilir..."
        "Alan hasarı olarak mantıklı bir seçim olabilirdi, savaş alanında..."
        me "Anladım ! "
        hide debabe_h
        show bakan
        with dissolve
        e "Sıradaki taşımız ise {b}bakan{/b}..."
        e "Bakan sahın sağ kolu gibidir..."
        hide bakan
        show bakan_h
        with dissolve
        e "Bakanın hareketi ise bir kare çapraza gidebilceği şekildedir."
        "Demek sağ kol..."
        hide bakan_h
        with dissolve
        me "Peki ya vezir? Normalde vezir sağ kolumuz olmaz mı ?"
        show vezir
        with dissolve
        e "Bakan her ne kadar sağ kolsa, vezir sol kol olarak vazife başında bulunur..."
        me "Nasıl yani ?"
        hide vezir
        show vezir_h
        with dissolve
        e "Vezir, bakan gibi çapraz değil de düz olarak bir kare ilerler..."
        e "Vezir ve bakan birbirini tamamlayan birer taştır..."
        hide vezir_h
        with dissolve
        e "Gerçek hayatta da benzer kural geçerlidir, vezir, bakan, şah; her biri birbirinin açıklarını kapatmak için mevcuttur. "
        "Şah ne kadar da akıllı olsa, her işin altından tek başına kalkamıyor yani..."
        show zürafa
        with dissolve
        me "Zürafa savaşta nasıl etkili olabilir ki ?"
        e "Evet normal savaşta kullanması biraz zor olurdu lakin hayal dünyamızdaki savaş alanında yer almasında pek bir sakınca yok."
        hide zürafa
        show zürafa_h
        with dissolve
        e "Çapraz olarak bir kare ilerledikten sonra en az üç kare düz hareket eder."
        e "Eğer gidebilecek yeri varsa dört kare de ilerleyebilir fakat kullanım alanı biraz kısıtlı bir taş."
        me "Garip bir taş ama anladım..."
        e "Ayrıca zürafamız diğer taşların üzerinden atlayamaz."
        hide zürafa_h
        with dissolve
        e "Yavaştan taşlarımızın sonuna yaklaşıyoruz..."
        show öncü
        with dissolve
        e "Sıradaki taşımız {b}öncü{/b}..."
        "İlk bakışta ne işe yaradğını anlayamasam da ismini duyunca aklımda bir kaç fikir oluşmaya başladı"
        me "Öncü diğer taşların önünü açan bir taş mı ?"
        e "Öyle de denebilir..."
        hide öncü
        show öncü_h
        with dissolve
        e "Öncümüz çapraz ikinci kareden başlayarak sınırsız ilerler..."
        e "Diğer taşların üzerinden atlayamaz."
        me "Hmm...Tahmin ettiğimden biraz farklıymış ama anladım sanırım."
        hide öncü_h
        with dissolve
        e "Evet taşlar bu kadardı..."
        e "Gelelim oyunun kurallarına."
        "Kural mı zaten bin tane ayrı şey saydı üstüne bir de kural mı var ?"
        e "Merak etme canını fazla detayla sıkmayacağım. Öğrendiklerimizin kısa bir özeti niteliğinde olacak..."
        e "Piyonlar için, klasik satrançtaki gibi son kareye ulaşan piyon yükselir... "
        e "...Fakat farklı olarak burada piyon hangi taşın piyonuysa o taşa dönüşür."
        e """Şahın piyonu son kareye ulaştığında kazanmak için rakibin mat etmesi gereken
        Prens’e dönüşür. Prens tıpkı şah gibi hareket eder."""
        e "Piyonun piyonunu detaylı bir şekilde anlattım zaten lakin bilmen gereken bir şey daha var..."
        me "?"
        e "Eğer piyonun piyonu bahsettiğimiz duruma gelip ikinci bir kez son sıraya ulaşabilirse prens olarak geri döner..."
        me "Yani iki çeşit prens alma yöntemi mi mevcut ?"
        e "Evet !"
        e "Oyuncu çıkmaza girdiği an oyunu kaybeder."
        e """Şahını kaybeden oyuncunun elinde dıştan gelen şah ya da prens varsa bunlardan birisi şah rolü
        üstlenir ve şah gibi hareket eder."""
        e "Son olarak şah veya şah görevi alan prens rakibin iç kalesine girerse oyun beraberlik ile biter."
        "Cidden de bir strateji uzmanı gibi çok detaylı ve zekice bir oyun tasarlamış..."
        e "Anladıysan bir kere denemeye ne dersin ?"
        menu:
            "Sizin için de uygunsa bir defa oynayabilirim sanırım":
                jump oyna
            "Oyunu kavradım ama pek kendime güvenmiyorum":
                jump atla
    label oyna:
        "İkimiz de kadife kaplamalı rahat koltuklara oturduk ve birbirimize karşı mücadele etmeye başladık..."
        "Timur hiç heyecan yapmadan rahat bir tavırla hareketlerimi inceliyor ve bir sonraki hamlesini dikkatlice düşünüyordu."
        "(Bir süre sonra)"
        e "Şah Ruh !!!"
        me "Şah Ruh mu ?"
        e "Evet, benim oyunum Şah Mat değil {b}Şah Ruh{/b} diyerek bitiyor..."
        "Cidden ellerim bağlı bir şekilde Timur'un prensimin etrafını sarmasını izledim..."
        me "Tahmin ettiğim gibi... "
        "Tam bunu söylerken kapı tıklatıldı..."
        play sound knock
        "Gelen sabah karşılaştığımız cariyeydi..."
        scene sarayoda
        with fade
        show c_mutlu
        show tmr
        with dissolve
        c "Efendim müjdeli haberi vermek için buradayım..."
        c "Agha hatun nurtopu gibi bir oğlan dünyaya getirdi..."
        "Timurun gözleri kocaman sevinçli bir şekilde açıldı..."
        c "Oğlunuza nasıl şanlı bir isim vereceksiniz efendim ?"
        e "ŞAHRUH !!!"
        "Şahruh mu ?"
        stop music fadeout 4.0
        "Timur'un veliahtının doğuşunu gördüğü an ve mutluluğu çok az kişiye göstermiş olduğu suratından bir kareydi..."
        jump son
    label atla:
        e "Hmm anlıyorum..."
        e "Lakin aklında bulunsun ki {b}yenileceğinden korkan yenilmeye mahkumdur{/b}..."
        "Bu söz üstüne biraz içerlensem de haklıydı, kendime güvenmezsem başaramam."
        "Belki de sadece rakibi kışkırtmak için söylenmiş bir sözdü, eğer öyleyse işe yaradı..."
        me "Bir kez denemek istiyorum !"
        "Timur'un dudakları istediği olmuşçasına bir gülümseme şekline büründü."
        "Evet tahmin ettiğim gibi tuzak bir cümleymiş..."
        e "Demek fikrini değiştirdin !"
        jump oyna
    label son:
        show kör
        hide tmr
        hide c_mutlu
        with dissolve
        "Ne.. "
        play music harp fadeout 1.0 fadein 1.0
        "...Oluyor?"
        "Bir anda başım ağırmaya, göz kapaklarım ağırlaşmaya başladı..."
        "Bacaklarım uyuştu ve hiç bir uzvum hareket edemez oldu."
        show kör
        with dissolve
        scene öl
        with dissolve
        "Bu namütenahi karanlık da ne böyle ?"
        scene rüya3
        with fade
        "Yine o güzel görüntülerden biri..."
        "Acaba yine mi rüyadayım..."
        "Timur nerede, cariye, Şahruh ..."
        scene rüya4
        with fade
        "Sağda günbatımının keyfini çıkaran biri..."
        "Bu görüntüleri daha önce görmüş müydüm ?"
        scene rüya5
        with fade
        "Ağaçlar ve kırmızının özgürlüğü..."
        "Sonsuza kadar burada bu manzaraya karşı durabilirim sanırım..."
        scene öl
        with fade
        "Yine mi karanlık..."
        stop music fadeout 3.0
        scene göz1
        with fade
        me "Agh başım !"
        scene göz2
        with fade
        me "Huh ? Nerdeyim ben?"
        play music alla fadein 2.0 fadeout 4.0
        me "Burası..."
        me  "...benim odam..."
        me "Yani Timur, Timur Satrancı, hepsi rüya mıydı ?"
        "Bir anlığına olan biteni düşündüm..."
        "Sonra araştırmaya karar verdim..."
        "Bu kadar iyi dizayn edilmiş bir oyun benim zihnimin eseri olamazdı, ben sıradan bir lise öğrencisiyim..."
        "Bilgisayarımın başına geçtim..."
        scene araştırma
        with fade
        "Evet cidden de kulaktan duyup rüyada gördüğüm bir şeydi sanırım..."
        "Lakin her bir detayı rüyamda gördüklerimin aynısı..."
        scene emir
        with fade
        "Araştırmalarıma biraz daha devam ettiğimde Emir Timur hakkında ve Timur Satrancı hakkında yeni şeyler öğrendim..."
        "Hatta bir kaç rivayette, Timur bir dostuyla satranç oynarken dostunu şahruh etmesi üzerine oğlunun doğum haberinin gelmesi ile... "
        stop music fadeout 3.0
        "...oğluna Şahruh ismini verdiği belirtilmekte... "
        play music end fadein 1.0 fadeout 2.0
        #efekt ekleme

        scene rüya6
        e "Peki..."

        show tmr
        with dissolve

        e "Peki ya o dost sen olsaydın ?"
        me "Emir Timur ?!"


        scene rüya7
        with fade
        #timur hakkında kısa övgü
        "Emir Timur çok az insanın tam manayla bilip övdüğü bir hükümdardır..."
        "Yaptıkları, savaşları, düşünce biçimi ve daha niceleriyle tam bir strateji dehası olduğu su götürmez bir gerçektir..."
        "Ve öyle birini düşünün ki normlara uymak istemeyip norm kavramını kendince şekillendirmiş..."
        "...gücünü ilmiyle birleştirerek dünyanın görmediği yeni şeyler ortaya koymuş..."
        "İşte bu kişi Emir Timur"
        "Adını tarihe renkli harflerle yazdırmış sayılı insandan biri..."

        "{b}SON{/b}"

    return
