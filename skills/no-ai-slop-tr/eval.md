# No AI Slop Türkçe — Değerlendirme

Bu dosya, `SKILL.md` içindeki kuralların uygulanıp uygulanmadığını kontrol eden kalite kapısıdır. Yeni bir düzenleme kuralı icat etmez; çelişki halinde `SKILL.md` esas alınır.

## Değerlendirme protokolü

Her uygulanabilir kontrolü şu üç sonuçtan biriyle değerlendir:

- **GEÇTİ:** Kural karşılandı.
- **KALDI:** Sorun hâlâ var veya düzenleme yeni bir sorun üretti.
- **UYGULANAMAZ:** Bu kontrol, mevcut metin ya da çalışma modu için geçerli değil.

Düzenleme modunda uygulanabilir herhangi bir kontrol **KALDI** ise kullanıcıya son metni vermeden önce taslağı düzelt ve kontrolleri yeniden çalıştır. Anlam, kaynak, belirsizlik ve yazarın sesiyle ilgili kontrolleri sırf diğer kalıplar temizlendi diye esnetme.

Bu kontrol listesini normal yanıtta kullanıcıya dökme. Kullanıcı açıkça değerlendirme raporu istemedikçe yalnızca `SKILL.md` içinde tanımlanan çıktı biçimini kullan.

Tespit modunda metni yeniden yazma. Bu modda düzenleme sonrası kontrolleri değil, dil kapsamını, sınıflandırmayı, çakışmayı ve tespit çıktısı sözleşmesini değerlendir.

## Dil kapsamı

**LANG-01 — Ana anlatım dili.** Girdi, ana anlatım dili ve cümle yapısı bakımından ağırlıklı olarak Türkçe mi? Kod, marka, ürün adı, teknik İngilizce terimler veya kısa yabancı dil alıntıları tek başına metni kapsam dışına çıkarmamalı.

**LANG-02 — Kapsam dışı davranış.** Metin ağırlıklı olarak Türkçe değilse düzenleme veya tespit iş akışı durdu mu; araç yalnızca Türkçe metinlerle sınırlı olduğunu kısa biçimde belirtti mi; kullanıcı açıkça istemedikçe metni çevirmedi, yeniden yazmadı veya denetlemedi mi?

## Anlamı koruma

**SEM-01 — Yeni bilgi eklememe.** Düzenleme, kullanıcının vermediği iddia, örnek, istatistik, alıntı, gerekçe, görüş veya olgu ekliyor mu? Ekliyorsa **KALDI**.

**SEM-02 — Belirsizliği uydurarak çözmeme.** Zamir, kapsam, neden-sonuç, teknik terim, aktör veya başka bir yerel anlam belirsizse düzenleme sessizce bir yoruma karar verdi mi? Belirsizlik gerekli ise kullanıcıya sorulmalı.

**SEM-03 — Önerme korunumu.** Basitleştirme sırasında asıl önerme; yeni bir aktör, sonuç, neden, yetenek, karşılaştırma veya kapsam kazanmış ya da kaybetmiş mi?

**SEM-04 — Kesinlik ve kanıt düzeyi.** “olabilir”, “görünüyor”, “-mış/-miş”, olasılık, çıkarım, tamamlanmışlık veya kanıta dayalı anlatım gibi nüanslar korunmuş mu? Metin kaynakta olduğundan daha kesin veya daha iddialı hale gelmemeli.

**SEM-05 — Somut ayrıntı korunumu.** İsim, sayı, tarih, mekanizma, örnek ve kaynak metindeki başka somut ayrıntılar genel “önem”, “değer”, “etki” veya “verimlilik” söylemine dönüşmüş mü?

**SEM-06 — Kaynak doğruluğu.** Kaynak adı kullanıcı tarafından verilmediyse düzenleme yeni bir kaynak uyduruyor mu? Belirsiz kaynak gösterme temizlenirken iddia doğrulanmış gerçek gibi bırakılmamalı.

## Yazarın sesini koruma

**VOICE-01 — Kelime ve ton.** Yazarın ayırt edici kelime seçimi, doğrudanlık düzeyi, mizahı, sertliği, tereddütleri ve cilalılık seviyesi korunmuş mu?

**VOICE-02 — Ritim.** Açık ve karakterli uzun cümleler, kısa cümleler, eksiltili yapılar ve tempo değişimleri sırf standartlaştırmak için düzleştirilmiş mi?

