default: test

lint:
	make -C compiler lint
	make -C lib/c lint
	make -C lib/go lint
	make -C lib/py lint

test:
	pytest tests -v -s -x
