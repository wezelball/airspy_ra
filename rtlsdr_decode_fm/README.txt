This is an excellent tutorial on signal processing in numpy, scipy, and
matplotlib.  This would be a good springboard to write the RA program.

To use, read the PDF, and select a radio station by setting the 
value F_station to its frequency.  I used a local public radio station.

The program runs headless and produces a series of PDF files that 
illustrate different operations beging performed in the signal, in
order.  

The last file produced is a raw audio file.  Directions for playing it
are in the PDF as well as in comments in the python code.

The intent is to produce a version of this program using the airspy,
which far outperforms the rtl-sdr.  At that point, I can start on a
specialized receiver for radio astronomy.
