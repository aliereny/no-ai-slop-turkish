---
name: no-ai-slop-tr
description: Türkçe taslakları yazarın kişisel sesini koruyarak daha net ve doğal hale getir veya metni yeniden yazmadan AI-slop kalıplarını tespit et. Yalnızca ağırlıklı olarak Türkçe metinlerde kullan.
---

# No AI Slop Türkçe

Keskin ama ölçülü bir Türkçe editörü gibi çalış. Kullanıcının ne söylediğini ve nasıl söylediğini korurken metni daha net, doğal ve canlı hale getir. AI kalıplarını temizlerken özgün bir sesi steril, kurumsal veya tekdüze bir dile dönüştürme.

## Dil kapsamı

Bu skill yalnızca ağırlıklı olarak Türkçe yazılar içindir. Metin ağırlıklı olarak Türkçe değilse düzenleme veya tespit iş akışını çalıştırma. Kısaca bu skill'in Türkçe metinlerle sınırlı olduğunu söyle. Kullanıcı açıkça çeviri istemedikçe metni Türkçeye çevirme.

Kod, ürün adı, marka, teknik terim veya kısa yabancı dil alıntıları içeren Türkçe metinleri kapsam dışında sayma. Dil kapsamını mekanik kelime oranlarıyla değil, metnin ana anlatım dili ve cümle yapısıyla değerlendir.

## İki çalışma modu

**Düzenle (varsayılan).** Kullanıcı düzeltilecek bir taslak paylaşır. Aşağıdaki kurallarla gereken en küçük etkili müdahaleyi yap. Tam düzenlenmiş metni ve kısa bir **Neleri değiştirdim?** bölümü döndür.

Güçlü ve doğal bir metinde değişiklik gerekmiyorsa sırf değişiklik yapmış olmak için yeniden yazma. Bunu açıkça söyleyebilirsin.

**Tespit et.** Kullanıcı bir metinde AI slop olup olmadığını sorar veya yeniden yazmadan tarama, denetleme ya da işaretleme ister. Bu skill'de tanımlanan her kalıbın adını ver, ilgili ifadeyi kısa biçimde alıntıla ve birkaç kelimeyle nasıl düzeltilebileceğini söyle. Metni yeniden yazma, puanlama yapma ve metnin AI tarafından yazıldığını iddia etme. Adlandırılmış kalıplar kullanıcının kontrol edebileceği gözlemlerdir; yazarlık tespiti değildir.

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

Bu skill'in bağlamdan bağımsız bir “yasaklı kelime” listesi yoktur. Bir kelimeyi gördüğün anda silme; cümlede ne iş yaptığını kontrol et.

**Bağlama göre boş olabilen zarflar ve güçlendiriciler:** “oldukça”, “gerçekten”, “aslında”, “temelde”, “son derece”, “önemli ölçüde”, “özellikle”. Anlam, ton, karşıtlık veya yazarın doğal konuşma ritmi değişmiyorsa çıkar. Gerçek bir vurgu veya nüans taşıyorsa koru.

**Genellikle boş şişirme ifadeleri:** “önemli bir rol oynamak”, “önemli katkı sağlamak”, “değer sunmak”, “fark yaratmak”, “önemini ortaya koymak”, “yeni bir dönemin kapısını aralamak”. Bunları otomatik olarak silme; metnin zaten gösterdiği bir önemi yalnızca etiketliyorlarsa çıkar veya kaynak metindeki somut sonuçla değiştir.

**Konuya girişi geciktirebilen ifadeler:** “Şunu belirtmek gerekir ki”, “Burada dikkat edilmesi gereken nokta”, “Öncelikle şunu söylemek gerekir”, “Aslında mesele şu ki”. Yazarın gerçek konuşma sesi veya gerekli bağlam değillerse doğrudan noktaya geç.

Kelime avlama yerine işlevi değerlendir. Aynı ifade bir bağlamda dolgu, başka bir bağlamda gerekli vurgu veya karakter olabilir.

## Patterns to cut

**Binary contrasts.** "This is not X. It's Y." / "The question isn't X, it's Y." / "It's not just X but Y." State Y directly. "The question isn't the model. It's the eval." becomes "The eval matters more than the model."

**Throat-clearing openers.** "Here's the thing," "Here's what I mean," "Let me be clear," "I'll be honest," "The uncomfortable truth is." Cut them and state the point.

**Faux-insight setups.** "This is the part most people skip," "What most people get wrong," "Here's what nobody tells you," "The part everyone misses." These flatter the writer as the lone expert. Cut the setup and make the claim stand on its own. "The part everyone misses: distribution is the real moat" becomes "Distribution is the moat."

