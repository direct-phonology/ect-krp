# Early Chinese texts from the Kanseki Repository
This repository aggregates the Kanseki Repository's digital versions of 64 key texts from early China. The titles are drawn from Michael Loewe's bibliography of essential early Chinese texts<sup>1</sup>.

Note that **not all texts are represented** - both _Shenzi_ texts<sup>2</sup> are not included here. Neither text is extant in the Kanseki Repository, and sourcing digital versions is difficult due to the texts' severely fragmentary nature. Users seeking these texts are encouraged to visit the versions offered by the Chinese Text Project<sup>3</sup>.

Texts are preprocessed to remove paratext (e.g. commentaries), punctuation, whitespace, and non-Chinese characters. The aim is to produce output that can be used for machine learning, natural language processing, and other computational applications.

## Usage
### Downloading
You can download compressed archives of all texts from the [releases page](https://github.com/direct-phonology/ect-krp/releases).
### Updating
To generate your own cleaned copy from the latest sources, first run:
```sh
$ git submodule update --init
```
Then, you can run either of the two python scripts included in this repository to generate plaintext or json-lines files:
```sh
$ bin/org2txt.py     # for plaintext
$ bin/org2jsonl.py   # for json-lines
```
Note that the `jsonlines` python library must be installed for the latter. You can install it with:
```sh
$ pip install -r requirements.txt
```
To periodically update the Kanseki repository texts from the upstream source, you can run:
```sh
$ git submodule update --remote --merge
```
## Titles
|title|pinyin|wade-giles|source|
|-|-|-|-|
|戰國策|Zhan guo ce|Chan kuo ts'e|[KR2e0003](https://www.kanripo.org/text/KR2e0003/)|
|潛夫論|Qian fu lun|Ch'ien fu lun|[KR3a0010](https://www.kanripo.org/text/KR3a0010/)|
|九章算術|Jiǔzhāng Suànshù|Chiu chang suan shu|[KR3f0032](https://www.kanripo.org/text/KR3f0032/)|
|周禮|Zhōu lǐ|Chou li|[KR1d0002](https://www.kanripo.org/text/KR1d0002/)|
|周髀算經|Zhoubi Suanjing|Chou pi suan ching|[KR3f0001](https://www.kanripo.org/text/KR3f0001/)|
|竹書紀年|Zhúshū Jìnián|Chu shu chi nien|[KR2b0001](https://www.kanripo.org/text/KR2b0001/)|
|楚辭|Chu Ci|Ch'u tz'u|[KR4a0002](https://www.kanripo.org/text/KR4a0002/)|
|莊子|Zhuangzi|Chuang tzu|[KR5c0126](https://www.kanripo.org/text/KR5c0126/)|
|春秋公羊傳|Chūnqiū Gōngyáng zhuàn|Ch'un ch'iu kung yang|[KR1e0007](https://www.kanripo.org/text/KR1e0007/)|
|春秋穀梁傳|Chūnqiū Gǔliáng zhuàn|Ch'un ch'iu ku liang|[KR1e0008](https://www.kanripo.org/text/KR1e0008/)|
|春秋左傳|Chūnqiū Zuǒ zhuàn|Ch'un ch'iu tso chuan|[KR1e0001](https://www.kanripo.org/text/KR1e0001/)|
|春秋繁露|Chūnqiū fánlù|Ch'un ch'iu fan lu|[KR1e0122](https://www.kanripo.org/text/KR1e0122/)|
|中論|Zhonglun|Chung lun|[KR3a0012](https://www.kanripo.org/text/KR3a0012/)|
|爾雅|Erya|Erh ya|[KR1j0002](https://www.kanripo.org/text/KR1j0002/)|
|法言|Fayan|Fa yen|[KR3a0009](https://www.kanripo.org/text/KR3a0009/)|
|風俗通義|Fengsu Tongyi|Feng su t'ung i|[KR3j0081](https://www.kanripo.org/text/KR3j0081/)|
|漢記|Hanji|Han chi|[KR2b0003](https://www.kanripo.org/text/KR2b0003/)|
|韓非子|Han Feizi|Han fei tzu|[KR3c0005](https://www.kanripo.org/text/KR3c0005/)|
|韓詩外傳|Han shi waizhuan|Han shih wai chuan|[KR1c0066](https://www.kanripo.org/text/KR1c0066/)|
|漢書|Han Shu|Han shu|[KR2a0007](https://www.kanripo.org/text/KR2a0007/)|
|鶡冠子|Heguanzi|Ho kuan tzu|[KR3j0006](https://www.kanripo.org/text/KR3j0006/)|
|孝經|Xiao Jing|Hsiao ching|[KR1f0001](https://www.kanripo.org/text/KR1f0001/)|
|新序|Xin Xu|Hsin hsü|[KR3a0008](https://www.kanripo.org/text/KR3a0008/)|
|新論|Xin lun|Hsin lun|[KR3j0192](https://www.kanripo.org/text/KR3j0192/)|
|新書|Xin shu|Hsin shu|[KR3a0005](https://www.kanripo.org/text/KR3a0005/)|
|新語|Xin yu|Hsin yü|[KR3a0004](https://www.kanripo.org/text/KR3a0004/)|
|荀子|Xúnzǐ|Hsün tzu|[KR3a0002](https://www.kanripo.org/text/KR3a0002/)|
|淮南子|Huainanzi|Huai nan tzu|[KR3j0010](https://www.kanripo.org/text/KR3j0010/)|
|黃帝內經|Huangdi Neijing|Huang ti nei ching|[KR3e0001](https://www.kanripo.org/text/KR3e0001/)|
|易經|Yi Jing|I ching|[KR1a0001](https://www.kanripo.org/text/KR1a0001/)|
|逸周書|Yì Zhōu Shū|I Chou shu|[KR2d0001](https://www.kanripo.org/text/KR2d0001/)|
|儀禮|Yílǐ|I li|[KR1d0026](https://www.kanripo.org/text/KR1d0026/)|
|管子|Guānzǐ|Kuan tzu|[KR3c0001](https://www.kanripo.org/text/KR3c0001/)|
|公孫龍子|Gōngsūn Lóngzǐ|Kung sun Lung tzu|[KR3j0007](https://www.kanripo.org/text/KR3j0007/)|
|孔子家語|Kǒngzǐ Jiāyǔ|K'ung tzu chia yü|[KR3a0001](https://www.kanripo.org/text/KR3a0001/)|
|國語|Guoyu|Kuo yü|[KR2e0001](https://www.kanripo.org/text/KR2e0001/)|
|老子道德經|Laozi Dàodé Jīng|Lao tzu Tao te ching|[KR5c0057](https://www.kanripo.org/text/KR5c0057/)|
|禮記|Liji|Li chi|[KR1d0052](https://www.kanripo.org/text/KR1d0052/)|
|列子|Liezi|Lieh tzu|[KR5c0124](https://www.kanripo.org/text/KR5c0124/)|
|論衡|Lunheng|Lun heng|[KR3j0080](https://www.kanripo.org/text/KR3j0080/)|
|論語|Lúnyǔ|Lun yü|[KR1h0004](https://www.kanripo.org/text/KR1h0004/)|
|呂氏春秋|Lüshi Chunqiu|Lü shih ch'un ch'iu|[KR3j0009](https://www.kanripo.org/text/KR3j0009/)|
|孟子|Mengzi|Meng tzu|[KR1h0001](https://www.kanripo.org/text/KR1h0001/)|
|墨子|Mozi|Mo tzu|[KR3j0002](https://www.kanripo.org/text/KR3j0002/)|
|穆天子傳|Mù Tiānzǐ Zhuàn|Mu t'ien tzu chuan|[KR3l0092](https://www.kanripo.org/text/KR3l0092/)|
|白虎通|Báihǔ Tōng|Pai hu t'ung|[KR3j0023](https://www.kanripo.org/text/KR3j0023/)|
|山海經|Shan Hai Jing|Shan hai ching|[KR3l0090](https://www.kanripo.org/text/KR3l0090/)|
|商君書|Shāng jūn shū|Shang chün shu|[KR3c0004](https://www.kanripo.org/text/KR3c0004/)|
|尚書|Shangshu|Shang shu|[KR1b0001](https://www.kanripo.org/text/KR1b0001/)|
|申鑒|Shenjian|Shen chien|[KR3a0011](https://www.kanripo.org/text/KR3a0011/)|
|史記|Shiji|Shih chi|[KR2a0001](https://www.kanripo.org/text/KR2a0001/)|
|詩經|Shijing|Shih ching|[KR1c0001](https://www.kanripo.org/text/KR1c0001/)|
|釋名|Shiming|Shih ming|[KR1j0007](https://www.kanripo.org/text/KR1j0007/)|
|說文解字|Shuowen Jiezi|Shuo wen chieh tzu|[KR1j0018](https://www.kanripo.org/text/KR1j0018/)|
|說苑|Shuo Yuan|Shuo yüan|[KR3a0007](https://www.kanripo.org/text/KR3a0007/)|
|孫子兵法|Sunzi Bingfa|Sun tzu ping fa|[KR3b0003](https://www.kanripo.org/text/KR3b0003/)|
|大戴禮記|Dà Dài Lǐjì|Ta Tai Li chi|[KR1d0076](https://www.kanripo.org/text/KR1d0076/)|
|太玄經|Tài Xuán Jīng|T'ai hsüan ching|[KR3g0001](https://www.kanripo.org/text/KR3g0001/)|
|獨斷|Duduan|Tu tuan|[KR3j0024](https://www.kanripo.org/text/KR3j0024/)|
|東觀漢記|Dongguan Hanji|Tung kuan Han chi|[KR2d0002](https://www.kanripo.org/text/KR2d0002/)|
|吳越春秋|Wu Yue Chunqiu|Wu Yüeh ch'un ch'iu|[KR2i0001](https://www.kanripo.org/text/KR2i0001/)|
|鹽鐵論|Yán Tiě Lùn|Yen t'ieh lun|[KR3a0006](https://www.kanripo.org/text/KR3a0006/)|
|晏子春秋|Yanzi Chunqiu|Yen tzu ch'un ch'iu|[KR2g0003](https://www.kanripo.org/text/KR2g0003/)|
|越絕書|Yue Jue Shu|Yüeh chüeh shu|[KR2i0002](https://www.kanripo.org/text/KR2i0002/)|

## License
All Kanseki Repository texts are licensed [CC-BY-SA 4.0](https://creativecommons.org/licenses/by-sa/4.0/legalcode). See [LICENSE](LICENSE).

---

<sup>1</sup>Loewe, Michael, ed. _Early Chinese Texts: A Bibliographical Guide_. Early China Special Monograph Series, no. 2.Berkeley, Calif.: Society for the Study of Early China : Institute of East Asian Studies, University of California, Berkeley, 1993.

<sup>2</sup>Namely the _Shēnzi_ (申子, or 申不害) and the _Shènzi_ (慎子, or 慎到).

<sup>3</sup>See <https://ctext.org/shen-bu-hai> and <https://ctext.org/shenzi> respectively.
