# Speaker identification using domain adaptation of speaking and singing voice

This project is an attempt to apply the paper: 
[Domain Adaptation for Speaker Recognition in Singing and Spoken Voice](https://ieeexplore.ieee.org/document/9746111)

## Dataset

**Speaking Data:**
At the time of this writing, the dataset for [Voxceleb V2](https://www.robots.ox.ac.uk/~vgg/data/voxceleb/vox2.html)  has been revoked from the official website. Due to lack of time, I have used previously (thankfully, since it is not available officially now) downloaded [VoxCeleb V1](https://www.robots.ox.ac.uk/~vgg/data/voxceleb/vox1.html) dataset. VoxCeleb V1 dataset is used for the speaking audio for the... (to be finished)

VoxCeleb V2 is also available now. I am using it as directed in the research paper. There are a total of 1092009 .wav files now for VoxCelebV2.

**Singing Data**: The singing data that has been used is [JukeBox V1](https://iprobe.cse.msu.edu/dataset_detail.php?id=8&?title=JukeBox:_A_Speaker_Recognition_Dataset_with_Multi-lingual_Singing_Voice_Audio). The access to this data is not instant and required filling up a form. The version 2 of the dataset [JukeBox V2](https://iprobe.cse.msu.edu/dataset_detail.php?id=9) contains both speaking and singing audio files.


 Due to lack of time, as the owners give access in a couple of months, I have used JukeBox V1 (previously accessed) and VoxCeleb V1 for this project (more data getting collected).

 ## Data collected

 `06.06.2023`

 I think downloading VoxCeleb V2 will also help in creating a larger dataset for my project. 

>:warning: `id05348` and `id04170` are not available in VoxCeleb_V2 `test` folder as stated in [vox2_meta.csv](/netscratch/rsharma/voice-recognition-speak-sing/VoxCeleb_1_2/V2/vox2_meta.csv)

`30.05.2023`

<br>

<div class="table-wrapper" markdown="block">

 | artist_name | voxceleb_id | jukebox_id | singing_time | speaking_time | vox_path | juke_path
 | :---:  | :---:  | :---:  | :---:  | :---:  | :---:  | :---: 
 |marie_osmond| id10742|842|239|690|/netscratch/rsharma/voice-recognition-speak-sing/data/speaking/marie_osmond|/netscratch/rsharma/voice-recognition-speak-sing/data/singing/marie_osmond|
|lea_salonga|id10679|790|239|1957|/netscratch/rsharma/voice-recognition-speak-sing/data/speaking/lea_salonga|/netscratch/rsharma/voice-recognition-speak-sing/data/singing/lea_salonga
|bruno_mars|id10115|452|239|611|/netscratch/rsharma/voice-recognition-speak-sing/data/speaking/bruno_mars|/netscratch/rsharma/voice-recognition-speak-sing/data/singing/bruno_mars
|smokey_robinson|id11098|1046|239|2447|/netscratch/rsharma/voice-recognition-speak-sing/data/speaking/smokey_robinson|/netscratch/rsharma/voice-recognition-speak-sing/data/singing/smokey_robinson
|miley_cyrus|id10825|892|239|2945|/netscratch/rsharma/voice-recognition-speak-sing/data/speaking/miley_cyrus|/netscratch/rsharma/voice-recognition-speak-sing/data/singing/miley_cyrus
|amanda_seyfried|id10041|359|239|1132|/netscratch/rsharma/voice-recognition-speak-sing/data/speaking/amanda_seyfried|/netscratch/rsharma/voice-recognition-speak-sing/data/singing/amanda_seyfried
|josh_groban|id10564|727|239|2555|/netscratch/rsharma/voice-recognition-speak-sing/data/speaking/josh_groban|/netscratch/rsharma/voice-recognition-speak-sing/data/singing/josh_groban
|nicole_scherzinger|id10880|924|239|1164|/netscratch/rsharma/voice-recognition-speak-sing/data/speaking/nicole_scherzinger|/netscratch/rsharma/voice-recognition-speak-sing/data/singing/nicole_scherzinger
|rita_ora|id10981|990|239|933|/netscratch/rsharma/voice-recognition-speak-sing/data/speaking/rita_ora|/netscratch/rsharma/voice-recognition-speak-sing/data/singing/rita_ora
|cyndi_lauper|id10180|503|239|1311|/netscratch/rsharma/voice-recognition-speak-sing/data/speaking/cyndi_lauper|/netscratch/rsharma/voice-recognition-speak-sing/data/singing/cyndi_lauper
|stevie_wonder|id11127|1057|239|525|/netscratch/rsharma/voice-recognition-speak-sing/data/speaking/stevie_wonder|/netscratch/rsharma/voice-recognition-speak-sing/data/singing/stevie_wonder
|troye_sivan|id11192|1128|239|761|/netscratch/rsharma/voice-recognition-speak-sing/data/speaking/troye_sivan|/netscratch/rsharma/voice-recognition-speak-sing/data/singing/troye_sivan
|meat_loaf|id10786|867|239|3121|/netscratch/rsharma/voice-recognition-speak-sing/data/speaking/meat_loaf|/netscratch/rsharma/voice-recognition-speak-sing/data/singing/meat_loaf
|chris_martin|id10157|1162|239|842|/netscratch/rsharma/voice-recognition-speak-sing/data/speaking/chris_martin|/netscratch/rsharma/voice-recognition-speak-sing/data/singing/chris_martin
|carrie_underwood|id10130|466|239|1896|/netscratch/rsharma/voice-recognition-speak-sing/data/speaking/carrie_underwood|/netscratch/rsharma/voice-recognition-speak-sing/data/singing/carrie_underwood
|cher|id10148|475|239|1987|/netscratch/rsharma/voice-recognition-speak-sing/data/speaking/cher|/netscratch/rsharma/voice-recognition-speak-sing/data/singing/cher
|lea_michele|id10678|789|239|887|/netscratch/rsharma/voice-recognition-speak-sing/data/speaking/lea_michele|/netscratch/rsharma/voice-recognition-speak-sing/data/singing/lea_michele
|kylie_minogue|id10666|776|239|688|/netscratch/rsharma/voice-recognition-speak-sing/data/speaking/kylie_minogue|/netscratch/rsharma/voice-recognition-speak-sing/data/singing/kylie_minogue
|sammy_davis_jr.|id11035|1020|239|802|/netscratch/rsharma/voice-recognition-speak-sing/data/speaking/sammy_davis_jr.|/netscratch/rsharma/voice-recognition-speak-sing/data/singing/sammy_davis_jr.
|blake_shelton|id10095|420|239|923|/netscratch/rsharma/voice-recognition-speak-sing/data/speaking/blake_shelton|/netscratch/rsharma/voice-recognition-speak-sing/data/singing/blake_shelton
|lorde|id10703|814|239|433|/netscratch/rsharma/voice-recognition-speak-sing/data/speaking/lorde|/netscratch/rsharma/voice-recognition-speak-sing/data/singing/lorde
|kenny_rogers|id10635|761|239|3070|/netscratch/rsharma/voice-recognition-speak-sing/data/speaking/kenny_rogers|/netscratch/rsharma/voice-recognition-speak-sing/data/singing/kenny_rogers
|jill_scott|id10499|682|237|714|/netscratch/rsharma/voice-recognition-speak-sing/data/speaking/jill_scott|/netscratch/rsharma/voice-recognition-speak-sing/data/singing/jill_scott

</div>



 ## Methodology

 ## Results