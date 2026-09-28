# No AI Slop Türkçe — plugin başvurusu

## Konumlandırma

No AI Slop Türkçe, [petergyang/no-ai-slop](https://github.com/petergyang/no-ai-slop) tabanlı Türkçeye özel bir uyarlamadır. Upstream plugin mimarisini mümkün olduğunca paralel tutarken paket kimliğini, skill kimliğini, Türkçe AI slop taksonomisini ve değerlendirme sözleşmesini ayrı geliştirir.

## Kapsam

- Plugin/paket adı: **no-ai-slop-turkish**
- Skill adı ve komutu: **no-ai-slop-tr** / **/no-ai-slop-tr**
- Dil kapsamı: ağırlıklı olarak Türkçe yazılar
- Çalışma modları: düzenleme ve tespit
- Türkçe taksonomi: 28 kalıp
- Davranışsal regresyon corpus'u: pozitif, zor negatif, overlap, dil kapsamı ve kalite vakaları
- Upstream paketleme ve release akışı: pratik olduğu ölçüde paralel

Kod, ürün adı, marka, teknik terim veya kısa yabancı dil alıntıları içeren Türkçe metinler kapsam içindedir. Ağırlıklı olarak Türkçe olmayan girdiler düzenleme veya tespit iş akışına alınmaz.

## Dizin başvurusu kontrolü

Türkçeye özgü taksonomi, self-eval sözleşmesi ve davranışsal eval corpus'u repoda mevcuttur. Önceki “taksonomi ve eval tamamlanana kadar başvurma” koşulu bu repo açısından karşılanmıştır.

Public plugin dizinine gönderimden önce:

1. **python scripts/build_plugin.py --check** çalıştırılmalı.
2. Üretilen paketin plugin metadata'sı, skill dosyaları ve hukuki bağlantıları son kez kontrol edilmeli.
3. Platformun güncel başvuru ve doğrulama kuralları ayrıca uygulanmalı.

Repo içindeki build kontrolünün başarılı olması, platformun nihai başvuru doğrulamasının yerine geçmez.

## Başlangıç istemleri

1. **@No AI Slop Türkçe Bu metni doğal Türkçeyi ve kişisel sesimi koruyarak düzenle: (metin)**
2. **@No AI Slop Türkçe Bu metindeki AI slop kalıplarını tespit et: (metin)**

## Negatif testler

1. Ağırlıklı olarak İngilizce veya başka bir dilde olan taslakta edit ya da detect modunu çalıştırma. Skill'in Türkçe metinlerle sınırlı olduğunu kısa biçimde belirt ve metni değiştirme.
2. Kullanıcı açıkça çeviri istemedikçe Türkçe olmayan girdiyi Türkçeye çevirme.
3. Tespit modunda AI yazarlığı iddiası veya yapay bir slop yüzdesi üretme.
4. “Bu bağlamda”, “-maktadır” veya edilgen yapı gibi yüzey biçimlerini bağlamdan bağımsız hata sayma.

## Sürüm notu

Sürüm **0.1.0**, bağımsız Türkçe plugin kimliğini, **no-ai-slop-tr** skill'ini, Türkçeye özgü 28 kalıplı taksonomiyi, self-eval kalite kapısını ve davranışsal eval corpus'unu içerir. Kullanıcıya görünen dokümantasyon, gizlilik ve kullanım koşulları da Türkçe ürün yüzeyiyle uyumludur.
