setup:
	pip install -e .[devel]
	kinderstadt syncdb --all
	kinderstadt migrate --fake
