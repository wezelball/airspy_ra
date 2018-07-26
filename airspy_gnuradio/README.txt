I have somewhat figured out the format of the airspy file, at least
when create by GnuRadio. I get good results when I use airspy_gr.grc
to produce the data with the current defaults, then plot it with
the following script (from gr-utils):

python plot_psd_base.py -d complex64 --sample-rate=2.5e6 --enable-spec  
	--block=8192 --spec-size=128 airspy_iqdata.dat

I could use this for averaging plots, but recording data this way 
consumes huge amounts of disk space.  I actually need to save the FFT
data to disk, not the IQ data, but this is a start.


I wote the grc app airspy_read_raw_iq.grc, where I recorded raw data at 10 msps to disk, and tried to read it
under gnuradio, with following results:

The airspy_read_raw_iq.grc is able to read the airspy file created with the following command:

airspy_rx -t 0 -r ./airspyiq.dat -a 0 -f 88.9 -g 18 -n 50000000

Format FLOAT32 I/Q (64 bits per sample)
Sample rate 10e6 sps
400MB disk space
5.981 sec
66 Mbytes disk space per second

A 1TB hard drive would record 15,151 sec or 252 minutes or 4.2 hours of data.
