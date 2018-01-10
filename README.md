# RescaledRange ![Language Badge](https://img.shields.io/badge/Language-Python-red.svg) ![License Badge](https://img.shields.io/badge/License-MIT-blue.svg)

A program and module that use a technique of statistical analysis for time series(Rescaled Range), which aims to find the Hurst exponent: https://en.wikipedia.org/wiki/Rescaled_range

### The Hurst exponent

Calculates the generalized Hurst exponent of a time series. The Hurst exponent gives a value indicating the long-term memory of a time-series, similar to the decay of a autocorrelation function: https://en.wikipedia.org/wiki/Hurst_exponent


```bash
init.py series [exponent]

Calculate the Hurst exponent

positional arguments:
  series             A list with all data in floats/ints

optional arguments:
  exponent           Determine the range of the analysis, based on exponents of the number 2, so if 1 is passed  					   then will be calculated the range 1/2, if 2 it will be calculated for 1/2 and 1/4, if 3 for 					   1/2, 1/4 and 1/8, and so on. If nothing is passed, will be calculate to the more accurate range

```

## Contributing

### Bug Reports & Feature Requests

Please use the [issue tracker](https://github.com/francnascimento/RescaledRange/issues) to report any bugs or file feature requests.

## Social Coding

1. Create an issue to discuss about your idea
2. [Fork it] (https://github.com/francnascimento/RescaledRange/fork)
3. Create your feature branch (`git checkout -b my-new-feature`)
4. Commit your changes (`git commit -am 'Add some feature'`)
5. Push to the branch (`git push origin my-new-feature`)
6. Create a new Pull Request
7. Profit! :white_check_mark:

## License

The MIT License (MIT)

Copyright (c) 2013-2018 Francisco Nascimento

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in
all copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT.  IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN
THE SOFTWARE.

