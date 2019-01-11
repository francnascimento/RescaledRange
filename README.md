# RescaledRange ![Language Badge](https://img.shields.io/badge/Language-Python-red.svg) ![License Badge](https://img.shields.io/badge/License-MIT-blue.svg)

A program and module that use a technique of statistical analysis for time series(Rescaled Range), which aims to find the Hurst exponent: https://en.wikipedia.org/wiki/Rescaled_range

### The Hurst exponent

Calculates the generalized Hurst exponent of a time series. The Hurst exponent gives a value indicating the long-term memory of a time-series, similar to the decay of a autocorrelation function: https://en.wikipedia.org/wiki/Hurst_exponent

### Example

```bash
init.py series [exponent]

Calculate the Hurst exponent

positional arguments:
  series             A list with all data in floats/ints

optional arguments:
  exponent           Determine the range of the analysis, based on exponents of the number 2, so if 1 is passed then will be calculated the range 1/2, if 2 it will be calculated for 1/2 and 1/4, if 3 for 1/2, 1/4 and 1/8, and so on. If nothing is passed, will be calculate to the more accurate range

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

This project is free to use according to the [MIT License](https://github.com/francnascimento/RescaledRange/blob/master/LICENSE) as long as you cite me and the License (read the License for more details). You can cite me by pointing to the following link:
- https://github.com/francnascimento/RescaledRange

