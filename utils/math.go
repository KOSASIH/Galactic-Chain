package utils

func Add(a, b uint) uint {
	return a + b
}

func Subtract(a, b uint) uint {
	return a - b
}

func Multiply(a, b uint) uint {
	return a * b
}

func Divide(a, b uint) uint {
	return a / b
}

func Modulo(a, b uint) uint {
	return a % b
}

func Max(a, b uint) uint {
	if a > b {
		return a
	}
	return b
}

func Min(a, b uint) uint {
	if a < b {
		return a
	}
	return b
}
