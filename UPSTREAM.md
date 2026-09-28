# Upstream ile ilişki

Bu depo, [petergyang/no-ai-slop](https://github.com/petergyang/no-ai-slop) projesinin Türkçeye özel bir fork'udur. Upstream değişiklikleri doğrudan `main` dalına alınmaz; her değişiklik incelenir ve Türkçe ürüne bilinçli olarak uyarlanır.

## Takip edilen taban

- Upstream deposu: `petergyang/no-ai-slop`
- Upstream dalı: `main`
- Son incelenmiş commit: `000650b156983f5159695b441477f4e63b25dc85`
- Makinece okunabilir kayıt: [`.upstream.json`](.upstream.json)

`.upstream.json` içindeki `tracked_commit`, Türkçe fork'un bilinçli olarak incelediği son upstream commit'i gösterir. Upstream'deki en yeni SHA'yı otomatik olarak bu alana yazmayın. Baseline yalnızca bütün yeni commitler için uyarlama kararı verilip değişiklikler bir sync PR'ında tamamlandıktan sonra ilerletilir.

## Dal modeli

- `main`: Türkçe ürünün ana dalı.
- `upstream-main`: `petergyang/no-ai-slop:main` dalının temiz aynası. Bu dala Türkçe commit atılmaz ve bu dal `main` ile merge edilmez.
- `sync/upstream-<short-sha>`: `main` üzerinden açılan inceleme ve uyarlama dalı.

Temiz aynayı oluşturmak veya güncellemek için:

```bash
git remote add upstream https://github.com/petergyang/no-ai-slop.git
git fetch upstream main
git push origin upstream/main:refs/heads/upstream-main
```

`upstream` remote'u daha önce eklenmişse ilk komutu atlayın. Normal upstream ilerlemesi aynaya fast-forward olarak gönderilir. Upstream geçmişi yeniden yazılmışsa eski aynayı zorla güncellemeden önce farkı inceleyin.

## Değişiklik sınıfları ve dosya eşlemesi

| Upstream dosyası | Fork'taki karşılığı | Karar |
| --- | --- | --- |
| `skills/no-ai-slop/SKILL.md` | `skills/no-ai-slop-tr/SKILL.md` | Anlamı koruyarak Türkçeye uyarla |
| `skills/no-ai-slop/eval.md` | `skills/no-ai-slop-tr/eval.md` | Türkçe değerlendirme ölçütlerine uyarla |
| `skills/no-ai-slop/agents/openai.yaml` | `skills/no-ai-slop-tr/agents/openai.yaml` | Şema değişikliğini taşı, görünen metni Türkçe tut |
| `agents/openai.yaml` | `agents/openai.yaml` | Yapısal metadata değişikliğini taşı, metni Türkçe tut |
| `.codex-plugin/plugin.json` | `.codex-plugin/plugin.json` | Paket şemasını taşı, Türkçe ürün kimliğini koru |
| `scripts/build_plugin.py` | `scripts/build_plugin.py` | Uygulanabilir yapısal düzeltmeyi taşı |
| `.github/workflows/plugin.yml` | `.github/workflows/plugin.yml` | Gerekli CI/release değişikliğini taşı |
| `README.md` | `README.md` | Yalnızca yararlı bilgiyi Türkçe belgeye uyarla |

`evals/**`, `skills/no-ai-slop-tr/**`, `scripts/check_turkish_surface.py`, `scripts/check_upstream.py`, `.upstream.json` ve bu dosyadaki Türkçeye özgü kararlar fork tarafından sahiplenilir. Upstream'de benzer adlı bir dosya belirse bile üzerine yazılmaz; içerik ayrıca incelenir.

Eşleyicide görünmeyen bir dosya `REVIEW` olarak raporlanır. Her değişiklik için şu kararlardan biri yazılır:

- **Uyarla:** Davranış Türkçede de yararlıysa Türkçeye özgü örnek ve kurallarla uygula.
- **Taşı:** Yapısal veya araç değişikliğini anlamını değiştirmeden uygula.
- **Atla:** Türkçe ürüne uygun değilse veya zaten karşılanıyorsa nedenini kaydet.

## Sync prosedürü

1. `python scripts/check_upstream.py` ile yeni commitleri ve dosyaları listeleyin. Script hiçbir dosyayı değiştirmez ve otomatik merge yapmaz.
2. Her upstream commit'i ve değişen dosyayı okuyun. Bilinmeyen dosyalar dahil hiçbirini sessizce atlamayın.
3. `main` dalından `sync/upstream-<short-sha>` oluşturun. Upstream commitlerini bu dala merge etmeyin.
4. Gerekli yapısal düzeltmeleri taşıyın; beceri ve değerlendirme içeriğini Türkçeye anlamsal olarak uyarlayın. Türkçe korpusunu ve yüzey denetleyicisini gerektiğinde güncelleyin.
5. `.github/PULL_REQUEST_TEMPLATE/upstream-sync.md` içindeki her commit için `uyarla / taşı / atla` kararını ve gerekçesini doldurun.
6. `python scripts/check_upstream.py --validate-config`, `python scripts/check_upstream.py --self-test`, `python scripts/check_turkish_surface.py --self-test`, `python scripts/check_turkish_surface.py` ve `python scripts/build_plugin.py --check` komutlarını çalıştırın.
7. Sync PR'ı tamamlanıp kararlar `main`e girdikten sonra `.upstream.json` içindeki `tracked_commit` değerini hedef SHA'ya ilerletin. Bu dosyadaki son incelenmiş commit satırını da aynı değişiklikte güncelleyin.
8. `upstream-main` aynasını güncelleyin. İzleme workflow'u eski upstream takip issue'sunu baseline güncel olduğunda kapatır.

Commit mesajları kısa ve karar odaklı olsun; örneğin `sync: port upstream packaging fix`, `sync: adapt editing rule for Turkish`, `sync: advance reviewed upstream baseline`.

## Otomatik takip ve deneme

`.github/workflows/upstream-check.yml` haftada bir upstream'i kontrol eder; `workflow_dispatch` ile elle de çalıştırılabilir. Yeni değişiklik varsa tek bir açık takip issue'sunu oluşturur veya günceller. Otomasyon upstream kodunu kopyalamaz, branch açmaz ve Türkçe `main`i değiştirmez. Baseline ilerleyince issue'yu kapatır.

Şu an kayıtlı taban upstream `main` ile aynı commit'tedir. Script'i gerçek baseline'a dokunmadan bir commit geriden sınamak için:

```bash
python scripts/check_upstream.py --tracked-commit d30eddb9e04562234f2070b5ee63ca4649d9a05e --json
```

Bu denemede beklenen sonuç `000650b156983f5159695b441477f4e63b25dc85` commit'inin tespit edilmesi ve script'in “upstream geride” çıkış kodu `2` ile bitmesidir. Normal çalıştırmada baseline yalnızca `.upstream.json` dosyasından okunur.
