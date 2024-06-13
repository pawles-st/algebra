x <- seq(-6, 6, length = 1000)
y <- seq(-8, 1, length = 1000)
z <- outer(x, y, function(x, y) (x^2 + y^2 + 4*y)^2 - 16 * (x^2 + y^2))
contour(x, y, z, levels = 0)

x <- seq(-10, 10, length = 1000)
y <- seq(-10, 10, length = 1000)
z <- outer(x, y, function(x, y) 2 * (x^2 + 9) * (y^2 - 16) + (x^2 - 9)^2 + (y^2 - 16)^2)
contour(x, y, z, levels = 0)

x <- seq(-1, 1, length = 1000)
y <- seq(-1, 1, length = 1000)
z <- outer(x, y, function(x, y) 350 * x^2 * y^2 - 15^2 * (x^2 + y^2) + 12^2 * (x^4 + y^4) + 81)
contour(x, y, z, levels = 0)
