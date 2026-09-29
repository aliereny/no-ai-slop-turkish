# PAT-29 için odaklı değerlendirme

Bu dokuz vaka, genel bir adın gereksiz olduğu yeri, işlevsel kullanımını ve düzenlemenin anlam sınırını sınar. Girdiler ve beklentiler `cases.jsonl` içindedir. İki pozitif vaka skill'deki örnek cümleyi kopyalamaz; iade akışı ve bağlantı geçişi bağlamlarını kullanır.

## Vakalar ve geçme ölçütleri

| Vaka | Sınanan ayrım | Geçme ölçütü |
| --- | --- | --- |
| `PAT-29-pos-01` | Aynı bilgiyi üç forma yazmayı “ele alınması gereken unsur” diye anlatma | PAT-29 bulunmalı; öneri tekrar girilen bilgileri ve gelecek haftaki planı korumalı. |
| `PAT-29-pos-02` | 404 hatasını “çözmemiz gereken nokta” içine koyma | PAT-29 bulunmalı; 404 ve henüz hazır olmayan yönlendirmeler doğrudan anlatılmalı, neden uydurulmamalı. |
| `PAT-29-neg-01` | Üç etkeni “unsur” altında gruplama | PAT-29 bulunmamalı; gerçek sınıflandırma korunmalı. |
| `PAT-29-neg-02` | Genel adın gözlemci ifadenin parçası olması | Yalnız PAT-18 bulunmalı; aynı ifade PAT-29 diye yeniden sayılmamalı. |
| `PAT-29-neg-03` | “Konu” ile gündem, “iki nokta” ile açık soruları belirtme | PAT-29 bulunmamalı; işlevsel üst adlar silinmemeli. |
| `OVL-14-29-01` | Genel adın soyut tamlama zincirinde bulunması | PAT-14 bulunmalı; aynı isim yığını PAT-29 diye tekrar raporlanmamalı. |
| `OVL-18-29-independent-01` | Ayrı cümlelerde gözlemci dolgu ve boş genel ad | PAT-18 ve PAT-29 ayrı alıntılarla bulunmalı; iki bağımsız sorun tek bulguya indirilmemeli. |
| `QUALITY-specificity-no-inference-01` | Özgün düşük gecikme cümlesini düzenleme | Düşük gecikme iddiası kalmalı. “Sorun/darboğaz/fırsat”, sayı, önceki sürümle kıyas veya neden eklenmemeli. |
| `QUALITY-specificity-supported-01` | Kaynakta ölçülmüş darboğazı koruma | Genel ad kaldırılırken darboğaz sınıfı, banka beklemesi, %80 ve cuma denemesi korunmalı. Çözüm veya kazanç icat edilmemeli. |

Son iki vaka birlikte değerlendirilir: somutlaştırmak için kategori uydurmak da kaynakta açıkça belirtilen kategoriyi silmek de hatadır. Tek bir örnek cümleye birebir eşleşme aranmaz; anlamı koruyan doğal alternatifler kabul edilir.

## Yerel canlı koşum

Pro aboneliğiyle giriş yapılmış Codex CLI'ın bulunduğu ortamda:

```sh
python3 scripts/eval_runner.py run --output eval-results/pat-29.jsonl --timeout 600 \
  --case-id PAT-29-pos-01 --case-id PAT-29-pos-02 \
  --case-id PAT-29-neg-01 --case-id PAT-29-neg-02 --case-id PAT-29-neg-03 \
  --case-id OVL-14-29-01 --case-id OVL-18-29-independent-01 \
  --case-id QUALITY-specificity-no-inference-01 \
  --case-id QUALITY-specificity-supported-01

python3 scripts/eval_runner.py grade --output eval-results/pat-29.jsonl \
  --report eval-results/pat-29-report.json > /dev/null
```

Bu kısmi koşumda diğer 148 vakanın `pending` kalması beklenir. Bu yüzden burada `--strict` kullanılmaz. Corpus veya skill değişirse yeni bir çıktı dosyası adı seçin.

## İnceleme

Tespitlerde başlık, alıntı, yanlış pozitif ve çakışma kararını; düzenlemelerde girdiyle çıktı arasındaki iddia farkını yukarıdaki ölçütlerle karşılaştırın. `must_not_add` ve `acceptable_direction` semantik beklentilerdir; runner bunları otomatik olarak doğrulamıyor. Alıntının uygunluğu ve son iki vakadaki sınıf/neden/ölçüm korunumu gerekçeli manuel karar ister.

CI corpus yapısını ve runner mantığını sınar. Canlı yanıtlar üretilip incelenmeden bu vakaların model tarafından geçildiği sonucuna varılmaz.