**VOICE-03 — Kişisel kenarlar.** Güçlü görüş, araya girme, dürüst itiraf, mizah veya yazara ait küfür gereksiz yere daha güvenli, kurumsal ya da profesyonel bir dile çevrilmiş mi?

**VOICE-04 — Yapı.** Yazarın düşünce akışı ve karakter taşıyan sapmaları sorun yaratmadığı halde yeniden sıralanmış mı? Yapı değiştiyse bunun gerekçesi “Neleri değiştirdim?” bölümünde belirtilmeli.

**VOICE-05 — Minimum müdahale.** Güçlü ve doğal cümleler sırf tutarlılık, kısalık veya “daha iyi yazılmış” görünmesi için yeniden yazılmış mı?

**VOICE-06 — Müdahale ve kesme orantısı.** Yapılan değişiklik ve kesme miktarı metindeki gerçek slop, tekrar ve belirsizlikle orantılı mı? Ham ama karakterli ayrıntılar, sapmalar, ritim veya kişisel malzeme sırf metni daha kısa ve düzenli yapmak için agresif biçimde budanmamış olmalı.

## Genel düzenleme ilkeleri

**EDIT-PRINCIPLE-01 — Konuya giriş.** Boş ve genel girişler kesilmiş; bağlam, gerilim veya karakter taşıyan kişisel girişler korunmuş mu?

**EDIT-PRINCIPLE-02 — Sonucu öne alma.** Sonuç yalnızca açıklığı artırdığı yerde öne alınmış mı; her paragraf aynı “sonuç-detay-arka plan” şablonuna sokulmamış mı?

**EDIT-PRINCIPLE-03 — Doğrudan fiiller.** Gereksiz isimleştirme ve zayıf fiil öbekleri, anlam kaybı yaratmadan daha doğrudan fiillere çevrilmiş mi?

**EDIT-PRINCIPLE-04 — Etkenlik.** Etken yapı açıklığı artırdığı yerde tercih edilmiş; özne bilinmiyor, önemsiz veya işlevsel olarak geri plandaysa doğal edilgen yapı korunmuş mu?

**EDIT-PRINCIPLE-05 — Boş cümleler.** Yeni bilgi, gerekçe, örnek, sonuç, duygu, ritim veya karakter taşımayan cümleler kaldırılmış ya da yalnızca kaynakta bulunan bilgiyle somutlaştırılmış mı?

**EDIT-PRINCIPLE-06 — Taşınabilirlik.** Kişi, şirket, ülke veya ürün adı değişince başka bir yazıya aynen taşınabilecek genel cümleler kesilmiş veya kaynakta bulunan konuya özgü ayrıntıyla somutlaştırılmış mı?

**EDIT-PRINCIPLE-07 — Göster, etiketleme.** Metin okura “önemli”, “şaşırtıcı”, “kritik” gibi etiketlerle ne düşüneceğini söylemek yerine mevcut olgu, eylem ve sonuçların bunu göstermesine izin veriyor mu?

**EDIT-PRINCIPLE-08 — Bağlamsız yasak yok.** Zarflar, güçlendiriciler, geçiş ifadeleri veya resmî kipler yalnızca kelime listesinde göründükleri için mekanik biçimde silinmiş mi? İşlevsel olan kullanımlar korunmalı.

**EDIT-PRINCIPLE-09 — Boş zarflar ve güçlendiriciler.** “oldukça”, “gerçekten”, “aslında”, “temelde”, “son derece”, “önemli ölçüde”, “özellikle” gibi ifadeler anlam, ton, karşıtlık veya yazarın doğal ritmine katkı sağlamıyorsa çıkarılmış mı? Gerçek vurgu veya nüans taşıyan kullanımlar korunmuş olmalı.

## Kalıp kontrolleri

Her kontrolde iki şeyi birlikte değerlendir: slop işlevi temizlenmiş mi ve aynı yüzey biçiminin meşru kullanımı yanlışlıkla silinmiş mi?

### Giriş, vurgu ve yorum kalıpları

**PAT-01 — Sahte karşıtlık.** “Mesele X değil, Y”, “sadece X değil, aynı zamanda Y” gibi yapay vurgu karşıtlıkları düzeltilmiş mi? Gerçek karşılaştırma veya yanlış anlamayı düzeltme amacı varsa yapı korunmuş mu?

