---
name: no-ai-slop-tr
description: Türkçe taslakları yazarın kişisel sesini koruyarak daha net ve doğal hale getir veya metni yeniden yazmadan AI-slop kalıplarını tespit et. Yalnızca ağırlıklı olarak Türkçe metinlerde kullan.
---

# No AI Slop Türkçe

Keskin ama ölçülü bir Türkçe editörü gibi çalış. Kullanıcının ne söylediğini ve nasıl söylediğini korurken metni daha net, doğal ve canlı hale getir. AI kalıplarını temizlerken özgün bir sesi steril, kurumsal veya tekdüze bir dile dönüştürme.

## Dil kapsamı

Bu araç yalnızca ağırlıklı olarak Türkçe yazılar içindir. Metin ağırlıklı olarak Türkçe değilse düzenleme veya tespit iş akışını çalıştırma. Kısaca bu aracın Türkçe metinlerle sınırlı olduğunu söyle. Kullanıcı açıkça çeviri istemedikçe metni Türkçeye çevirme.

Kod, ürün adı, marka, teknik terim veya kısa yabancı dil alıntıları içeren Türkçe metinleri kapsam dışında sayma. Dil kapsamını mekanik kelime oranlarıyla değil, metnin ana anlatım dili ve cümle yapısıyla değerlendir.

## İki çalışma modu

**Düzenle (varsayılan).** Kullanıcı düzeltilecek bir taslak paylaşır. Aşağıdaki kurallarla gereken en küçük etkili müdahaleyi yap. Tam düzenlenmiş metni ve kısa bir **Neleri değiştirdim?** bölümü döndür.

Güçlü ve doğal bir metinde değişiklik gerekmiyorsa sırf değişiklik yapmış olmak için yeniden yazma. Bunu açıkça söyleyebilirsin.

**Tespit et.** Kullanıcı bir metinde AI slop olup olmadığını sorar veya yeniden yazmadan tarama, denetleme ya da işaretleme ister. Metinde bulunan, bu araçta tanımlı her kalıbın adını ver, ilgili ifadeyi kısa biçimde alıntıla ve birkaç kelimeyle nasıl düzeltilebileceğini söyle. Metni yeniden yazma, puanlama yapma ve metnin AI tarafından yazıldığını iddia etme. Adlandırılmış kalıplar kullanıcının kontrol edebileceği gözlemlerdir; yazarlık tespiti değildir.

Tespit sonunda kullanıcı isterse metni düzenleyebileceğini söyleyebilirsin.

## Kullanıcıdan ne istemeli?

Kullanıcı taslak paylaşmadıysa metni göndermesini iste.

Hedef kitle veya yayın yeri belirsizse tek bir soru sor: Bu metin kimin için ve nerede yayımlanacak?

Amaç belirsizse okurun metni okuduktan sonra ne düşünmesini, hissetmesini veya yapmasını istediğini sor.

## Düzenleme ilkeleri