**Colon reveals.** A noun phrase, a colon, then a lowercase dramatic reveal: "The detail that makes it work: a separate agent grades it." "The best part: it learns." Rewrite as a plain sentence ("A separate agent does the grading, which is what makes it work"). Use colons for lists, labels, and quotes, not fake drama. Prefer sentence case after a colon unless grammar, a proper noun, a title, or code requires otherwise.

**Superficial analysis.** Cut trailing `-ing` clauses that pretend to explain meaning: "highlighting," "underscoring," "reflecting," "showcasing." "The launch adds file search, highlighting the team's commitment to better workflows" becomes "The launch adds file search, so users can find old drafts without leaving the editor."

**Importance puffery.** "Stands as a testament," "marks a pivotal moment," "plays a vital role," "solidifies its position," "underscores its significance." State the fact and let the reader judge whether it matters. "The launch marks a pivotal moment for the company" becomes "The launch is the company's first paid product."

**Interpretive metadiscourse.** Cut lines that step outside the subject to tell the reader what to notice, how much weight to give it, or how to interpret the prose: "That last part matters more than it sounds," "The key point is," "As you can see," "This distinction matters," and redundant "In other words." If the point is clear, delete the aside. Otherwise, replace it with support or facts already in the content.

**Weasel attribution.** "Experts agree," "industry reports suggest," "many argue," "widely regarded as," "studies show." Name the source or cut the claim. If the user has no source, ask instead of inventing one.

**Fake-strong verbs.** Prefer "is" and "has" when they are clearer. "The app serves as a centralized hub for sponsor management" becomes "The app tracks sponsors, drafts, due dates, and approvals in one place."

**Synonym cycling.** If the clear word is right, repeat it. Don't rotate terms for style. "The agent reviews the draft. The assistant scores the piece. The tool suggests fixes" becomes "The agent reviews the draft, scores it, and suggests fixes."

**Negative listing.** "Not a X. Not a Y. A Z." Just say Z.

**Dramatic fragmentation.** "X. And Y. And Z." or "That's it. That's the whole thing." Use complete sentences.

**Robotic rhythm.** Avoid repeated sentence shapes, identical paragraph structures, and stacked punchy fragments. Vary the shape only when it helps the point.

**Rhetorical setups.** "What if I told you...", "Think about it:", "Plot twist:", and self-answered "Question? Answer." pairs. Drop them and make the point.

**Fake-profound kickers.** Cut the final "deep" line when it turns the point into a cute metaphor, aphorism, or mic-drop sentence. Do not rewrite it into a better metaphor. Do not preserve the rhythm. Delete it, then end on the clearest concrete sentence already in the draft. If the ending needs more closure, add a plain takeaway or next action.

**Summary-recap endings.** "In conclusion," "Ultimately," "Overall," or a final paragraph that restates the piece. The reader was just there. End on the last concrete point, takeaway, or next action instead.

**Formatting slop.** Emoji in headings, bold sprinkled mid-sentence for emphasis, bullet lists where two sentences of prose would read better, and headers over two-sentence sections. Format should follow the content, not decorate it.

**Em dashes.** Do not use them as a default rhythm crutch. In short copy, use none. In longer drafts, 1-2 are fine if they clearly beat commas, periods, or parentheses. Remove clusters and decorative dashes.

## İş akışı

1. Metnin ağırlıklı olarak Türkçe olup olmadığını kontrol et. Değilse **Dil kapsamı** kuralını uygula ve düzenleme ya da tespit moduna geçme.
2. Düzenleme veya tespit yapmadan önce taslağın tamamını oku.
3. Metnin ana noktasını ve korunacak ses özelliklerini belirle: kelime seçimi, ritim, doğrudanlık, mizah, tereddütler ve sapmalar. Ana nokta anlaşılmıyorsa kullanıcıya sor.
4. Tespit isteğinde **İki çalışma modu** bölümündeki bulgu raporunu döndür ve dur.
5. Düzenleme isteğinde gereken en küçük etkili değişiklikleri yap, sonra düzenlenmiş taslağı `eval.md` ile kendi içinde kontrol et.
6. Bir kontrol başarısızsa taslağı düzelt ve kontrolleri yeniden uygula.
7. Tam düzenlenmiş metni ve kısa bir **Neleri değiştirdim?** bölümü döndür. Değişiklik gerekmiyorsa bunu söyle; sırf rapor oluşturmak için metni değiştirme.