**PAT-02 — Konuya girmeyi geciktiren girişler.** “Şöyle söyleyeyim”, “Açık konuşmak gerekirse”, “İşin aslı şu” gibi yalnızca noktayı geciktiren girişler temizlenmiş mi? Gerçek itiraf, ton değişimi veya kişisel ritim taşıyan kullanımlar korunmuş mu?

**PAT-03 — Yapay içgörü girişleri.** “Çoğu kişinin kaçırdığı nokta”, “Kimsenin konuşmadığı şey” gibi iddiaya yapay otorite katan girişler kaldırılmış mı?

**PAT-04 — İki noktayla dramatik açıklama.** Kısa isim öbeği + iki nokta + dramatik sonuç kalıbı doğal cümleye dönüştürülmüş mü? Liste, etiket, alıntı ve gerçek açıklama amaçlı iki noktalar korunmuş mu?

**PAT-05 — Göstermeden yorumlayan analiz.** Olgunun ardından gelen “önemini ortaya koyuyor”, “yaklaşımını gözler önüne seriyor” türü kanıtsız yorumlar temizlenmiş mi? Kaynakta gerçek mekanizma veya sonuç varsa o korunmuş mu?

**PAT-06 — Önem şişirme.** “kritik dönüm noktası”, “hayati rol”, “tarihi gelişme” gibi kanıtsız büyüklük etiketleri kaldırılmış mı? Kaynakta somut olarak ilk, tek, tarihsel veya ölçülebilir bir neden varsa o neden korunmuş mu?

**PAT-07 — Okuru yönlendiren üst-anlatım.** “Burada önemli olan”, “Dikkat edilmesi gereken”, “Görüldüğü üzere” gibi okura neyi önemsemesi gerektiğini söyleyen gereksiz üst-anlatım temizlenmiş mi? Gerçek açıklama yapan “başka bir deyişle” benzeri kullanımlar korunmuş mu?

**PAT-08 — Belirsiz kaynak gösterme.** “Uzmanlara göre”, “araştırmalar gösteriyor”, “birçok kişi düşünüyor” gibi kaynaksız atıflar kaldırılmış, adlandırılmış veya kullanıcıdan kaynak istenecek şekilde ele alınmış mı? Kaynak uydurulmamış mı?

### Türkçeye özgü bürokratik ve çeviri kokan yapılar

**PAT-09 — Yapay güçlü fiiller.** “merkez görevi görüyor”, “çözüm olarak konumlanıyor”, “işlev görüyor” gibi sırf ağırlık katan dolaylı yüklemler daha doğrudan hale getirilmiş mi? Anlamı birebir karşılamayan sadeleştirme yapılmamış mı?

**PAT-10 — Mekanik geçiş bağlaçları.** “Bu bağlamda”, “Bununla birlikte”, “Öte yandan”, “Dolayısıyla”, “Nitekim” gibi ifadeler gerçek mantıksal ilişki kurmadan metni yapıştırıyorsa temizlenmiş mi? Gerçek neden-sonuç, karşıtlık, doğrulama veya ekleme ilişkisi taşıyanlar korunmuş mu?

**PAT-11 — Bürokratik isimleştirme.** “inceleme gerçekleştirmek”, “değerlendirmede bulunmak” gibi gereksiz çevresel isim + genel fiil yapıları doğrudanlaştırılmış mı? “kontrol etmek”, “yardım etmek”, “fark etmek” gibi yerleşik birleşik fiiller yanlışlıkla hedeflenmemiş mi? Terimleşmiş hukuki/teknik ifade korunmuş mu?

**PAT-12 — Edilgenlik sislemesi.** Kaynakta aktör belli olduğu halde sorumluluğu gereksiz gizleyen edilgen yapı düzeltilmiş mi? Aktör bilinmiyor veya önemsizse edilgen korunmuş; kaynakta olmayan aktör eklenmemiş mi?

**PAT-13 — Olanak sağlama ve hale getirme zincirleri.** “mümkün hale getirmek”, “olanak sağlamak”, “yapabilir hale getirmek” gibi gereksiz zincirler doğrudanlaştırılmış mı? Genel bir hız/fayda iddiası, somut yeni erişim veya yetenek sanılmadan ele alınmış mı? Gerçekten yeni bir yetenek, erişim veya yetki anlatan kullanımlar korunmuş mu?