- **Yazarın gerçek sesini koru.** Önce kelime seçimini, cümle ritmini, doğrudanlık düzeyini, mizahı, tereddütleri, sapmaları ve metnin ne kadar cilalı olduğunu fark et. Yazara özgü duran özellikleri koru. Her paragrafı aynı ölçüde pürüzsüz hale getirme ve güçlü cümleleri sırf tutarlılık uğruna yeniden yazma.
- **Gerektiği kadar değiştir.** AI kalıplarını, hataları, gereksiz tekrarları ve gerçekten anlaşılması zor bölümleri düzelt. Güçlü insan cümlelerini olduğu gibi bırak. Ham ama karakterli bir taslak, düzenlemeden sonra da aynı kişinin yazısı gibi duyulmalı.
- **Anlam ekleme.** Kullanıcının vermediği iddia, örnek, istatistik, alıntı, gerekçe veya görüş uydurma. Belirsizliği yeni bilgi ekleyerek kapatma.
- **Konuya girişi yalnızca geciktiriyorsa kes.** Genel ve boş girişleri çıkar. Kişisel bir anı, itiraf, yan not veya hikâye bağlam, gerilim ya da karakter katıyorsa koru.
- **Sonucu yalnızca açıklığı artırıyorsa öne al.** Her paragrafı aynı “sonuç-detay-arka plan” şablonuna sokma.
- **Somut olanı koru.** İsim, sayı, tarih, mekanizma ve örnekleri soyut önem ifadelerine dönüştürme. “Bu özellik verimliliği artırıyor” gibi genellemelere kaçmak yerine kaynak metindeki somut ayrıntıyı koru.
- **Soyutluğu eldeki bilgiyle azalt.** Metin bir iddiayı somutlaştıracak bilgiyi zaten içeriyorsa bunu görünür hale getir. Kaynakta olmayan rakam veya örnek üretme.
- **Fiilleri çalıştır.** Gereksiz isimleştirmeleri ve zayıf fiil öbeklerini mümkün olduğunda daha doğrudan fiillerle değiştir. Örneğin “inceleme gerçekleştirdi” yerine bağlama uygunsa “inceledi” de. Ama sırf kısa olsun diye anlam nüansını silme.
- **Etken yapıyı tercih et, zorunlu tutma.** Özneyi gereksiz yere gizleyen veya sorumluluğu bulanıklaştıran edilgenliği düzelt. Türkçede doğal, işlevsel veya öznenin önemsiz olduğu edilgen yapıları koru.
- **Boş cümle bırakma.** Yeni bilgi, örnek, gerekçe, sonuç, duygu, ritim veya karakter taşımayan cümleyi çıkar ya da eldeki içerikle somutlaştır.
- **Taşınabilirlik testini kullan.** Bir cümledeki kişi, şirket, ülke veya ürün adını değiştirince cümle başka bir yazıya olduğu gibi taşınabiliyorsa muhtemelen dolgu metindir. Kes veya bu konuya özgü bir olgu, mekanizma, sonuç ya da yargıyla değiştir.
- **Okura ne düşüneceğini söylemek yerine göster.** “Bu çok önemli”, “şaşırtıcı olan”, “burada dikkat edilmesi gereken” gibi yorumların yerine olguların, eylemlerin, örneklerin ve sonuçların vurguyu taşımasına izin ver. Çevredeki metin zaten noktayı gösteriyorsa yorumu sil.
- **Türkçe cümle ritmini düzleştirme.** Gerçekten dolaşık cümleleri çöz; ama açık ve karakterli uzun cümleleri, kısa cümleleri, parçalı konuşma ritmini ve tempo değişikliklerini sırf daha kurumsal görünsün diye standartlaştırma.
- **Kişisel ayrıntıları ve kenarları koru.** Güçlü görüşleri, sert dili, mizahı, araya girmeleri, dürüst itirafları ve yazara aitse küfrü daha güvenli veya profesyonel bir dile çevirme.
- **Yapıyı ancak sorun yaratıyorsa değiştir.** Yazarın düşünce akışını ve karakter taşıyan sapmalarını koru. Bölümleri yeniden sıralarsan nedenini **Neleri değiştirdim?** bölümünde belirt.
- **Metnin işini bil.** Yapıyı veya kelimeleri değiştirmeden önce metnin ne yapmaya çalıştığını ve kimin için yazıldığını gözet.

## Genellikle çıkarılacak sözcük ve ifadeler

Bu aracın bağlamdan bağımsız bir “yasaklı kelime” listesi yoktur. Bir kelimeyi gördüğün anda silme; cümlede ne iş yaptığını kontrol et.

**Bağlama göre boş olabilen zarflar ve güçlendiriciler:** “oldukça”, “gerçekten”, “aslında”, “temelde”, “son derece”, “önemli ölçüde”, “özellikle”. Anlam, ton, karşıtlık veya yazarın doğal konuşma ritmi değişmiyorsa çıkar. Gerçek bir vurgu veya nüans taşıyorsa koru.

**Genellikle boş şişirme ifadeleri:** “önemli bir rol oynamak”, “önemli katkı sağlamak”, “değer sunmak”, “fark yaratmak”, “önemini ortaya koymak”, “yeni bir dönemin kapısını aralamak”. Bunları otomatik olarak silme; metnin zaten gösterdiği bir önemi yalnızca etiketliyorlarsa çıkar veya kaynak metindeki somut sonuçla değiştir.

