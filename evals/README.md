# Türkçe eval corpus'u

Bu dizin, `skills/no-ai-slop-tr/SKILL.md` ve `skills/no-ai-slop-tr/eval.md` için davranışsal regresyon corpus'udur.

Amaç belirli bir "doğru cümle" üretmek değil; skill'in şu sözleşmeleri koruyup korumadığını ölçmektir:

1. Tanımlı slop kalıbını doğru adla yakalamak.
2. Aynı yüzey biçiminin meşru kullanımını yanlış pozitif olarak işaretlememek.
3. Çakışan kalıplarda en spesifik sınıflandırmayı seçmek ve aynı sorunu çift raporlamamak.
4. Düzenleme sırasında anlamı, somut bilgiyi, kip/görünüş nüansını ve yazarın sesini korumak.
5. Türkçe olmayan girdilerde dil kapsamını uygulamak.

## Dosya yapısı

- `cases.jsonl`: Kısa ve orta uzunlukta atomik vakaların canonical kaynağı.
- `fixtures/long-form/`: Paragraf ve metin düzeyinde ses, ritim ve doğallık testleri.

Corpus sürüm 1 hedefi **140 atomik vaka**dır:

- PAT-01–PAT-28 için 4 vaka: 2 pozitif + 2 zor negatif = 112
- 12 overlap/sınıflandırma vakası
- 8 dil kapsamı vakası
- 8 çapraz kalite vakası

Uzun metin fixture'ları bu 140 atomik vakanın dışında tutulur.

## Vaka kimlikleri

Kimlikler kararlı olmalıdır. Bir vaka anlamını değiştirecek kadar yeniden yazılacaksa eski ID farklı bir test anlamına gelecek şekilde sessizce yeniden kullanılmamalıdır.

Önerilen biçimler:

- `PAT-10-pos-01`
- `PAT-10-neg-02`
- `OVL-05-06-18-01`
- `LANG-tr-tech-01`
- `QUALITY-voice-01`

Bu kimlikler issue, commit ve regresyon raporlarında doğrudan referans olarak kullanılabilir.

## JSONL şeması

Her satır tek bir JSON nesnesidir. Zorunlu alanlar:

- `id`: Kararlı vaka kimliği.
- `mode`: `detect`, `edit` veya `scope`.
- `register`: Metnin bağlamı/üslup kaydı. Örnekler: `editorial`, `marketing`, `technical`, `business`, `academic`, `legal`, `personal`.
- `patterns`: Vakanın hedeflediği pattern ID'leri. Negatif veya kapsam vakalarında boş olabilir.
- `input`: Modele verilecek Türkçe ya da kapsam testi girdisi.
- `expect`: Davranışsal beklentiler.
- `notes`: Vakanın neden corpus'ta olduğunu açıklayan kısa not.

### Tespit modu beklentileri

Tespit vakalarında `expect` şu alanlardan gerekenleri kullanır:

- `must_find`: Raporlanması gereken PAT ID'leri.
- `must_not_find`: Raporlanmaması gereken PAT ID'leri.
- `evidence`: Bulguyu destekleyen kısa yüzey ifadeleri.
- `must_not_claim_ai_authorship`: AI yazarlığı iddiasının yasak olduğunu belirtir.
- `must_not_score`: Slop yüzdesi/skoru verilmemesi gerektiğini belirtir.

Örnek:

```json
{"id":"PAT-10-neg-01","mode":"detect","register":"technical","patterns":[],"input":"Önbellek devredeyken istek süresi 80 ms. Bununla birlikte önbellek kaçırıldığında süre 240 ms'ye çıkıyor.","expect":{"must_find":[],"must_not_find":["PAT-10"]},"notes":"Bununla birlikte gerçek karşıtlık kuruyor; yüzey biçimi tek başına slop değildir."}
```

### Düzenleme modu beklentileri

Düzenleme vakaları exact-output testi yapmaz. Aynı girdinin birden fazla iyi düzenlemesi olabilir. Bunun yerine:

- `must_change`: Kaynakta sorunlu olup düzenlemede aynı işlevle kalmaması gereken öğeler.
- `must_preserve`: Anlam, bilgi, aktör, zaman, ton veya karakter açısından korunması gereken öğeler.
- `must_not_add`: Kaynakta bulunmayan ve icat edilmemesi gereken bilgi türleri.
- `acceptable_direction`: Düzenlemenin semantik yönünü tarif eden kısa açıklama.
- `must_keep_register`: Metnin üslup düzeyinin korunması gerektiğini belirtir.

