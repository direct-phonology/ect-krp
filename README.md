# Early Chinese texts from the Kanseki Repository
This repository aggregates the Kanseki Repository's digital versions of 64 key texts from early China. The titles are drawn from Michael Loewe's bibliography of essential early Chinese texts<sup>1</sup>.

Note that **not all texts are represented** - both _Shenzi_ texts<sup>2</sup> are not included here. Neither text is extant in the Kanseki Repository, and sourcing digital versions is difficult due to the texts' severely fragmentary nature. Users seeking these texts are encouraged to visit the versions offered by the Chinese Text Project<sup>3</sup>.

## Usage
### Downloading
You can download compressed archives of all texts from the [releases page](https://github.com/direct-phonology/ect-krp/releases).
### Updating
To generate your own cleaned copy from the latest sources, first run:
```sh
$ git submodule update --remote --merge
```
Then, you can run either of the two scripts included in this repository to generate plaintext or json-lines files:
```sh
$ python org2txt.py     # for plaintext
$ python org2jsonl.py   # for json-lines
```
Note that the `jsonlines` library must be installed for the latter. You can install it with:
```sh
$ pip install -r requirements.txt
```
## Titles
|title|wade-giles|source|
|-|-|-|
|戰國策|Chan kuo ts'e|[KR2e0003](https://www.kanripo.org/text/KR2e0003/)|
|潛夫論|Ch'ien fu lun|[KR3a0010](https://www.kanripo.org/text/KR3a0010/)|
|九章算術iǔzhāng Suànshù|Chiu chang suan shu|[KR3f0032](https://www.kanripo.org/text/KR3f0032/)|
|周禮|Chou li|[KR1d0002](https://www.kanripo.org/text/KR1d0002/)|
|周髀算經|Chou pi suan ching|[KR3f0001](https://www.kanripo.org/text/KR3f0001/)|
|竹書紀年|Chu shu chi nien|[KR2b0001](https://www.kanripo.org/text/KR2b0001/)|
|楚辭|Ch'u tz'u|[KR4a0002](https://www.kanripo.org/text/KR4a0002/)|
|莊子|Chuang tzu|[KR5c0126](https://www.kanripo.org/text/KR5c0126/)|
|春秋公羊傳|Ch'un ch'iu kung yang|[KR1e0007](https://www.kanripo.org/text/KR1e0007/)|
|春秋穀梁傳|Ch'un ch'iu ku liang|[KR1e0008](https://www.kanripo.org/text/KR1e0008/)|
|春秋左傳|Ch'un ch'iu tso chuan|[KR1e0001](https://www.kanripo.org/text/KR1e0001/)|
|春秋繁露|Ch'un ch'iu fan lu|[KR1e0122](https://www.kanripo.org/text/KR1e0122/)|
|中論|Chung lun|[KR3a0012](https://www.kanripo.org/text/KR3a0012/)|
|爾雅|Erh ya|[KR1j0002](https://www.kanripo.org/text/KR1j0002/)|
|法言|Fa yen|[KR3a0009](https://www.kanripo.org/text/KR3a0009/)|
|風俗通義|Feng su t'ung i|[KR3j0081](https://www.kanripo.org/text/KR3j0081/)|
|漢記|Han chi|[KR2b0003](https://www.kanripo.org/text/KR2b0003/)|
|韓非子|Han fei tzu|[KR3c0005](https://www.kanripo.org/text/KR3c0005/)|
|韓詩外傳|Han shih wai chuan|[KR1c0066](https://www.kanripo.org/text/KR1c0066/)|
|漢書|Han shu|[KR2a0007](https://www.kanripo.org/text/KR2a0007/)|
|鶡冠子|Ho kuan tzu|[KR3j0006](https://www.kanripo.org/text/KR3j0006/)|
|孝經|Hsiao ching|[KR1f0002](https://www.kanripo.org/text/KR1f0002/)|
|新序|Hsin hsü|[KR3a0008](https://www.kanripo.org/text/KR3a0008/)|
|新論|Hsin lun|[KR3j0192](https://www.kanripo.org/text/KR3j0192/)|
|新書|Hsin shu|[KR3a0005](https://www.kanripo.org/text/KR3a0005/)|
|新語|Hsin yü|[KR3a0004](https://www.kanripo.org/text/KR3a0004/)|
|荀子|Hsün tzu|[KR3a0002](https://www.kanripo.org/text/KR3a0002/)|
|淮南子|Huai nan tzu|[KR3j0010](https://www.kanripo.org/text/KR3j0010/)|
|黃帝內經|Huang ti nei ching|[KR3e0001](https://www.kanripo.org/text/KR3e0001/)|
|易經|I ching|[KR1a0001](https://www.kanripo.org/text/KR1a0001/)|
|逸周書|I Chou shu|[KR2d0001](https://www.kanripo.org/text/KR2d0001/)|
|儀禮|I li|[KR1d0026](https://www.kanripo.org/text/KR1d0026/)|
|管子|Kuan tzu|[KR3c0001](https://www.kanripo.org/text/KR3c0001/)|
|公孫龍子|Kung sun Lung tzu|[KR3j0007](https://www.kanripo.org/text/KR3j0007/)|
|孔子家語|K'ung tzu chia yü|[KR3a0001](https://www.kanripo.org/text/KR3a0001/)|
|國語|Kuo yü|[KR2e0001](https://www.kanripo.org/text/KR2e0001/)|
|老子道德經|Lao tzu Tao te ching|[KR5c0057](https://www.kanripo.org/text/KR5c0057/)|
|禮記|Li chi|[KR1d0052](https://www.kanripo.org/text/KR1d0052/)|
|列子|Lieh tzu|[KR5c0124](https://www.kanripo.org/text/KR5c0124/)|
|論衡|Lun heng|[KR3j0080](https://www.kanripo.org/text/KR3j0080/)|
|論語|Lun yü|[KR1h0004](https://www.kanripo.org/text/KR1h0004/)|
|呂氏春秋|Lü shih ch'un ch'iu|[KR3j0009](https://www.kanripo.org/text/KR3j0009/)|
|孟子|Meng tzu|[KR1h0001](https://www.kanripo.org/text/KR1h0001/)|
|墨子|Mo tzu|[KR3j0002](https://www.kanripo.org/text/KR3j0002/)|
|穆天子傳|Mu t'ien tzu chuan|[KR3l0092](https://www.kanripo.org/text/KR3l0092/)|
|白虎通|Pai hu t'ung|[KR3j0023](https://www.kanripo.org/text/KR3j0023/)|
|山海經|Shan hai ching|[KR3l0090](https://www.kanripo.org/text/KR3l0090/)|
|商君書|Shang chün shu|[KR3c0004](https://www.kanripo.org/text/KR3c0004/)|
|尚書|Shang shu|[KR1b0001](https://www.kanripo.org/text/KR1b0001/)|
|申鑒|Shen chien|[KR3a0011](https://www.kanripo.org/text/KR3a0011/)|
|史記|Shih chi|[KR2a0001](https://www.kanripo.org/text/KR2a0001/)|
|詩經|Shih ching|[KR1c0001](https://www.kanripo.org/text/KR1c0001/)|
|釋名|Shih ming|[KR1j0007](https://www.kanripo.org/text/KR1j0007/)|
|說文解字|Shuo wen chieh tzu|[KR1j0018](https://www.kanripo.org/text/KR1j0018/)|
|說苑|Shuo yüan|[KR3a0007](https://www.kanripo.org/text/KR3a0007/)|
|孫子兵法|Sun tzu ping fa|[KR3b0003](https://www.kanripo.org/text/KR3b0003/)|
|大戴禮記|Ta Tai Li chi|[KR1d0076](https://www.kanripo.org/text/KR1d0076/)|
|太玄經|T'ai hsüan ching|[KR3g0001](https://www.kanripo.org/text/KR3g0001/)|
|獨斷|Tu tuan|[KR3j0024](https://www.kanripo.org/text/KR3j0024/)|
|東觀漢記|Tung kuan Han chi|[KR2d0002](https://www.kanripo.org/text/KR2d0002/)|
|吳越春秋|Wu Yüeh ch'un ch'iu|[KR2i0001](https://www.kanripo.org/text/KR2i0001/)|
|鹽鐵論|Yen t'ieh lun|[KR3a0006](https://www.kanripo.org/text/KR3a0006/)|
|晏子春秋|Yen tzu ch'un ch'iu|[KR2g0003](https://www.kanripo.org/text/KR2g0003/)|
|越絕書|Yüeh chüeh shu|[KR2i0002](https://www.kanripo.org/text/KR2i0002/)|

## License
All Kanseki Repository texts are licensed [CC-BY-SA 4.0](https://creativecommons.org/licenses/by-sa/4.0/legalcode). See [LICENSE](LICENSE).

---

<sup>1</sup>Loewe, Michael, ed. _Early Chinese Texts: A Bibliographical Guide_. Early China Special Monograph Series, no. 2.Berkeley, Calif.: Society for the Study of Early China : Institute of East Asian Studies, University of California, Berkeley, 1993.

<sup>2</sup>Namely the _Shēnzi_ (申子, or 申不害) and the _Shènzi_ (慎子, or 慎到).

<sup>3</sup>See <https://ctext.org/shen-bu-hai> and <https://ctext.org/shenzi> respectively.