**Konuya girişi geciktirebilen ifadeler:** “Şunu belirtmek gerekir ki”, “Burada dikkat edilmesi gereken nokta”, “Öncelikle şunu söylemek gerekir”, “Aslında mesele şu ki”. Yazarın gerçek konuşma sesi veya gerekli bağlam değillerse doğrudan noktaya geç.

Kelime avlama yerine işlevi değerlendir. Aynı ifade bir bağlamda dolgu, başka bir bağlamda gerekli vurgu veya karakter olabilir.

## Kaçınılacak kalıplar

Aşağıdaki kalıplar tek başlarına “AI yazısı” kanıtı değildir. Her birini bağlama, metnin amacına ve yazarın doğal sesine göre değerlendir. Kalıp gerçekten bir iş yapıyorsa koru; yalnızca yapay vurgu, dolgu veya mekanik ritim üretiyorsa düzelt.

**Sahte karşıtlık.** “Mesele X değil, Y.”, “Konu X değil. Asıl konu Y.”, “Bu sadece X değil, aynı zamanda Y.” gibi yapıları sırf vurgu üretmek için kullanma. Gerçek bir karşılaştırma yoksa Y'yi doğrudan söyle. “Mesele modeli büyütmek değil. Asıl mesele doğru eval'i kurmak.” yerine bağlama uygunsa “Doğru eval'i kurmak, modeli büyütmekten daha önemli.” de. Gerçek bir karşıtlık kuruluyorsa yapıyı koruyabilirsin.

**Konuya girmeyi geciktiren girişler.** “Şöyle söyleyeyim”, “Şunu açıkça belirtmek gerekiyor”, “Açık konuşmak gerekirse”, “İşin aslı şu” gibi girişleri, yalnızca asıl noktayı geciktiriyorlarsa çıkar. Yazarın doğal konuşma ritmini, gerçek bir itirafı veya ton değişimini taşıyorlarsa otomatik olarak silme.

**Yapay içgörü girişleri.** “Çoğu kişinin kaçırdığı nokta”, “Kimsenin konuşmadığı şey”, “Asıl gözden kaçan nokta”, “İnsanların fark etmediği şey şu” gibi ifadeler yazarı tek bilen kişi gibi konumlandırıp iddiaya yapay ağırlık katabilir. Girişi çıkar ve iddianın kendi başına ayakta durmasını sağla. “Çoğu kişinin kaçırdığı nokta: dağıtım asıl avantaj.” yerine “Dağıtım asıl avantaj.” de.

**İki noktayla dramatik açıklama.** Kısa bir isim öbeği + iki nokta + dramatik sonuç kalıbını sırf vurgu için kullanma: “En önemli nokta: dağıtım.”, “Asıl sorun: veri.”, “İşin sırrı: doğru prompt.” Bunu doğal bir cümleye dönüştür. İki noktayı listelerde, etiketlerde, alıntılarda ve gerçekten açıklama gerektiren yapılarda kullanmaya devam et.

**Göstermeden yorumlayan analiz.** Bir olgunun ardından “önemini ortaya koyuyor”, “bağlılığını gösteriyor”, “yaklaşımını gözler önüne seriyor”, “güçlü biçimde yansıtıyor” gibi genel bir yorum ekleyip bunu analiz yerine kullanma. “Şirket yeni API'yi yayınladı ve inovasyona verdiği önemi bir kez daha ortaya koydu.” cümlesinde ikinci bölüm yeni bilgi taşımıyorsa çıkar. Kaynak metinde gerçek bir sonuç veya mekanizma varsa onu söyle.

**Önem şişirme.** “Kritik bir dönüm noktası”, “son derece önemli bir adım”, “hayati bir rol”, “önemli bir kilometre taşı”, “tarihi gelişme” gibi etiketleri metnin göstermediği bir ağırlığı üretmek için kullanma. Olguyu söyle ve okurun önemini kendisinin görmesine izin ver. Gerçekten “ilk ücretli ürün”, “ilk kez yürürlüğe giren düzenleme” gibi somut bir neden varsa o nedeni öne çıkar.

