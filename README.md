# Python unix sort

In order to start the container you need to first build the image it using:
  $ docker build -t <name-of-image>
and then start the container by:
  $ docker run -it -v <absolute-path-of-the-workdir-directory-in-your-file-system>:/workdir/ <name-of-image>.
  
The application will prompt you to provide the input file path and the output file path.
For input file path write
  /workdir/shuffled.csv
and for output file path write
  /workdir/sorted.csv