Exact bir örnek çıktı yalnızca dokümantasyon amacıyla verilebilir; test oracle'ı sayılmaz.

### Dil kapsamı beklentileri

`scope` vakalarında:

- `should_run`: Skill'in edit/detect akışını çalıştırıp çalıştırmaması.
- `reason`: Ana anlatım dili üzerinden verilen gerekçe.

Kelime oranı tek başına oracle değildir. Kod, marka, ürün adı ve teknik terimler içeren ağırlıklı Türkçe metinler kapsam içidir.

## Pozitif ve zor negatif ilkesi

Her PAT için en az iki pozitif ve iki negatif vaka vardır.

Pozitiflerin biri açık, diğeri gerçek hayatta görülebilecek kadar ince olmalıdır.

Negatiflerin biri aynı yüzey biçimini **meşru işlevle** kullanmalıdır. Örneğin:

- Gerçek karşıtlık kuran "Bununla birlikte".
- Aktörün bilinmediği doğal edilgen yapı.
- Akademik bağlamda yerinde "-maktadır" kullanımı.
- Gerçek üç özelliği sayan üçlü liste.
- Açık gönderimli "Bu durum".

İkinci negatif mümkünse hedef pattern'e benzeyen fakat başka bir kategoriye ait bir vaka olmalıdır. Böylece corpus yalnızca recall değil precision ve sınıflandırmayı da ölçer.

## Çakışma kuralları

Overlap vakalarında `must_find` kadar `must_not_find` de önemlidir.

Özellikle şu ayrımlar korunur:

- PAT-05 / PAT-06 / PAT-18: yorum / önem şişirme / gözlemci dolgu.
- PAT-11 / PAT-12 / PAT-14: bürokratik isimleştirme / edilgenlik sislemesi / soyut isim yığılması.
- Tek bir dil parçasındaki aynı işlev iki farklı pattern adıyla raporlanmaz.
- Aynı cümlede bağımsız iki sorun varsa ayrı bulgular kabul edilir.

## Tür dağılımı

Atomik corpus tek bir internet yazısı türüne aşırı uyum sağlamamalıdır. Hedef dağılım yaklaşık olarak:

- %20 ürün/pazarlama
- %20 blog/editoryal
- %15 teknik
- %15 iş/e-posta
- %15 akademik/rapor
- %10 kişisel/sosyal
- %5 hukuk/resmî

Bu oranlar katı kota değil, corpus dengesini izlemek için kılavuzdur.

## Uzun metin fixture'ları

Uzun fixture'lar tek pattern recall testinden çok bütünsel davranışı ölçer:

- Yazarın sesi ve karakterli ritmi korunuyor mu?
- Metin gereksiz yere sıkıştırılıyor mu?
- Kişisel anı/yan not sırf "verimli" olsun diye siliniyor mu?
- Metin gereksiz kurumsallaştırılıyor veya samimileştiriliyor mu?
- Kaynakta olmayan sayı, neden, örnek veya görüş ekleniyor mu?
- İngilizce iskelet Türkçe kelimelerle sürdürülüyor mu?

Her fixture kendi başlığında kısa oracle notları taşır.

## Regresyon sözleşmesi

Corpus'un amacı ilk günden yapay bir "%100 başarı" üretmek değildir.

İş akışı:

1. Mevcut skill üzerinde baseline al.
2. Yeni bir gerçek hata bulunduğunda önce bunu yeniden üreten vaka ekle.
3. Kuralı `SKILL.md` veya `eval.md` içinde düzelt.
4. Tüm corpus'u yeniden çalıştır.
5. Daha önce geçen bir vaka bozulursa bunu regresyon olarak incele.

Bir pattern davranışı bilinçli olarak değiştiriliyorsa ilgili corpus vakaları aynı PR'da açık gerekçeyle güncellenmelidir.

## Runner ve v1.0 kalite kapısı

`scripts/eval_runner.py` canonical `cases.jsonl` ve 8 uzun metin fixture'ını kullanır. Standart kütüphane dışında bağımlılığı yoktur.

