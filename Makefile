.PHONY: build run

build:
	docker build -t my-blockchain-image .

run:
	docker run -p 8080:8080 my-blockchain-image