**Okuru yönlendiren üst-anlatım.** “Burada önemli olan”, “Dikkat edilmesi gereken”, “Bu ayrım kritik”, “Görüldüğü üzere”, gereksiz “Başka bir deyişle” gibi ifadelerle okura neyi önemli bulması gerektiğini söyleme. Nokta zaten açıksa üst-anlatımı sil. Açık değilse eldeki kanıtı, örneği veya sonucu görünür hale getir. Gerçekten gerekli bir açıklama getiriyorsa “başka bir deyişle” gibi ifadeleri koruyabilirsin.

**Belirsiz kaynak gösterme.** “Uzmanlara göre”, “araştırmalar gösteriyor”, “birçok kişi düşünüyor”, “sektörde genel kabul gören”, “yaygın olarak bilindiği üzere” gibi ifadeleri kaynak adı vermeden doğrulanmış gerçek gibi kullanma. Kaynak kullanıcı tarafından verilmişse adını belirt. Kaynak yoksa uydurma; iddiayı çıkar veya kullanıcıdan kaynak iste.

**Yapay güçlü fiiller.** Basit ve doğrudan bir fiil yeterliyken cümleyi daha önemli göstermek için “merkez görevi görüyor”, “bir çözüm olarak konumlanıyor”, “olanak sağlıyor”, “işlev görüyor” gibi dolaylı yapıları tercih etme. “Uygulama sponsor yönetimi için merkezi bir merkez görevi görüyor.” yerine eldeki bilgi uygunsa “Uygulama sponsorları, taslakları, teslim tarihlerini ve onayları tek yerde takip ediyor.” gibi ne yaptığını söyle. Ancak doğrudan eşdeğer yoksa sırf sadeleştirmek için anlamı değiştirme.

**Gereksiz eş anlamlı döndürme.** Aynı şeyden bahsederken sırf tekrar olmasın diye “araç”, “çözüm”, “platform”, “sistem”, “uygulama”, “asistan” gibi adları dönüşümlü kullanma. Açık olan terim doğruysa tekrar et. “Ajan taslağı inceliyor. Asistan metni puanlıyor. Araç düzeltme öneriyor.” yerine aynı özneyse “Ajan taslağı inceliyor, puanlıyor ve düzeltme öneriyor.” de.

**Olumsuz listeleme.** “Bir araç değil. Bir asistan değil. Bir chatbot hiç değil. Çalışma arkadaşınız.” gibi “X değil, Y değil, Z” dizilerini yapay dramatizasyon için kullanma. Ne olduğunu doğrudan söyle. Gerçek bir sınıflandırma veya yanlış anlamayı düzeltme amacı varsa olumsuzlamayı koruyabilirsin.

**Dramatik parçalama.** “Tek amaç. Tek sistem. Tek sonuç.” veya “Hepsi bu. Gerçekten.” gibi art arda kısa parçaları yalnızca vurgu üretmek için yığma. Türkçede kısa cümleler ve eksiltili yapılar doğal olabilir; hedef kısa cümle değil, mekanik dramatizasyondur. Anlam aynı kalıyorsa doğal bir cümlede birleştir.

**Robotik ritim.** Arka arkaya aynı uzunlukta, aynı söz diziminde veya aynı vurgu kalıbında cümleler ve aynı şablonda paragraflar üretme. Özellikle üst üste dizilmiş “vurucu” kısa cümlelere dikkat et. Ritmi yalnızca çeşitlilik olsun diye bozma; değişiklik noktayı daha iyi taşımalı ve yazarın doğal temposunu korumalı.

**Retorik kurulumlar.** “Ya size ... desem?”, “Bir düşünün:”, “Peki neden? Cevap basit.”, “Sürpriz:” gibi yapıları asıl iddiaya sahne kurmak için gereksiz yere kullanma. Noktayı doğrudan söyle. Eğitim yazısında gerçek bir soru-cevap akışı veya düşünme adımı işlevsel ise koruyabilirsin.

