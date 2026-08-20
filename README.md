---
title: "BacDive Veri İndirme"
author: "Meryem Su Tortuk"

---

# Giriş

Bu depo kapsamında BacDive veri tabanından veri indirme betikleri oluştururuz.

# Yöntem

## Girdi Listesinin Hazırlanma:
   data klasörüne taranacak bakteri türlerinin yer aldığı "species" metin dosyasını oluştururuz.

## Gerekli Kütüphanelerin Yüklenmesi:
   Veritabanı erişimi için bacdive, veri düzenleme ve tablo oluşturma işlemleri için pandas, veri yapılandırması için json kütüphanelerinı içe aktarırız.

## API Bağlantısının Kurulması:
   bacdive.BacdiveClient() fonksiyonu kullanılarak BacDive API sunucusu ile oturum başlatık.

## Tür Listesinin Okunması:
   species dosyası UTF-8 kodlamasıyla açılarak satır satır okunur. Boşluklar "strip()" ile temizlenir. Tür isimleri bir Python listesine aktarılır.