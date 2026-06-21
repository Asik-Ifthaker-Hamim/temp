
def draw_base_triangle(base: int, char: str = "*") -> None:
	"""Draw a right-angled triangle with given base length using the specified character."""
	if base <= 0:
		print("Base must be a positive integer.")
		return
	for i in range(1, base + 1):
		print(char * i)


if __name__ == "__main__":
	try:
		b = int(input("Enter base length (positive integer): "))
	except Exception:
		print("Invalid input.")
	else:
		draw_base_triangle(b)