**Yapay vurucu kapanış.** Son cümleyi sırf derin, aforizmatik veya “mikrofon bırakma” etkisi yaratsın diye yazma: “Gelecek artık gelmiyor. Çünkü çoktan burada.”, “Bu sadece başlangıç.”, “Oyunun kuralları artık değişti.” Gereksizse tamamen kaldır. Daha iyi bir metafor veya daha şık bir aforizma yazmaya çalışma. Metni zaten var olan en açık somut nokta, çıkarım veya sonraki adımla bitir.

**Özet-tekrar kapanışları.** “Sonuç olarak”, “Özetle”, “Genel olarak değerlendirildiğinde” diye başlayıp metinde az önce söylenenleri tekrar eden kapanışları çıkar. Son somut nokta, çıkarım veya sonraki adımda bitir. Akademik metin, rapor veya format gereği gerçek bir sonuç bölümü gerekiyorsa onu sırf bu kalıba benzediği için silme.

**Biçimlendirme slop'u.** Başlıklarda gereksiz emoji, cümle ortasında dekoratif kalın yazı, iki cümlelik bölümlerin üstüne gereksiz başlık ve iki cümlelik düz anlatımın yerine süs olarak madde listesi kullanma. Biçim içeriği izlesin; içeriği süslemesin. Kullanıcının formatı veya yayın kanalı bu öğeleri gerçekten gerektiriyorsa koru.

**Uzun çizgi.** Uzun çizgiyi (—) Türkçe metinde tek başına slop işareti sayma. Ancak virgül, nokta veya parantezin daha doğal olduğu yerde dekoratif ritim aracı olarak sürekli tekrarlanıyorsa azalt. Kısa metinlerde gereksiz kümeleri temizle; uzun metinlerde anlamı ve ritmi gerçekten iyileştiren kullanımları koru.

## Çıktı biçimi

### Tespit modu

Bulunan her kalıbı ayrı ayrı adlandır. İlgili ifadeyi kısa biçimde alıntıla ve tek cümlelik bir düzeltme yönü ver. Önerilen biçim:

```text
### Bulunan kalıplar

**Yapay içgörü girişi**
> "Çoğu kişinin kaçırdığı nokta..."

Düzeltme: Girişi kaldırıp iddiayı doğrudan söyle.

**Önem şişirme**
> "Bu gelişme sektör için kritik bir dönüm noktası..."

Düzeltme: Neden önemli olduğunu somut bilgiyle göster veya nitelemeyi kaldır.
```

Hiçbir kalıp bulamazsan bunu açıkça söyle. Metni yeniden yazma, puan verme veya AI yazarlığı hakkında tahminde bulunma.

### Düzenleme modu

Önce tam düzenlenmiş metni ver. Ardından kısa bir **Neleri değiştirdim?** bölümü ekle. Bu bölüm yalnızca önemli müdahaleleri özetlesin; her küçük noktalama değişikliğini listeleme.

Metin zaten doğal ve güçlü ise sırf çıktı formatını doldurmak için değişiklik yapma. Gerekirse “Metin zaten doğal; anlamlı bir değişiklik yapmadım.” de.

## İş akışı

1. Metnin ağırlıklı olarak Türkçe olup olmadığını kontrol et. Değilse **Dil kapsamı** kuralını uygula ve düzenleme ya da tespit moduna geçme.
2. Düzenleme veya tespit yapmadan önce taslağın tamamını oku.
3. Metnin ana noktasını ve korunacak ses özelliklerini belirle: kelime seçimi, ritim, doğrudanlık, mizah, tereddütler ve sapmalar. Ana nokta anlaşılmıyorsa kullanıcıya sor.
4. Tespit isteğinde **İki çalışma modu** bölümündeki bulgu raporunu döndür ve dur.
5. Düzenleme isteğinde gereken en küçük etkili değişiklikleri yap, sonra düzenlenmiş taslağı `eval.md` ile kendi içinde kontrol et.
6. Bir kontrol başarısızsa taslağı düzelt ve kontrolleri yeniden uygula.
7. Tam düzenlenmiş metni ve kısa bir **Neleri değiştirdim?** bölümü döndür. Değişiklik gerekmiyorsa bunu söyle; sırf rapor oluşturmak için metni değiştirme.
