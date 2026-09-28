## Upstream sync

- From: `<!-- önceki .upstream.json SHA -->`
- To: `<!-- incelenen upstream SHA -->`
- Sync dalı: `sync/upstream-<short-sha>`

### Commit incelemesi

Her upstream commit'i için `uyarla`, `taşı` veya `atla` kararını ve gerekçesini yaz.

- [ ] `<sha>` — karar: `uyarla / taşı / atla` — gerekçe:

### Kontroller

- [ ] Upstream'deki bütün yeni commitleri ve değişen dosyaları inceledim.
- [ ] Semantik davranışı Türkçe kurallar, örnekler ve ritimle uyarladım.
- [ ] Türkçeye özgü dosyaları upstream içeriğiyle ezmedim.
- [ ] `python scripts/check_upstream.py --validate-config`
- [ ] `python scripts/check_upstream.py --self-test`
- [ ] `python scripts/check_turkish_surface.py --self-test`
- [ ] `python scripts/check_turkish_surface.py`
- [ ] `python scripts/build_plugin.py --check`
- [ ] Gerekliyse Türkçe eval vakalarını güncelledim.
- [ ] `.upstream.json` yalnızca bu PR'da incelenen son upstream SHA'ya ilerletildi.
- [ ] `UPSTREAM.md` içindeki baseline aynı SHA ile güncellendi.
