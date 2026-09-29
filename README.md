# No AI Slop Türkçe

Türkçe metinlerdeki AI slop kalıplarını azaltırken yazarın kişisel sesini koruyan bir düzenleme ve tespit skill'i.

[petergyang/no-ai-slop](https://github.com/petergyang/no-ai-slop) tabanlıdır; ancak İngilizce kuralların birebir çevirisi değildir. Türkçenin sözdizimi, resmiyet kipleri, edilgenlik kullanımı, bürokratik anlatımı ve çeviri kokan cümle yapılarına göre yeniden tasarlanmıştır.

## Ne işe yarıyor?

No AI Slop Türkçe iki modda çalışır:

- **Düzenle:** Metindeki mekanik, şişirilmiş veya yapay duran kalıpları temizlerken anlamı, somut ayrıntıları ve yazarın kişisel sesini korur.
- **Tespit et:** Metni yeniden yazmadan hangi tanımlı kalıpların bulunduğunu, kısa kanıtlarla ve düzeltme yönüyle bildirir.

Araç yalnızca ağırlıklı olarak Türkçe metinler için tasarlanmıştır. Kod, marka adı, ürün adı veya kısa yabancı dil alıntıları içeren Türkçe metinler kapsam içindedir.

## Neden Türkçe için ayrı bir sürüm?

Türkçedeki AI slop yalnızca İngilizce klişelerin çevrilmiş hâli değildir.

Türkçe metinlerde özellikle şu sorunlar farklı biçimde ortaya çıkar:

- gereksiz resmî kipler ve sürekli “-maktadır/-mektedir” kullanımı,
- “inceleme gerçekleştirmek” gibi bürokratik isimleştirmeler,
- aktörü gereksiz yere gizleyen edilgen yapılar,
- “Bu bağlamda”, “Bununla birlikte”, “Öte yandan” gibi mekanik geçişler,
- “karşımıza çıkıyor”, “öne çıkıyor”, “gözler önüne seriyor” gibi gözlem ve yorum dolguları,
- İngilizce cümle iskeletinin Türkçe kelimelerle korunması,
- “araç / çözüm / platform / sistem” gibi gereksiz eş anlamlı döndürme.

Bu repo bu davranışları Türkçenin kendi bağlamında değerlendirir. Aynı yüzey biçimini her zaman hata saymaz; gerçek karşıtlık, akademik resmiyet, işlevsel edilgenlik veya doğal teknik jargon gibi meşru kullanımları korumaya çalışır.

## Kurulum

### ChatGPT, Codex veya uyumlu bir coding agent

Aşağıdaki isteği yapıştırın:

~~~text
https://github.com/aliereny/no-ai-slop-turkish deposundaki /no-ai-slop-tr skill'ini global olarak kur.
~~~

### npx

~~~sh
npx skills add aliereny/no-ai-slop-turkish --skill no-ai-slop-tr --global --yes
~~~

## Kullanım

### Metni düzenleme

~~~text
/no-ai-slop-tr

Bu metni düzenle:

(metniniz)
~~~

Skill gereken en küçük etkili müdahaleyi yapar ve tam düzenlenmiş metnin ardından kısa bir **Neleri değiştirdim?** bölümü verir.

### AI slop tespiti

~~~text
/no-ai-slop-tr

Bu metindeki AI slop kalıplarını tespit et:

(metniniz)
~~~

Tespit modunda metin yeniden yazılmaz. Her bulgu tanımlı kalıp adıyla, kısa bir alıntıyla ve düzeltme yönüyle verilir.

## Örnek

### Önce

> Bu bağlamda, yeni önbellek sistemi sayfaların daha hızlı yüklenmesini mümkün hale getiriyor. Bununla birlikte sistem, kullanıcı deneyiminin iyileştirilmesi açısından önemli bir rol oynuyor.

### Sonra

> Yeni önbellek sistemiyle sayfalar daha hızlı yükleniyor.

Bu örnekte gereksiz geçiş ifadeleri, “mümkün hale getirmek” zinciri ve somut bilgi taşımayan önem şişirmesi temizlenir. Kaynakta olmayan yeni bir neden, sayı veya sonuç eklenmez.

## Hangi kalıpları yakalıyor?

Skill şu anda 30 kalıbı değerlendirir. Bunların bir bölümü genel AI yazım davranışlarının Türkçe karşılıkları, bir bölümü ise Türkçeye özgü yapılardır.

| Grup | Örnek kalıplar |
| --- | --- |
| Yapay vurgu ve giriş | Sahte karşıtlık, konuya girmeyi geciktiren girişler, yapay içgörü girişleri, iki noktayla dramatik açıklama |
| Şişirme ve yorum | Göstermeden yorumlayan analiz, önem şişirme, okuru yönlendiren üst-anlatım, belirsiz kaynak gösterme |
| Türkçeye özgü bürokratik dil | Bürokratik isimleştirme, edilgenlik sislemesi, soyut isim yığılması, resmî kip otomatiği |
| Mekanik Türkçe | Mekanik geçiş bağlaçları, gösterici zamir zinciri, geciken adlandırma, yapay gözlem dili, genel adla belirsizleştirme, çeviri kokan cümle iskeleti |
| Ritim ve kapanış | Gereksiz eş anlamlı döndürme, dramatik parçalama, robotik ritim, retorik kurulumlar, yapay vurucu kapanış |
| Biçim | Gereksiz özet-tekrar kapanışları, biçimlendirme slop'u, dekoratif uzun çizgi kullanımı |

Tam kalıp listesi, karar kuralları ve örnekler için [SKILL.md](skills/no-ai-slop-tr/SKILL.md) dosyasına bakın.

## Ne yapmaz?

No AI Slop Türkçe:

- bir metnin AI tarafından yazılıp yazılmadığını tahmin etmez,
- “%87 AI” gibi bir skor üretmez,
- her uzun veya resmî cümleyi kötü saymaz,
- “Bu bağlamda” veya “-maktadır” gibi yüzey biçimlerini bağlamdan bağımsız yasaklamaz,
- metni tek tip, kurumsal veya steril Türkçeye dönüştürmez,
- kaynak metinde bulunmayan iddia, istatistik, örnek, aktör veya gerekçe uydurmaz,
- Türkçe olmayan bir metni kullanıcı açıkça istemedikçe çevirmeye veya Türkçe kurallarla düzenlemeye çalışmaz.

## Nasıl çalışıyor?

Ana davranış sözleşmesi iki dosyada tanımlanır:

- [SKILL.md](skills/no-ai-slop-tr/SKILL.md): düzenleme ilkeleri, iki çalışma modu ve 30 kalıbın karar kuralları,
- [eval.md](skills/no-ai-slop-tr/eval.md): anlam korunumu, kişisel ses, Türkçe doğallık, false-positive kontrolü ve çıktı sözleşmesi için kalite kapısı.

Davranışsal regresyon corpus'u [evals/](evals/) altında tutulur. Corpus, 30 kalıp için pozitif ve zor negatif örneklerin yanı sıra çakışma, dil kapsamı ve kalite vakalarını içerir. Uzun metin fixture'ları kişisel ses, teknik jargon, akademik kayıt, hukukî resmiyet ve benzeri bütünsel davranışları test eder.

## Repo yapısı

- [skills/no-ai-slop-tr/SKILL.md](skills/no-ai-slop-tr/SKILL.md): ana skill tanımı
- [skills/no-ai-slop-tr/eval.md](skills/no-ai-slop-tr/eval.md): self-eval kalite kapısı
- [evals/cases.jsonl](evals/cases.jsonl): atomik davranışsal regresyon vakaları
- [evals/fixtures/long-form/](evals/fixtures/long-form/): uzun metin testleri
- [.codex-plugin/plugin.json](.codex-plugin/plugin.json): ChatGPT ve Codex plugin metadata'sı
- [scripts/build_plugin.py](scripts/build_plugin.py): plugin paketleme ve doğrulama
- [UPSTREAM.md](UPSTREAM.md): upstream senkronizasyon notları

## Geliştirme kontrolleri

PR açmadan önce Türkçe kullanıcı yüzeyi ve plugin paketi yerelde doğrulanabilir:

~~~sh
python scripts/check_turkish_surface.py --self-test
python scripts/check_turkish_surface.py
python scripts/build_plugin.py --check
~~~

`check_turkish_surface.py`, eski skill kimliklerinin veya upstream'den kalan İngilizce kullanıcı arayüzü ifadelerinin Türkçe yüzeye sızmasını engeller. Ayrıca plugin manifest kimliğini ve iki `openai.yaml` dosyasının birebir aynı kalmasını denetler. GitHub Actions aynı kontrolleri her pull request ve `main` push'unda otomatik çalıştırır.

## Upstream ile ilişki

Bu proje [petergyang/no-ai-slop](https://github.com/petergyang/no-ai-slop) tabanlı bağımsız bir Türkçe uyarlamadır. Upstream'in paketleme ve repo mimarisi mümkün olduğunca paralel tutulurken dil kuralları, değerlendirme sözleşmesi ve corpus Türkçe için ayrı geliştirilir.

Upstream senkronizasyon yaklaşımı ve takip edilen commit bilgisi için [UPSTREAM.md](UPSTREAM.md) dosyasına bakın.

## Gizlilik ve kullanım koşulları

- [Gizlilik](PRIVACY.md)
- [Kullanım Koşulları](TERMS.md)

## Lisans

MIT. Orijinal telif ve lisans bildirimi [LICENSE](LICENSE) dosyasında korunur.
