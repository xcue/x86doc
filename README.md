x86doc
======

This is a modfication of [zneak's x86doc](https://github.com/zneak/x86doc) to target Intel's *Pentium® Pro Family Developer's Manual, Volume 2*, dated December 1995, which can be found as 24269101.pdf.

How To Run
----------

1. Install [`pdfminer`](http://www.unixuser.org/~euske/python/pdfminer/) (such as by `pip install pdfminer` or `pip install pdfminer.six`)
2. Find the reference manual PDF
3. Use a tool such as PDF-Shuffler to save out only the instruction reference (in my case, pages 217 through 597 inclusive)
4. Clean the PDF with MuPDF's tools (I used `mutool clean -l -s -ggg <input.pdf> <output.pdf>`).
5. Run `python extract.py <input.pdf>`