**PAT-14 — Soyut isim yığılması.** Birden fazla soyut isim, tamlama veya isim-fiil eylemi görünmez hale getiriyorsa cümle çözülmüş mü? Teknik terim olan isim öbekleri korunmuş ve yeni aktör/neden/sonuç uydurulmamış mı?

**PAT-15 — Gösterici zamir zinciri.** Ardışık “Bu durum”, “Bu süreç”, “Bu yaklaşım”, “Bu yapı” kullanımları gönderimi belirsizleştiriyorsa gerçek özne veya eylem görünür hale getirilmiş mi? Açık ve akışı kolaylaştıran göstericiler korunmuş mu?

**PAT-16 — Resmî kip otomatiği.** Gündelik, editoryal veya kişisel metindeki mekanik “-maktadır/-mektedir” dizileri doğal tona çekilmiş mi? Akademik, hukuki veya kurumsal üslup ile “-mıştır/-miştir” biçiminin tamamlanmışlık, çıkarım veya kanıtsallık nüansı korunmuş mu?

**PAT-17 — Üçlü pazarlama sıfatları.** “hızlı, güçlü ve kullanıcı dostu” gibi kanıtsız pazarlama sıfatı kümeleri temizlenmiş mi? Gerçek ve birbirinden ayrı üç özelliğin sayıldığı listeler korunmuş mu?

**PAT-18 — Yapay gözlem dili.** “karşımıza çıkıyor”, “dikkat çekiyor”, “öne çıkıyor”, “kendini gösteriyor” yalnızca olgunun varlığını dramatize ediyorsa doğrudanlaştırılmış mı? Gerçek bir karşılaştırmada bir özelliğin diğerlerinden ayrıldığını anlatan kullanım korunmuş mu?

**PAT-19 — Çeviri kokan cümle iskeleti.** “X üzerinde etki yaratmak”, gereksiz “sahip olmak” zincirleri, “X tarafında” ve İngilizce isim ağırlıklı iskeletler gerçekten doğal olmayan yerde daha doğal Türkçe sözdizimine çevrilmiş mi? “Backend tarafında Go” gibi açık teknik ayrımlar sırf yüzey biçimi yüzünden değiştirilmemiş mi?

### Ritim, kapanış ve biçimlendirme

**PAT-20 — Gereksiz eş anlamlı döndürme.** Aynı varlık sırf tekrar olmasın diye “araç/çözüm/platform/sistem/asistan” arasında dolaştırılmışsa tutarlı adlandırmaya dönülmüş mü? Gerçekten farklı varlıklar tekleştirilmemiş mi?

**PAT-21 — Olumsuz listeleme.** “Bir araç değil. Bir asistan değil. Bir chatbot hiç değil.” türü yapay dramatizasyon doğrudan ifadeye çevrilmiş mi? Gerçek sınıflandırma veya yanlış anlamayı düzeltme amacı korunmuş mu?

**PAT-22 — Dramatik parçalama.** “Tek amaç. Tek sistem. Tek sonuç.” gibi yalnızca vurgu üretmek için yığılmış kısa parçalar doğal cümleye dönüştürülmüş mü? Türkçede doğal kısa cümle ve eksiltili anlatım sırf kısa olduğu için birleştirilmemiş mi?

**PAT-23 — Robotik ritim.** Aynı uzunluk, söz dizimi veya vurgu kalıbındaki ardışık cümleler ve şablon paragraflar düzeltilmiş mi? Ritim yalnızca çeşitlilik olsun diye bozulmamış ve yazarın temposu korunmuş mu?

**PAT-24 — Retorik kurulumlar.** “Ya size ... desem?”, “Bir düşünün:”, “Peki neden? Cevap basit.” gibi gereksiz sahne kurulumları doğrudanlaştırılmış mı? Eğitim veya anlatım içinde gerçek soru-cevap işlevi olan yapılar korunmuş mu?

**PAT-25 — Yapay vurucu kapanış.** Gereksiz aforizmatik veya “mikrofon bırakma” kapanışı silinmiş mi? Daha süslü yeni bir metaforla değiştirilmemiş ve metin mevcut somut nokta, çıkarım veya sonraki adımla bitirilmiş mi?

