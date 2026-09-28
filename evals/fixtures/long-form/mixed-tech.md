# Türkçe teknik yazı / karma terminoloji

## Metadata

- Mode: edit
- Register: technical-editorial
- Primary patterns: language scope / PAT-19 false-positive control

## Input

Geçen ay monolith içindeki notification worker'ı ayrı bir service'e taşıdık. İlk hedef "perfect architecture" değildi; deploy sırasında ana API'yi bloklamamasını istiyorduk.

Yeni worker Kafka'dan event okuyor ve başarısız işleri dead-letter queue'ya atıyor. Retry policy şu an 30 saniye, 2 dakika ve 10 dakika. Kodun en kritik parçası aslında fancy değil:

`if attempts >= 3: send_to_dlq(job)`

Bu değişiklikten sonra deploy süresi 14 dakikadan 9 dakikaya indi. Bunun bütün farkı worker'ın yarattığını söyleyemem; aynı hafta Docker image'ını da küçülttük.

## Oracle

- Metin ağırlıklı Türkçedir; İngilizce teknik terimler ve kod kapsam dışı sayılmamalı.
- "İlk hedef ... değildi" gerçek niyet ayrımıdır; PAT-01 diye otomatik kesilmemeli.
- 30 saniye / 2 dakika / 10 dakika ile 14→9 dakika ayrıntıları korunmalı.
- Son paragraftaki nedensellik konusundaki ihtiyat korunmalı; tek nedene indirgenmemeli.
- Yerleşmiş jargon sırf yabancı kökenli diye yapay Türkçeye çevrilmemeli.
