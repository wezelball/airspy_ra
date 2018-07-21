I have somewhat figured out the format of the airspy file, at least
when create by GnuRadio. I get good results when I use airspy_gr.grc
to produce the data with the current defaults, then plot it with
the following script (from gr-utils):

python plot_psd_base.py -d complex64 --sample-rate=2.5e6 --enable-spec  
	--block=8192 --spec-size=128 airspy_iqdata.dat

I could use this for averaging plots, but recording data this way 
consumes huge amounts of disk space.  I actually need to save the FFT
data to disk, not the IQ data, but this is a start.
