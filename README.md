# KELOMPOK 1
![Group 1](https://user-images.githubusercontent.com/85054950/207575804-1b612218-1e41-49e8-9ded-af1c6dd2b660.png)


[![Generic badge](https://img.shields.io/badge/51-Iqbal%20Putra-<COLOR>.svg)](https://shields.io/)
[![Generic badge](https://img.shields.io/badge/52-Pasya%20Alvan-<COLOR>.svg)](https://shields.io/)
[![Generic badge](https://img.shields.io/badge/54-Lustiyana-<COLOR>.svg)](https://shields.io/)
[![Generic badge](https://img.shields.io/badge/21-Asma%20Zulfiah-<COLOR>.svg)](https://shields.io/)
[![Generic badge](https://img.shields.io/badge/56-Denta-<COLOR>.svg)](https://shields.io/)

# VISUALISASI DATA


---

> TEMA: QUALITY EDUCATION IN INDONESIA




### Ketua Proyek:Pasya Alvan Gail 

Anggota:<br>
* Asma Zulfiah Malik
* Iqbal Putra Ramadhan
* Lustiyana
* Denta Pratama Anggayana



#CRISP-DM
(Cross-Industry Standard Process for Data Mining) merupakan suatu konsorsium perusahaan yang didirikan oleh Komisi Eropa pada tahun 1996 dan telah ditetapkan sebagai proses standar dalam data mining yang dapat diaplikasikan di berbagai sektor industri. Gambar menjelaskan tentang siklus hidup pengembangan data mining.


## Business Understanding
Tahap pertama dari CRISP DM adalah Business Understanding yang merupakan tahap dimana Business problem didefinisikan dengan sederhana dan tepat. Meskipun terkesan sederhana pada hakikatnya tahapan ini memerlukan penguasaan pada dua bagian yang berbeda yaitu pemahaman terhadap business process termasuk regulasi yang mengaturnya dan pemahaman terhadap cara pengolahannya.


---


Dalam kasusnya Indonesia masih mengalami ketidak merataan pendidikan sehingga diperlukan upaya untuk menangani hal ini. Salah satu upaya pemerintah adalah dengan penggunaan sistem zonasi. Namun ada hal yang kurang dari sistem zonasi ini adalah ketidakmerataan fasilitas pendidikan di setiap daerah. Maka dari itu diperlukan fokus pembangunan sekolah sekolah untuk berbagai jenjang (SD, SMP, SMA, dan Perguruan Tinggi). Jika kita bisa menginisiasikan wilayah mana saja yang diperlukan pembangunan sekolah tiap jenjang nya maka ini dapat digunakan untuk upaya pemerataan pendidikan di Indonesia.


## Data Understanding
Data Understanding merupakan proses dimana kita mempertemukan antara data apa yang kita miliki dan data apa yang kita seharusnya perlukan. Bisa jadi suatu project data analisis berawal dari penemuan data-data yang telah ada yang kemudian mengarahkan analist untuk menggali knowledge yang ada pada kumpulan data tersebut. Jenis data akan sangat menentukan jenis algoritma dan tujuan dari data mining yang ingin dicapai

---

1. Kebutuhan Data
    Data yang dibutuhkan adalah data jumlah tenaga pengajar pendidik di Indonesia, persentase mengurangi kesalahan dalam pembagian dana pendidikan, persentase ketidakmerataan fasilitas pendidikan di setiap daerah

2. Pengambilan Data
  Data yang diambil berdasarkan data yang dikeluarkan oleh BPS. BPS merupakan Badan Pusat Statistik, dimana BPS ini lembaga yang menyediakan informasi data statistik pada skala nasional dan regional di Indonesia

3. Integrasi Data
  Berkaitan dengan data yang telah disediakan oleh BPS, yang merupakan data yang terbagi dalam satu kategori, kami melakukan integrasi dari setiap kategoti data yang kami perlukan.

4. Telaah Data
  Berdasarkan kategori data yang sudah terintegrasi sesuai dengan kebutuhan, data akan dihapus jika ada data yang ganda pada kategori tersebut.

5. Analisis Karakteristik Data
  Data yang digunakan merupakan data terstruktur, yang berupa numerikal atau angka. 

6. Validasi Data
  Data yang telah divalidasi sebagai persyaratan yang memenuhi dapat digunakan jika berupa persentase,  kisarannya adalah 0 hingga 1 atau 0% hingga 100%.
  
  
---

## Data Preparation
Untuk mempermudah dalam memvisualisasikan data, maka dilakukan persiapan data yang akan diolah dari sumber data yang telah disiapkan. Terdapat beberapa persiapan yang dilakukan, diantaranya adalah sebagai berikut:

---

### Negara yang digunakan Indonesia
Untuk menunjang tujuan teknis serta mempermudah dalam memvisualisasikan data, maka data yang disiapkan hanya data dari negara Indonesia saja.

### Merapihkan kategori sekolah
Pada sumber data yang digunakan, terdapat banyak murid sekolah dasar (SD) sampai dengan sekolah menengah astas (SMA), diambil rata-rata nya sebagai berikut.

| TAHUN | PROVINCE  | TP SD | TP SMP | TP SMA | MH Perempuan | MH Laki-Laki |
| ----- | --------- | ----- | ------ | ------ | ------------ | ------------ |
|2015|Aceh|96,47|89,01|68,16|96,53|97,63|
|2015|Sumatera Utara|92,76|80,87|59,54|98,04|98,68|
|2015|Sumatera Barat|87,85|78,77|58,04|97,85|98,56|
|2015|Riau|90,44|76,54|57,28|98,16|98,87|
|2015|Jambi|93,12|78,04|49,05|96,75|97,84|
|2015|Sumatera Selatan|90,27|78,35|48,9|97,52|98,22|
|2015|Bengkulu|92,15|78,16|55,94|96,27|97,63|
|2015|Lampung|94,46|76,68|40,6|94,89|96,67|
|2015|Kepulauan Bangka Belitung|90,05|70,35|43,46|96,78|97,63|
|2015|Kepulauan Riau|97,85|88,25|65,28|98,53|98,79|
|2015|DKI Jakarta|96,56|86,79|74,1|99,33|99,59|
|2015|Jawa Barat|92,42|79,09|48,53|97,14|98,01|
|2015|Jawa Tengah|92,91|78,96|43,86|90,01|93,12|
|2015|DI Yogyakarta|95,98|87,41|80,77|91,78|94,50|
|2015|Jawa Timur|91,76|80,98|52,04|88,17|91,47|
|2015|Banten|91,66|79,23|52,95|96,14|97,37|
|2015|Bali|96,73|85,95|69,08|88,94|92,77|
|2015|Nusa Tenggara Barat|94,4|84,04|51,83|83,50|86,97|
|2015|Nusa Tenggara Timur|78,94|66,62|37,78|90,12|91,45|
|2015|Kalimantan Barat|83,99|63,41|35,69|89,10|92,32|
|2015|Kalimantan Tengah|93,18|72,59|47,28|98,45|98,88|
|2015|Kalimantan Selatan|87,15|72,89|44,85|97,17|98,21|
|2015|Kalimantan Timur|94,65|85,13|67,56|98,12|98,69|
|2015|Kalimantan Utara|92,11|83,02|47,64|93,08|94,99|
|2015|Sulawesi Utara|93,41|82,35|55,5|99,56|99,63|
|2015|Sulawesi Tengah|87,06|77,31|45,84|96,41|97,34|
|2015|Sulawesi Selatan|91,18|78,08|50,85|89,47|91,29|
|2015|Sulawesi Tenggara|92,21|82,75|61,52|91,69|94,10|
|2015|Gorontalo|85,72|68,81|44,67|98,45|98,24|
|2015|Sulawesi Barat|90,27|75,58|39,29|90,88|92,64|
|2015|Maluku|91,56|86,29|58,59|98,39|98,85|
|2015|Maluku Utara|92,25|76,39|57,12|97,87|98,49|
|2015|Papua Barat|82,45|76,33|55,24|95,50|96,88|
|2015|Papua|62,34|50,57|28,23|65,47|70,83|
|...|...|...|...|...|...|...|
|2021|Papua|78,43|66,06|32,95|76,17|78,89|

Keterangan: 
- TP merupakan singkatan dari Tingkat Partisipasi
- MH merupakan singkatan dari Melek Huruf

## Data Visualization
![image](https://user-images.githubusercontent.com/85054950/207549152-77f57691-dfd7-4bf2-9044-6905b1b91e0c.png)




## MODELING
Modeling dibuat dengan bahasa python dengan bantuan library seaborn dan matplotlib dengan detail pada link berikut:
<br>
[![Open In Collab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/Lustiyana/Visualisasi-Data-Education-of-Indonesia-Kelompok-1/blob/main/Visualisasi_Data_Kelompok_1.ipynb)

---

## DASHBOARD
Berikut Dashboard untuk keseluruhan data terkait penyelesaian pendidikan di indonesia

![image](https://user-images.githubusercontent.com/85054950/209521785-81bf5aa5-a1b7-4e07-a0c2-bee988a00589.png)

---

