# Upstream ile ilişki

Bu depo, [petergyang/no-ai-slop](https://github.com/petergyang/no-ai-slop) projesinin Türkçeye özel bir fork'udur.

## Mevcut taban

- Upstream deposu: `petergyang/no-ai-slop`
- Takip edilen taban commit: `000650b156983f5159695b441477f4e63b25dc85`
- Fork deposu: `aliereny/no-ai-slop-turkish`

## Paralellik sözleşmesi

1. Upstream'in üst seviye repo yapısını, plugin paketleme akışını ve release workflow'unu pratik olduğu ölçüde paralel tut.
2. Plugin/paket kimliği olarak `no-ai-slop-turkish` kullan.
3. Skill kimliği olarak `no-ai-slop-tr`, kullanıcıya dönük komut olarak `/no-ai-slop-tr` kullan.
4. Skill'i ağırlıklı olarak Türkçe yazılarla sınırla. Türkçe olmayan girdilerde düzenleme/tespit iş akışını çalıştırma.
5. Gelecekteki upstream davranış değişikliklerini Türkçeye özgü kuralların üzerine yazmak yerine anlamsal olarak uyarla.
6. Upstream MIT lisansını ve attribution bilgisini koru.

Türkçe slop taksonomisi, örnekleri ve değerlendirme ölçütleri dile özgü içerik olarak ayrı sürdürülür ve gerektiğinde upstream'den bilinçli biçimde ayrışabilir.
