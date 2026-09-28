# Teknik not / doğal jargon

## Metadata

- Mode: edit
- Register: technical
- Primary patterns: precision / false-positive control

## Input

Backend tarafında Go, frontend tarafında React kullanıyoruz. API, kullanıcı izni varsa üçüncü taraf istemcilerin dosya metadata'sını okumasına olanak sağlıyor; dosyanın kendisini döndürmüyor.

Dün cache katmanını açtıktan sonra p50 gecikme 82 ms'den 37 ms'ye indi. Bununla birlikte cache miss olduğunda p95 hâlâ 410 ms. Şimdilik en büyük darboğaz S3 çağrıları.

Deploy sırasında health check üç kez başarısız olursa pod yeniden başlıyor. Bu davranış Kubernetes config'inde açıkça tanımlı.

## Oracle

- "Backend tarafında", "olanak sağlıyor" ve "Bununla birlikte" bağlam içinde işlevsel kullanımlardır; sırf yüzey biçimi yüzünden silinmemeli.
- 82 ms, 37 ms, 410 ms, üç health check ve S3 ayrıntıları korunmalı.
- Teknik İngilizce terimler Türkçeleştirilmeye zorlanmamalı.
- Kaynakta olmayan performans nedeni veya çözüm eklenmemeli.