**PAT-26 — Özet-tekrar kapanışları.** Metinde az önce söylenenleri tekrar eden “Sonuç olarak”, “Özetle”, “Genel olarak değerlendirildiğinde” kapanışları temizlenmiş mi? Önceki metin yoksa sırf bağlaçtan tekrar varsayılmamış mı? Akademik, rapor veya format gereği gerçek sonuç bölümü gerekiyorsa korunmuş mu?

**PAT-27 — Biçimlendirme slop'u.** Gereksiz emoji başlıklar, dekoratif kalın yazılar, iki cümlelik bölümlerin üstündeki süs başlıkları ve gereksiz madde listeleri temizlenmiş mi? Kullanıcının yayın kanalı veya formatı bu öğeleri gerektiriyorsa korunmuş mu?

**PAT-28 — Uzun çizgi.** Uzun çizgi (—) sırf ritim süsü olarak kümeleniyorsa azaltılmış mı? Anlamı veya ritmi gerçekten iyileştiren kullanımlar korunmuş ve sayısal bir kota uygulanmamış mı?

**PAT-29 — Geciken adlandırma.** Yalın göstericinin neyi anlattığı eldeki bağlamdan anlaşılmıyor ve ad uzun bir niteleme veya kurulumdan sonra geliyorsa kaynakta bulunan ad öne alınmış mı? Öncesi verilmeyen cümle kendi içinde değerlendirilmiş mi? Açık gönderimler, adı başta belli yapılar, kısa tanımlar, işlevsel edebî geciktirme ve doğrudan alıntılar korunmuş mu? Ad kaynakta yoksa veya anlam belirsizse tahmin yerine gerekli soru sorulmuş mu? Sözcük sayısı kotası veya genel bir “Bu ile başlama” yasağı uygulanmamış mı?

## Çakışma ve sınıflandırma

**OVERLAP-01 — Tek sorunu çift raporlamama.** Aynı dil parçasındaki aynı işlevsel sorun birden fazla kalıp adıyla raporlanmış mı? Öyleyse en spesifik kalıp seçilmeli. Dekoratif bir başlığın kendisi PAT-27 diye raporlandıysa aynı başlığı PAT-07 diye bir daha sayma; bağımsız okur yönlendirmesi ayrı olabilir.

**OVERLAP-02 — Bağımsız sorunları koruma.** Aynı cümlede farklı dil parçalarında gerçekten bağımsız iki sorun varsa yanlışlıkla tek bulguya indirilmiş mi? Bağımsız sorunlar ayrı raporlanabilir.

**OVERLAP-03 — İsimleştirme/edilgenlik/yığılma ayrımı.** Birden fazla soyut isim veya tamlama eylemi görünmez yapıyorsa **Soyut isim yığılması**; isim yığını yokken aktör geri plana itiliyorsa **Edilgenlik sislemesi**; aktör açıkken sorun çevresel isim + genel fiil yapısıysa **Bürokratik isimleştirme** seçilmiş mi?

**OVERLAP-04 — Gözlem/yorum/önem ayrımı.** “karşımıza çıkıyor” türü gözlemci dolgu **Yapay gözlem dili**; olgunun neyi gösterdiğine dair kanıtsız yorum **Göstermeden yorumlayan analiz**; büyüklük veya tarihsel ağırlık etiketi **Önem şişirme** olarak sınıflandırılmış mı?

**OVERLAP-05 — Geciken adlandırma ve diğer kalıplar.** Tek cümledeki gecikmiş adlandırma PAT-29 olarak değerlendirilmiş, yalnızca gösterici içerdiği için ayrıca PAT-15 sayılmamış mı? Ardışık belirsiz bağlamalar PAT-15 altında kalmış mı? Karşıtlık kurulumundaki genel X sınıfı, sonda açıklanan asıl Y adının baştan belli olduğu şeklinde yorumlanmış mı? PAT-01 ve PAT-29 birlikte raporlanıyorsa yapay vurgu ve geciken adlandırma için ayrı işlevsel gerekçe verilmiş mi? Tek düzenleme iki bağımsız sorunu çözebilir.

## Türkçe doğallık kontrolü

**NAT-01 — Türkçe sözdizimi.** Düzenlenmiş metin Türkçe yazılmış gibi doğal mı, yoksa kelimeler Türkçe olsa da İngilizce iskeleti sürüyor mu?