```sh
python scripts/eval_runner.py validate
python scripts/eval_runner.py self-test
codex login
codex login status # ChatGPT ile giriş yapıldığını doğrulayın
python scripts/eval_runner.py run --model MODEL_ID --output eval-results/outputs.jsonl
python scripts/eval_runner.py grade --output eval-results/outputs.jsonl --report eval-results/report.json
```

Yerelde varsayılan sağlayıcı `codex`'tir: ChatGPT Pro/Plus oturumunuzla açtığınız Codex CLI üzerinden `codex exec` çalıştırır; API anahtarı veya ayrı API faturalaması gerekmez. CLI ve oturumun bilgisayarınızda kurulmuş olması gerekir. `MODEL_ID`, `codex exec --model` için hesabınızda erişilebilir sabit bir model kimliğidir. Her vaka izole, geçici bir dizinde, salt okunur sandbox'ta ve ek araç kullanmama talimatıyla çalışır. Bu yol GitHub Actions üzerinde ChatGPT oturum belirteci saklamaz. ChatGPT kullanım limitleri geçerlidir.

`run`, gerçek skill talimatlarını ve `eval.md` dosyasını modele gönderir; sağlayıcıyı, istenen model kimliğini, API yanıtı veya Codex oturum kimliğini, zamanı, corpus/skill parmak izini ve çıktıyı her vaka için JSONL'ye yazar. Codex CLI dönen kesin model revizyonunu bildirmiyorsa `model` alanı istenen kimliktir. Aynı sağlayıcı, model ve parmak iziyle kesilen çalışmayı devam ettirir; sürüm değişmişse yeni dosya gerekir. Çıktılar kullanıcı metinlerini de içerebilir; artifact erişimini buna göre yönetin. Bir model çağrısında hata oluşursa eldeki kayıtlar korunur ve iş başarısız olur.

İlk çağrı başarısız olursa runner, Codex JSON olaylarındaki hata nedenini gösterir. Hiç vaka kaydedilmediyse `grade` rapor üretemez; önce `run` hatasını giderip aynı komutu tekrarlayın. Hata model erişimiyle ilgiliyse `codex exec --model MODEL_ID 'Merhaba de'` ile model kimliğini yerelde sınayın.

API ile çalıştırmak isterseniz `OPENAI_API_KEY=... python scripts/eval_runner.py run --provider api --model MODEL_ID --output eval-results/api-outputs.jsonl` komutunu kullanın. Bu ayrı API kullanımına tabidir.

`grade` tespit başlıklarındaki kalıp adlarını `SKILL.md` içindeki 28 kalıbın sırasıyla eşler; beklenen/beklenmeyen bulguları ve düzenlemedeki birebir kalan sorunlu ifadeleri kontrol eder. Alıntının uygunluğu, gerçek yanlış pozitifler, anlam, üslup, yeni iddia ve uzun metin oracle'ları insan incelemesi ister. Otomatik kontrol geçse bile durum `review` kalır. `scope` vakaları da ana anlatım diline göre elle değerlendirilir. Başlıksız veya farklı adlandırılmış bulgular ayrıca incelenmelidir.

İnceleme dosyası bir JSON nesnesidir: `{"PAT-01-pos-01": {"verdict": "pass", "note": "Alıntı ve sınıflandırma doğru."}}`. Her vaka için gerekçeli `pass` veya `fail` girin. Ardından:

```sh
python scripts/eval_runner.py grade --output eval-results/outputs.jsonl --review eval-results/reviews.json --report eval-results/report.json --strict
```

`--strict`, 148 vakanın tamamında gerekçeli insan onayı ve sıfır otomatik hata ister; `fail`, `review` veya `pending` varsa sıfırdan farklı çıkar. Bu eşik v1.0 için önerilen kalite kapısıdır. Hataları vaka ID'siyle düzeltip aynı modeli ve tüm corpus'u tekrar çalıştırın. CI yalnızca corpus sözleşmesini ve runner mantığını ağsız doğrular; canlı sonuçları varmış gibi göstermez.

GitHub'daki **Model eval baseline** workflow'u isteğe bağlı API yoludur; bunun için depoya `OPENAI_API_KEY` secret'ı eklemek gerekir. Genel/açık kaynak GitHub runner'ına ChatGPT oturum dosyanızı veya belirtecinizi koymayın. Pro aboneliğinizle test için yukarıdaki yerel Codex yolunu kullanın. Son insan incelemesi yerel `--review` ile tamamlanır.
