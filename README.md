# Kuro2-scripts

With CLE's release of Kuro 2, the game requires the compression and encryption of tbl and dat files in order to be accepted.These scripts just do that. Huge thanks to Twn for helping in making these scripts possible!

# Requirements
You will require
- zstandard
- blowfish
- python 3.10
in order to use these scripts

# Usage
After recompiling any dat or tbl file with KuroTools, run <python path> kuro_cle_compress.py <file name> then run <python path> kuro_cle_decrypt.py <file name>. The resulting file will be <file name>.compressed.encrypted, and after removing the .compressed and .encrytped from the filename, you can place the file back in the game folders and load the game.
