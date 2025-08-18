$$
\sigma(x) = \frac{1}{1+e^{-x}}
$$

$$
\begin{align}
\sigma'(x) &= \frac{-1}{(1+e^{-x})^2}(1+e^{-x})' \\
           &= \frac{-1}{(1+e^{-x})^2}(-e^{-x}) \\
           &= \frac{e^{-x}}{(1+e^{-x})^2} \\
           &= \frac{1}{1+e^{-x}}\frac{e^{-x}}{1+e^{-x}} \\
           &= \sigma(x)\frac{1 + e^{-x} - 1}{1+e^{-x}} \\
           &= \sigma(x)(1 - \frac{1}{1 + e^{-x}}) \\
           &= \sigma(x)[1 - \sigma(x)]
\end{align}
$$