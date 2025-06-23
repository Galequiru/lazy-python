from typing import Callable

type Lazy[T] = Callable[[], T]

def and_op(left: Lazy[bool], right: Lazy[bool]) -> Lazy[bool]:
	return lambda: False if not left() else right()

def or_op(left: Lazy[bool], right: Lazy[bool]) -> Lazy[bool]:
	return lambda: True if left() else right()

def print_and_return[T](message: str, value: T) -> Lazy[T]:
	def func() -> T:
		print(message)
		return value
	return func

def boolean_tests():
	f = print_and_return("evaluated false", False)
	t = print_and_return("evaluated true", True)

	# Created tests but not yet evaluated
	t_and_t = and_op(t, t)
	f_and_t = and_op(f, t)
	t_and_f = and_op(t, f)
	f_and_f = and_op(f, f)

	t_or_t = or_op(t, t)
	f_or_t = or_op(f, t)
	t_or_f = or_op(t, f)
	f_or_f = or_op(f, f)

	# evaluate and print tests
	print("True && True:", t_and_t(), end="\n\n")
	print("False && True:", f_and_t(), end="\n\n")
	print("True && False:", t_and_f(), end="\n\n")
	print("False && False:", f_and_f(), end="\n\n")

	print("True || True:", t_or_t(), end="\n\n")
	print("False || True:", f_or_t(), end="\n\n")
	print("True || False:", t_or_f(), end="\n\n")
	print("False || False:", f_or_f(), end="\n\n")

if __name__ == "__main__":
	boolean_tests()