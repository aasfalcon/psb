# psb
Simple linux sound file browser and previewer. This is an early alpha version. It works great, but not well packaged yet.

== INSTALL

Do not use setup.py, it does not work.

git submodule init
git submodule update
cd vendor/wav2png/wav2png/build
make
cd ../../../../
cp vendor/wav2png/wav2png/bin/Linux/wav2png ./bin

cd vendor/samplerate/scilkits/samplerate
python3 setup.py build
python3 setup.py install

== RUN

python3 psb.py


== REQUIRMENTS

- python3
- cython3
- python packages:
	numpy
	soundfile
	JACK-client
	scikits.samplerate

== CHHANGELOG

0.1.1 - added waveform image
0.1.0 - initial version with file dialog