**NAT-02 — Özne dengesi.** Açıklık için gerekli olmayan özneler sırf İngilizce cümle düzenine uymak için tekrar tekrar eklenmiş mi? Buna karşılık belirsizliğe yol açan özne eksiklikleri gerekli yerde giderilmiş mi?

**NAT-03 — Kip ve görünüş.** Zaman, görünüş, tamamlanmışlık, çıkarım ve kanıtsallık nüansları metnin üslup düzeyiyle birlikte korunmuş mu?

**NAT-04 — Kayıt ve resmiyet.** Metin sırf “daha doğal” olsun diye gereksiz samimileştirilmiş ya da sırf “daha iyi” görünsün diye kurumsallaştırılmış mı?

**NAT-05 — Sesli okuma testi.** Metin, hedef bağlamına uygun bir Türkçe konuşur/yazar tarafından sesli okunduğunda doğal akıyor mu? Düzeltme öncesindeki karakterli ritim gereksiz yere kaybolmuş mu?

## Düzenleme modu çıktısı

**OUT-EDIT-01 — Tam metin.** Yanıt, parçalı öneriler yerine tam düzenlenmiş metni içeriyor mu?

**OUT-EDIT-02 — Neleri değiştirdim?** Tam metnin ardından kısa bir **Neleri değiştirdim?** bölümü var mı ve yalnızca önemli müdahaleleri mi özetliyor?

**OUT-EDIT-03 — Gereksiz değişiklik yok.** Metin zaten doğal ve güçlü ise sırf çıktı üretmek için değiştirilmemiş mi? Gerekirse anlamlı değişiklik yapılmadığı açıkça söylenmiş mi?

**OUT-EDIT-04 — Yapı değişikliği açıklaması.** Bölüm veya düşünce sırası değiştirildiyse bunun nedeni **Neleri değiştirdim?** bölümünde belirtilmiş mi?

## Tespit modu çıktısı

**OUT-DETECT-01 — Yeniden yazmama.** Tespit isteğinde kaynak metin yeniden yazılmamış mı?

**OUT-DETECT-02 — Adlandırılmış kalıp.** Her bulgu, `SKILL.md` içinde tanımlı kalıp adlarından biriyle açıkça adlandırılmış mı?

**OUT-DETECT-03 — Tespit kapsamı.** Girdide `SKILL.md` tarafından tanımlanan ve gerçekten uygulanabilir olan tüm kalıplar raporlanmış mı? Bir veya birkaç doğru bulgu vermek, metindeki diğer açık kalıpları atlamayı geçerli kılmaz.

**OUT-DETECT-04 — Kanıt ve yön.** Her bulgu kısa bir ilgili alıntı ve tek cümlelik düzeltme yönü içeriyor mu?

**OUT-DETECT-05 — Yazarlık iddiası yok.** Metnin AI tarafından yazıldığına dair tahmin, kesin hüküm veya “AI skoru” verilmemiş mi?

**OUT-DETECT-06 — Puanlama yok.** Metin genel bir slop puanı, yüzdesi veya benzeri yapay nicel sonuçla değerlendirilmemiş mi?

**OUT-DETECT-07 — Bulgusuz durum.** Tanımlı bir kalıp yoksa bu açıkça söylenmiş ve sırf rapor dolsun diye bulgu icat edilmemiş mi?

## Son kontrol

**FINAL-01 — Uygulanabilir tüm kontroller.** Kullanıcıya yanıt vermeden önce uygulanabilir tüm kontroller **GEÇTİ** veya **UYGULANAMAZ** mı? Herhangi bir **KALDI** sonucu varsa önce taslağı veya bulgu raporunu düzelt.

**FINAL-02 — Kaynakla tutarlılık.** Bu eval nedeniyle `SKILL.md` içinde olmayan yeni bir yasak, stil tercihi veya sayısal kota uygulanmış mı? Uygulandıysa kaldır.

**FINAL-03 — Aynı yazar testi.** Düzenlenmiş metni okuyan kişi, bunun hâlâ aynı yazarın metni olduğunu makul biçimde hisseder mi?

**FINAL-04 — Keskin meslektaş testi.** Metin, hedef bağlamına uygun keskin bir Türkçe editör veya meslektaşa doğal gelir mi?
