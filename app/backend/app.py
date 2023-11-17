from gradio_client import Client

file = 'recordings/d0b14fcb-288a-4439-ab74-ee7a92b535b0.wav'
cache_dir = 'cache'
client = Client("zomehwh/sovits-teio", output_dir=cache_dir)
result = client.predict(
				file,	# str (filepath or URL to file) in 'inputs' Audio component
				0,	# str in 'Task' Radio component
				True,
                '',	# str in 'Model' Radio component
                '',	# str in 'Model' Radio component
                False,
                fn_index=0,
)
print(result)