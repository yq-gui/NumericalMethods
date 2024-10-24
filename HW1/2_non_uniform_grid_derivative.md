## variables
$(x_1,y_1)$, $(x_2,y_2)$ and $(x_3,y_3)$ where $x_1<x_2<x_3$

## first derivative
Taylor expansions around $x_2$:
$$
y_1 = y_2 + f^{'}(x_2)(x_1-x_2) + \frac{f^{''}(x_2)}{2}(x_1-x_2)^2 + \mathcal{O}((x_1-x_2)^3)
$$

$$
y_3 = y_2 + f^{'}(x_2)(x_3-x_2) + \frac{f^{''}(x_2)}{2}(x_3-x_2)^2 + \mathcal{O}((x_3-x_2)^3)
$$

​Neglect higher order terms and eliminate terms with $f^{''}(x_2)$ :
$$
(y_1-y_2)(x_3-x_2)^2 - (y_3-y_2)(x_1-x_2)^2 = f^{'}(x_2)[(x_1-x_2)(x_3-x_2)^2 -(x_3-x_2)(x_1-x_2)^2]
$$

So that:
**$$
f^{'}(x_2) = \frac{(y_1-y_2)(x_3-x_2)^2 - (y_3-y_2)(x_1-x_2)^2}{(x_1-x_2)(x_3-x_2)(x_3-x_1)}
$$**

We can see that when $x_1$, $x_2$, $x_3$ are evenly spaced ($x_2-x_1=x_3-x_2=h$)
$$
f^{'}(x_2) = \frac{y_3 - y_1}{2h}
$$
reduced to central differencing formula.

## second derivative
Taylor expansions around $x_2$:
$$
y_1 = y_2 + f^{'}(x_2)(x_1-x_2) + \frac{f^{''}(x_2)}{2}(x_1-x_2)^2 + \frac{f^{'''}(x_2)}{6}(x_1-x_2)^3 + \mathcal{O}({(x_1-x_2)}^4)
$$

$$
y_3 = y_2 + f^{'}(x_2)(x_3-x_2) + \frac{f^{''}(x_2)}{2}(x_3-x_2)^2 + \frac{f^{'''}(x_2)}{6}(x_3-x_2)^3 + \mathcal{O}((x_3-x_2)^4)
$$

​Neglect higher order terms and eliminate terms with $f^{'''}(x_2)$ :
$$
(y_1-y_2)(x_3-x_2)^3 - (y_3-y_2)(x_1-x_2)^3 = f^{'}(x_2)[(x_1-x_2)(x_3-x_2)^3 -(x_3-x_2)(x_1-x_2)^3] \\+ \frac{f^{''}(x_2)}{2}[(x_1-x_2)^2(x_3-x_2)^3 -(x_3-x_2)^2(x_1-x_2)^3]
$$

So we have:
**$$
f^{''}(x_2) = 2\frac{-(y_1-y_2)(x_3-x_2) + (y_3-y_2)(x_1-x_2)}{(x_1-x_2)(x_3-x_2)(x_3-x_1)}
$$**

We can see that when $x_1$, $x_2$, $x_3$ are evenly spaced ($x_2-x_1=x_3-x_2=h$)
$$
f^{';}(x_2) = \frac{-h(y_1-y_2) - h(y_3-y_2)}{-2h^3}=\frac{y_1-2 y_2 +y_3}{2h^2}
$$
reduced to central differencing formula.