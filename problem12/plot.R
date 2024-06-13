par(mfrow = c(2,3))

for (a in c(-4, -2, 0, 1, 2, 3)) {
	x <- seq(-10, 10, len = 100)
	y <- seq(-10, 10, len = 100)
	z <- outer(x, y, function(x, y) (x^2 + y^2) * (x - 1) - a * x^2)
	contour(x, y, z, levels = 0, main = paste0("Conhoid of de Sluze, a = ", a))
}

