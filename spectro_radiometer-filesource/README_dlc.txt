Command line options for spectro_radiometer:

Usage: spectro_radiometer.py: [options]

Options:
  -h, --help            show this help message and exit
  --abw=ABW             Set Analog  bandwidth [default=4.0M]
  --antenna=ANTENNA     Set Antenna [default=RX2]
  --baseline=BASELINE   Set Baseline length [default=99.3]
  --bbgain=BBGAIN       Set Baseband Gain [default=5.0]
  --bw=BW               Set Bandwidth [default=-1.0M]
  --clock=CLOCK         Set Clock Source [default=default]
  --dcg=DCG             Set Detector DC Gain [default=100]
  --decln=DECLN         Set Observing Declination [default=0.0]
  --device=DEVICE       Set SDR Device Name [default=rtl=0
                        file=/dev/zero,rate=5e6]
  --fftsize=FFTSIZE     Set FFT size [default=2048]
  --frequency=FREQUENCY
                        Set Center Frequency [default=1.42041G]
  --gain=GAIN           Set RF Gain [default=30.0]
  --ifgain=IFGAIN       Set IF Gain [default=5.0]
  --latitude=LATITUDE   Set Local Latitude [default=44.9]
  --longitude=LONGITUDE
                        Set Local Longitude [default=-76.03]
  --mode=MODE           Set Operation Mode [default=total]
  --ppstime=PPSTIME     Set Time Source [default=internal]
  --prefix=PREFIX       Set Data File Prefix [default=h1]
  --ra=RA               Set Target RA [default=12.0]
  --rfilist=RFILIST     Set RFI Frequency List [default=]
  --srate=SRATE         Set Sample rate [default=2.56M]
  --zerotime=ZEROTIME   Set SIdereal time for auto baseline set [default=99.3]

Command line testing for spectro_radiometer:

Airspy:
spectro_radiometer_filesource.py --abw=250e3 --bw=250e3 --device="airspy=0 file=/dev/zero,rate=2.5e6" --frequency=1420.4058e6 --mode=total --srate=10e6 --latitude=37.79 --longitude=-77.92

July 28, 2018

Note:
I am able to make this work by replacing the OSMOCOMM source with
a file source that was recorded with the same settings (gain , sample rate, etc).
That allows me to record data at 10 MSPS without all of the overruns that
I have when trying to run the Airspy with any other software.

