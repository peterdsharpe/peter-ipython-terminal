import time

start = time.time()

import contextlib



@contextlib.contextmanager
def timing():
	start_ns = time.time_ns()
	yield
	end_ns = time.time_ns()
	elapsed = (end_ns - start_ns) / 1e9
	print(f"{elapsed} sec")




import numpy as np

def wa(
		query: str,
		more_details=False
) -> str:
	"""
	Calls WolframAlpha on a string query.
	:param query:
	:return:
	"""
	import wolframalpha

	client = wolframalpha.Client()



print(f"Peter's Python Terminal"
	f" (started in {1000*(time.time() - start):.0f} ms)"
)
del start